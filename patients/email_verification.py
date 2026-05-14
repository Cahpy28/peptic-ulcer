from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from datetime import timedelta
import secrets

from .models import EmailVerificationCode


class EmailVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{user.password}{user.email}{user.is_active}{timestamp}"


email_verification_token = EmailVerificationTokenGenerator()


def make_verification_url(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = email_verification_token.make_token(user)
    path = reverse("patients:verify_email", kwargs={"uidb64": uid, "token": token})
    return request.build_absolute_uri(path)


def verify_token(uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        return None
    if not email_verification_token.check_token(user, token):
        return None
    return user


def create_verification_code(user):
    code = f"{secrets.randbelow(900000) + 100000}"
    expires_at = timezone.now() + timedelta(seconds=settings.EMAIL_VERIFICATION_MAX_AGE)
    EmailVerificationCode.objects.filter(user=user, used=False).update(used=True)
    EmailVerificationCode.objects.create(user=user, code=code, expires_at=expires_at)
    return code


def verify_code(email, code):
    User = get_user_model()
    user = User.objects.filter(email__iexact=email, is_active=False).first()
    if not user:
        return None, "No unverified account was found for this email."

    verification = EmailVerificationCode.objects.filter(user=user, used=False).first()
    if not verification:
        return None, "No active verification code was found. Please request a new one."
    if verification.is_expired:
        verification.used = True
        verification.save(update_fields=["used"])
        return None, "This verification code has expired. Please request a fresh code."
    if verification.attempts >= 5:
        verification.used = True
        verification.save(update_fields=["used"])
        return None, "Too many incorrect attempts. Please request a fresh code."
    if verification.code != code:
        verification.attempts += 1
        verification.save(update_fields=["attempts"])
        return None, "The verification code is incorrect. Check your email and try again."

    verification.used = True
    verification.save(update_fields=["used"])
    return user, ""


def send_verification_email(request, user):
    verification_url = make_verification_url(request, user)
    verification_code = create_verification_code(user)
    context = {
        "user": user,
        "verification_url": verification_url,
        "verification_code": verification_code,
        "expires_hours": max(1, settings.EMAIL_VERIFICATION_MAX_AGE // 3600),
    }
    subject = "Verify your PUDPredict account"
    text_body = render_to_string("registration/email_verification.txt", context)
    html_body = render_to_string("registration/email_verification.html", context)
    message = EmailMultiAlternatives(subject, text_body, settings.DEFAULT_FROM_EMAIL, [user.email])
    message.attach_alternative(html_body, "text/html")
    message.send()
    return verification_url, verification_code
