# Deploy PUDPredict Live on Render

This guide turns the Django project into a live web app using Render + PostgreSQL.

## 1. Prepare Locally

Open VS Code terminal:

```powershell
cd "C:\Users\HP\Documents\PEPTIC ULCER DISEASE"
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py check
python manage.py collectstatic --noinput
```

## 2. Push Project to GitHub

Create a GitHub repository, then push this folder. Do not upload `.env`, `.venv`, `db.sqlite3`, or private Gmail passwords.

```powershell
git init
git add .
git commit -m "Prepare PUDPredict for deployment"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pudpredict.git
git push -u origin main
```

If `git` is not recognized, install Git for Windows first.

## 3. Create Render Web Service

1. Go to https://render.com
2. Create an account or sign in.
3. Click **New +**.
4. Choose **Blueprint** if using `render.yaml`, or choose **Web Service** manually.
5. Connect your GitHub repository.
6. Render will create the web service and PostgreSQL database.

## 4. Render Environment Variables

If using manual Web Service setup, add these variables:

```text
DEBUG=False
SECRET_KEY=generate-a-long-secret-key
ALLOWED_HOSTS=your-app-name.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-app-name.onrender.com
DATABASE_URL=Render PostgreSQL internal database URL
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-gmail-address@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=PUDPredict <your-gmail-address@gmail.com>
```

## 5. Render Build and Start Commands

Build command:

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

Start command:

```bash
gunicorn pudpredict.wsgi:application
```

## 6. After Deployment

Open your live link:

```text
https://your-app-name.onrender.com
```

Create a new account and verify email. If email does not send, check Render environment variables and Gmail app password.

## Important Notes

- Do not use `python manage.py runserver` in production.
- Do not upload `.env` to GitHub.
- Keep `DEBUG=False` on the live server.
- Use Render PostgreSQL or another real database for live deployment.
- Uploaded datasets and generated files may not persist permanently on Render free web services unless stored in database or external storage.
