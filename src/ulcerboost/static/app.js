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
