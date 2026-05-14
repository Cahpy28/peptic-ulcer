const assessmentForm = document.querySelector("[data-assessment-form]");
const reportForm = document.querySelector("[data-report-form]");
const API_BASE = location.protocol === "file:" ? "http://127.0.0.1:8000" : "";

const samples = [
  {
    id: "PUD-2401",
    name: "Amina Yusuf",
    age: 42,
    risk: 78,
    severity: "High",
    symptoms: "Burning epigastric pain, melena alert, NSAID use",
    recommendation: "Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan",
    recommendations: ["Urgent clinician review, stop NSAIDs where appropriate, H. pylori test, PPI plan"]
  },
  {
    id: "PUD-2402",
    name: "Chinedu Okafor",
    age: 35,
    risk: 52,
    severity: "Medium",
    symptoms: "Nocturnal discomfort, nausea, high stress pattern",
    recommendation: "Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms",
    recommendations: ["Schedule review, evaluate H. pylori, dietary counseling, monitor symptoms"]
  },
  {
    id: "PUD-2403",
    name: "Grace Mensah",
    age: 29,
    risk: 24,
    severity: "Low",
    symptoms: "Intermittent dyspepsia, no alarm symptoms",
    recommendation: "Lifestyle guidance, symptom tracking, routine follow-up if persistent",
    recommendations: ["Lifestyle guidance, symptom tracking, routine follow-up if persistent"]
  }
];

let assessmentCache = [];

function setActiveNav() {
  const current = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach((link) => {
    const href = link.getAttribute("href");
    const match = link.getAttribute("data-nav-match");
    link.classList.toggle(
      "active",
      href === current ||
      (current === "" && href === "index.html") ||
      (match && location.pathname.includes(match))
    );
  });
}

function initUiEffects() {
  document.body.classList.toggle("app-bg", !document.querySelector(".hero"));

  const revealItems = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("visible"));
  }

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener("click", (event) => {
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  document.querySelectorAll("[data-loading-form]").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (button) {
        button.classList.add("loading");
        button.innerHTML = "Processing...";
      }
    });
  });

  document.querySelectorAll(".accordion-trigger").forEach((trigger) => {
    trigger.addEventListener("click", () => {
      const item = trigger.closest(".accordion-item");
      if (!item) return;
      item.classList.toggle("open");
      if (window.lucide) window.lucide.createIcons();
    });
  });

  const advisorForm = document.querySelector("[data-advisor-form]");
  const advisorMessage = advisorForm ? advisorForm.querySelector("textarea") : null;

  document.querySelectorAll("[data-question]").forEach((button) => {
    button.addEventListener("click", () => {
      if (!advisorMessage) return;
      advisorMessage.value = button.getAttribute("data-question") || "";
      advisorMessage.focus();
      if (button.getAttribute("data-auto-submit") === "true" && advisorForm) {
        advisorForm.requestSubmit();
      }
    });
  });

  document.querySelectorAll("[data-clear-chat]").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll(".advisor-response").forEach((response) => response.remove());
      document.querySelectorAll(".chat-row.user").forEach((row) => row.remove());
      if (advisorMessage) advisorMessage.value = "";
    });
  });

  if (advisorForm && advisorMessage) {
    advisorMessage.addEventListener("input", () => {
      advisorMessage.style.height = "auto";
      advisorMessage.style.height = `${Math.min(advisorMessage.scrollHeight, 180)}px`;
    });
  }
}

function severityFromScore(score) {
  if (score >= 70) return "High";
  if (score >= 40) return "Medium";
  return "Low";
}

function badgeClass(severity) {
  return String(severity || "low").toLowerCase();
}

function computeRisk(data) {
  let score = 8;
  score += Number(data.age || 0) > 55 ? 12 : Number(data.age || 0) > 40 ? 7 : 2;
  score += Number(data.pain || 0) * 6;
  score += data.nsaid === "yes" ? 15 : data.nsaid === "sometimes" ? 8 : 0;
  score += data.hpylori === "positive" ? 18 : data.hpylori === "unknown" ? 8 : 0;
  score += data.bleeding === "yes" ? 20 : 0;
  score += data.smoking === "yes" ? 8 : 0;
  score += data.alcohol === "high" ? 8 : data.alcohol === "moderate" ? 4 : 0;
  score += data.stress === "high" ? 7 : data.stress === "moderate" ? 3 : 0;
  return Math.max(3, Math.min(96, Math.round(score)));
}

function recommendationsFor(severity, data) {
  const list = [];
  if (severity === "High") {
    list.push("Prioritize clinician review and screen immediately for alarm symptoms or bleeding.");
    list.push("Run H. pylori confirmation where status is unknown and document medication history.");
    list.push("Generate a structured report for gastroenterology referral or urgent review.");
  } else if (severity === "Medium") {
    list.push("Schedule follow-up assessment and track pain frequency, triggers, and response to therapy.");
    list.push("Recommend H. pylori testing if not recently confirmed.");
    list.push("Review NSAID exposure, diet, alcohol use, smoking, and stress contributors.");
  } else {
    list.push("Provide lifestyle guidance and symptom monitoring with routine reassessment.");
    list.push("Escalate if pain worsens, vomiting occurs, weight loss appears, or bleeding is suspected.");
    list.push("Keep baseline patient record for future model comparison.");
  }

  if (data.nsaid === "yes") list.push("Flag frequent NSAID use as a modifiable ulcer risk factor.");
  if (data.bleeding === "yes") list.push("Bleeding symptoms require urgent medical evaluation.");
  return list;
}

async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || "Backend request failed.");
  }
  return payload;
}

function readLocalAssessments() {
  const saved = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  return saved.length ? saved : samples;
}

async function loadAssessments() {
  try {
    const payload = await apiRequest("/api/patients");
    assessmentCache = payload.patients.length ? payload.patients : samples;
  } catch (error) {
    assessmentCache = readLocalAssessments();
  }
  return assessmentCache;
}

function saveLocalAssessment(record) {
  const existing = JSON.parse(localStorage.getItem("pudAssessments") || "[]");
  existing.unshift(record);
  localStorage.setItem("pudAssessments", JSON.stringify(existing.slice(0, 20)));
}

function updateResult(score, severity, recommendations) {
  const scoreText = document.querySelector("[data-score]");
  const severityText = document.querySelector("[data-severity]");
  const ring = document.querySelector("[data-score-ring]");
  const recommendationList = document.querySelector("[data-recommendations]");
  if (!scoreText || !severityText || !ring || !recommendationList) return;

  scoreText.textContent = `${score}%`;
  severityText.textContent = `${severity} Risk`;
  const degrees = Math.round((score / 100) * 360);
  const color = severity === "High" ? "#c04444" : severity === "Medium" ? "#f2a03a" : "#24895a";
  ring.style.background = `conic-gradient(${color} 0deg, ${color} ${degrees}deg, #e8eef3 ${degrees}deg 360deg)`;
  recommendationList.innerHTML = recommendations.map((item) => `<li>${item}</li>`).join("");
}

function renderPatientTable(items = assessmentCache) {
  const body = document.querySelector("[data-patient-table]");
  if (!body) return;
  body.innerHTML = items.map((item) => `
    <tr>
      <td><strong>${item.id}</strong><br><span class="muted">${item.name}</span></td>
      <td>${item.age}</td>
      <td>${item.symptoms}</td>
      <td><span class="badge ${badgeClass(item.severity)}">${item.severity}</span></td>
      <td>${item.risk}%</td>
    </tr>
  `).join("");
}

function renderPredictionCards(items = assessmentCache) {
  const target = document.querySelector("[data-prediction-cards]");
  if (!target) return;
  target.innerHTML = items.slice(0, 6).map((item) => `
    <article class="card">
      <div class="card-icon"><i data-lucide="activity"></i></div>
      <h3>${item.name}</h3>
      <p><strong>${item.risk}% ${item.severity} risk</strong></p>
      <p>${item.recommendation}</p>
    </article>
  `).join("");
  if (window.lucide) window.lucide.createIcons();
}

function normalizeRecommendations(item) {
  if (Array.isArray(item.recommendations)) return item.recommendations;
  if (item.recommendations_json) {
    try {
      return JSON.parse(item.recommendations_json);
    } catch (error) {
      return [item.recommendation];
    }
  }
  return [item.recommendation];
}

function renderReportPreview(record) {
  const target = document.querySelector("[data-report-preview]");
  if (!target) return;
  const item = record || assessmentCache[0] || samples[0];
  const recommendations = normalizeRecommendations(item);
  target.innerHTML = `
    <header>
      <div>
        <h3>Intelligent PUD Management Report</h3>
        <p class="muted">Extreme Gradient Algorithm assessment summary</p>
      </div>
      <strong>${item.id}</strong>
    </header>
    <section>
      <h3>Patient</h3>
      <p>${item.name}, ${item.age} years</p>
    </section>
    <section>
      <h3>Prediction</h3>
      <p><span class="badge ${badgeClass(item.severity)}">${item.severity}</span> ${item.risk}% estimated PUD management risk</p>
    </section>
    <section>
      <h3>Clinical Notes</h3>
      <p>${item.symptoms}</p>
    </section>
    <section>
      <h3>Recommendations</h3>
      <ul class="recommendations">${recommendations.map((text) => `<li>${text}</li>`).join("")}</ul>
    </section>
  `;
}

function populateReportOptions(items = assessmentCache) {
  const select = document.querySelector("[data-report-patient]");
  if (!select) return;
  select.innerHTML = items.map((item) => `<option value="${item.id}">${item.id} - ${item.name}</option>`).join("");
}

async function createAssessment(formData) {
  try {
    const payload = await apiRequest("/api/assessments", {
      method: "POST",
      body: JSON.stringify(formData)
    });
    return payload.assessment;
  } catch (error) {
    const score = computeRisk(formData);
    const severity = severityFromScore(score);
    const recommendations = recommendationsFor(severity, formData);
    const record = {
      id: `PUD-${Date.now().toString().slice(-5)}`,
      name: formData.name || "New Patient",
      age: formData.age || "N/A",
      risk: score,
      severity,
      symptoms: formData.symptoms || "New assessment captured from clinical input.",
      recommendation: recommendations[0],
      recommendations
    };
    saveLocalAssessment(record);
    return record;
  }
}

if (assessmentForm) {
  assessmentForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = Object.fromEntries(new FormData(assessmentForm).entries());
    const submitButton = assessmentForm.querySelector("button[type='submit']");
    if (submitButton) submitButton.disabled = true;

    try {
      const record = await createAssessment(formData);
      updateResult(record.risk, record.severity, normalizeRecommendations(record));
      assessmentCache.unshift(record);
    } finally {
      if (submitButton) submitButton.disabled = false;
    }
  });
}

if (reportForm) {
  reportForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(reportForm).entries());
    let record = assessmentCache.find((item) => item.id === data.patient);

    try {
      const payload = await apiRequest(`/api/reports/${data.patient}`);
      record = payload.report;
    } catch (error) {
      record = record || assessmentCache[0];
    }
    renderReportPreview(record);
  });
}

async function boot() {
  setActiveNav();
  initUiEffects();
  const assessments = await loadAssessments();
  renderPatientTable(assessments);
  renderPredictionCards(assessments);
  populateReportOptions(assessments);
  renderReportPreview(assessments[0]);

  if (window.lucide) {
    window.lucide.createIcons();
  }
}

boot();

// Screenshot-matched page interactions
(function initScreenshotInteractions() {
  const navToggle = document.querySelector("[data-nav-toggle]");
  const navMenu = document.querySelector("[data-nav-menu]");
  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      const isOpen = navMenu.classList.toggle("nav-open");
      navToggle.classList.toggle("active", isOpen);
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });
    navMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("nav-open");
        navToggle.classList.remove("active");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  const searchInput = document.querySelector("[data-history-search]");
  const riskFilter = document.querySelector("[data-risk-filter]");
  const historyRows = Array.from(document.querySelectorAll("[data-history-row]"));
  const filterHistory = () => {
    const query = (searchInput?.value || "").trim().toLowerCase();
    const risk = (riskFilter?.value || "all").toLowerCase();
    historyRows.forEach((row) => {
      const nameMatch = (row.dataset.patientName || "").includes(query);
      const rowRisk = (row.dataset.risk || "").toLowerCase();
      const riskMatch = risk === "all" || rowRisk === risk || (risk === "medium" && rowRisk === "moderate");
      row.hidden = !(nameMatch && riskMatch);
    });
  };
  if (searchInput) searchInput.addEventListener("input", filterHistory);
  if (riskFilter) riskFilter.addEventListener("change", filterHistory);

  const modal = document.querySelector("[data-prediction-modal]");
  if (modal && modal.parentElement !== document.body) {
    document.body.appendChild(modal);
  }
  const setText = (selector, value) => {
    const el = document.querySelector(selector);
    if (el) el.textContent = value;
  };
  document.querySelectorAll("[data-open-prediction]").forEach((button) => {
    button.addEventListener("click", () => {
      setText("[data-modal-name]", button.dataset.name || "Patient");
      setText("[data-modal-score]", `${button.dataset.score || 0}%`);
      setText("[data-modal-risk]", button.dataset.risk || "Moderate");
      setText("[data-modal-confidence]", `${button.dataset.confidence || 72}%`);
      if (modal) {
        modal.classList.add("open");
        modal.setAttribute("aria-hidden", "false");
        document.body.style.overflow = "hidden";
        document.body.classList.add("modal-open");
      }
      if (window.lucide) window.lucide.createIcons();
    });
  });
  document.querySelectorAll("[data-close-modal]").forEach((button) => {
    button.addEventListener("click", () => {
      if (modal) {
        modal.classList.remove("open");
        modal.setAttribute("aria-hidden", "true");
      }
      document.body.style.overflow = "";
      document.body.classList.remove("modal-open");
    });
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && modal?.classList.contains("open")) {
      modal.classList.remove("open");
      modal.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      document.body.classList.remove("modal-open");
    }
  });

  const reportSelect = document.querySelector("[data-report-select]");
  const reportEmpty = document.querySelector("[data-report-empty]");
  const reportSheets = Array.from(document.querySelectorAll("[data-selected-report]"));
  const showReport = () => {
    const selected = reportSelect?.value || "";
    let hasReport = false;
    reportSheets.forEach((sheet) => {
      const show = sheet.id === selected;
      sheet.hidden = !show;
      if (show) hasReport = true;
    });
    if (reportEmpty) reportEmpty.hidden = hasReport;
  };
  if (reportSelect) {
    reportSelect.addEventListener("change", showReport);
    showReport();
  }

  document.querySelectorAll("[data-print-report]").forEach((button) => {
    button.addEventListener("click", () => window.print());
  });
})();

// Smooth switch controls for assessment symptom selectors
(function initAssessmentSwitches() {
  document.querySelectorAll("[data-switch-select]").forEach((button) => {
    const wrap = button.closest(".switch-wrap");
    const select = wrap ? wrap.querySelector("select") : null;
    if (!select) return;
    const onValue = button.dataset.onValue || "yes";
    const offValue = button.dataset.offValue || "no";
    const sync = () => {
      const isOn = String(select.value).toLowerCase() === String(onValue).toLowerCase();
      button.classList.toggle("is-on", isOn);
      button.setAttribute("aria-pressed", String(isOn));
      button.setAttribute("title", isOn ? "On" : "Off");
    };
    button.addEventListener("click", () => {
      const isOn = button.classList.contains("is-on");
      select.value = isOn ? offValue : onValue;
      select.dispatchEvent(new Event("change", { bubbles: true }));
      sync();
    });
    select.addEventListener("change", sync);
    sync();
  });
})();

// Tap-to-show report chart percentages
(function initReportChartTooltips() {
  const bars = document.querySelectorAll("[data-chart-tooltip]");
  if (!bars.length) return;
  bars.forEach((bar) => {
    bar.addEventListener("click", (event) => {
      event.stopPropagation();
      bars.forEach((other) => {
        if (other !== bar) other.classList.remove("show-tooltip");
      });
      bar.classList.toggle("show-tooltip");
    });
  });
  document.addEventListener("click", () => {
    bars.forEach((bar) => bar.classList.remove("show-tooltip"));
  });
})();

// Reports page: only show charts after a patient report is selected
(function initSelectedReportCharts() {
  const select = document.querySelector("[data-report-select]");
  const charts = document.querySelector("[data-report-charts]");
  const donut = document.querySelector(".synced-donut");
  const bar = document.querySelector("[data-chart-tooltip]");
  const scoreText = document.querySelector("[data-chart-score]");
  const labelText = document.querySelector("[data-chart-label]");
  const riskBadge = document.querySelector("[data-chart-risk]");
  const tooltipScore = document.querySelector("[data-chart-tooltip-score]");
  if (!select || !charts) return;

  const riskClassList = ["low", "medium", "moderate", "high", "critical", "no", "data"];
  const updateCharts = () => {
    const option = select.options[select.selectedIndex];
    const hasSelection = Boolean(select.value && option);
    charts.hidden = !hasSelection;
    if (!hasSelection) return;

    const score = Number(option.dataset.score || 0);
    const risk = option.dataset.risk || "Risk";
    const riskClass = option.dataset.riskClass || risk.toLowerCase();
    if (donut) donut.style.setProperty("--score", `${score}%`);
    if (bar) bar.style.setProperty("--height", `${score}%`);
    if (scoreText) scoreText.textContent = `${score}%`;
    if (labelText) labelText.textContent = risk;
    if (tooltipScore) tooltipScore.textContent = `avgScore : ${score}%`;
    if (riskBadge) {
      riskBadge.textContent = risk;
      riskBadge.classList.remove(...riskClassList);
      riskBadge.classList.add(riskClass);
    }
  };

  select.addEventListener("change", updateCharts);
  updateCharts();
})();

// Confirm before deleting patient history records
(function initDeleteConfirmation() {
  document.querySelectorAll("[data-confirm-delete]").forEach((form) => {
    form.addEventListener("submit", (event) => {
      const ok = window.confirm("Delete this patient history record? This cannot be undone.");
      if (!ok) event.preventDefault();
    });
  });
})();

// Workflow scroll-in effects
(function initWorkflowEffects() {
  const steps = document.querySelectorAll(".workflow .step");
  if (!steps.length) return;
  if (!("IntersectionObserver" in window)) {
    steps.forEach((step) => step.classList.add("step-visible"));
    return;
  }
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("step-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.18 });
  steps.forEach((step) => observer.observe(step));
})();



// Password visibility toggles for login and account creation
(function initPasswordToggles() {
  document.querySelectorAll("[data-password-toggle]").forEach((button) => {
    const wrapper = button.closest(".password-wrap");
    const input = wrapper?.querySelector("input[type='password'], input[type='text']");
    if (!input) return;
    button.addEventListener("click", () => {
      const isHidden = input.type === "password";
      input.type = isHidden ? "text" : "password";
      button.setAttribute("aria-label", isHidden ? "Hide password" : "Show password");
      button.classList.toggle("is-visible", isHidden);
      button.innerHTML = isHidden ? '<i data-lucide="eye-off"></i>' : '<i data-lucide="eye"></i>';
      if (window.lucide) window.lucide.createIcons();
      input.focus();
    });
  });
})();

// Auto-dismiss floating toast messages
(function initToastMessages() {
  document.querySelectorAll("[data-toast-message]").forEach((toast, index) => {
    window.setTimeout(() => toast.classList.add("toast-visible"), 90 + index * 120);
    window.setTimeout(() => {
      toast.classList.remove("toast-visible");
      toast.classList.add("toast-hiding");
    }, 2800 + index * 260);
    window.setTimeout(() => toast.remove(), 3500 + index * 260);
  });
})();

// Password strength guidance on account creation
(function initPasswordStrength() {
  const input = document.querySelector("[data-password-input]");
  const panel = document.querySelector("[data-password-strength-panel]");
  if (!input || !panel) return;
  const bar = panel.querySelector("[data-password-strength-bar]");
  const text = panel.querySelector("[data-password-strength-text]");
  const rules = {
    length: panel.querySelector('[data-password-rule="length"]'),
    upper: panel.querySelector('[data-password-rule="upper"]'),
    lower: panel.querySelector('[data-password-rule="lower"]'),
    number: panel.querySelector('[data-password-rule="number"]'),
    symbol: panel.querySelector('[data-password-rule="symbol"]'),
  };
  const labels = ["Too weak", "Weak", "Fair", "Strong", "Very strong"];
  const update = () => {
    const value = input.value || "";
    const checks = {
      length: value.length >= 12,
      upper: /[A-Z]/.test(value),
      lower: /[a-z]/.test(value),
      number: /\d/.test(value),
      symbol: /[^A-Za-z0-9]/.test(value),
    };
    const score = Object.values(checks).filter(Boolean).length;
    Object.entries(checks).forEach(([name, passed]) => {
      const rule = rules[name];
      if (!rule) return;
      rule.classList.toggle("rule-met", passed);
      rule.querySelector("i")?.setAttribute("data-lucide", passed ? "check-circle-2" : "circle");
    });
    if (bar) {
      bar.style.width = `${Math.max(score, 1) * 20}%`;
      bar.dataset.score = String(score);
    }
    if (text) {
      text.textContent = value ? labels[Math.max(score - 1, 0)] : "Use at least 12 characters with uppercase, lowercase, a number, and a symbol.";
    }
    if (window.lucide) window.lucide.createIcons();
  };
  input.addEventListener("input", update);
  update();
})();

// Smooth account verification sent popout
(function initVerificationPopout() {
  const popout = document.querySelector("[data-verification-popout]");
  if (!popout) return;
  const close = popout.querySelector("[data-close-verification-popout]");
  const hide = () => {
    popout.classList.add("is-hiding");
    window.setTimeout(() => popout.remove(), 320);
  };
  close?.addEventListener("click", hide);
  window.setTimeout(hide, 4200);
})();
