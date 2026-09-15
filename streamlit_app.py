import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Sagar Khurana | Finance & Business Operations",
    page_icon="assets/profile.jpg",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

def img_to_base64(path):
    return base64.b64encode(Path(path).read_bytes()).decode()

profile_b64 = img_to_base64(ASSETS / "profile.jpg")

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', -apple-system, sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }
    .hero {
        display: flex;
        align-items: center;
        gap: 32px;
        margin-bottom: 8px;
    }
    .hero img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        object-position: center 15%;
        border: 3px solid #1F2A44;
    }
    .hero-name {
        font-size: 34px;
        font-weight: 700;
        color: #1F2A44;
        margin-bottom: 4px;
    }
    .hero-headline {
        font-size: 16px;
        color: #4B5A6A;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 700;
        color: #1F2A44;
        border-bottom: 2px solid #1F2A44;
        padding-bottom: 6px;
        margin-top: 36px;
        margin-bottom: 14px;
    }
    .card {
        background: #F7F8FA;
        border: 1px solid #E3E7EC;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 14px;
    }
    .card-title {
        font-size: 17px;
        font-weight: 700;
        color: #1F2A44;
        margin-bottom: 4px;
    }
    .card-meta {
        font-size: 13px;
        color: #6B7686;
        margin-bottom: 8px;
    }
    .compact-card {
        background: #F7F8FA;
        border: 1px solid #E3E7EC;
        border-radius: 8px;
        padding: 12px 16px;
        margin-bottom: 10px;
    }
    .compact-title {
        font-size: 15px;
        font-weight: 700;
        color: #1F2A44;
    }
    .compact-meta {
        font-size: 12px;
        color: #6B7686;
        margin-bottom: 4px;
    }
    .skill-badge {
        display: inline-block;
        background: #E9EEF5;
        color: #1F2A44;
        padding: 4px 12px;
        border-radius: 14px;
        font-size: 13px;
        margin: 3px 4px 3px 0;
    }
    .skill-group-label {
        font-size: 13px;
        font-weight: 700;
        color: #4B5A6A;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-top: 10px;
        margin-bottom: 4px;
    }
    a.link-pill {
        display: inline-block;
        background: #1F2A44;
        color: #ffffff !important;
        text-decoration: none;
        padding: 8px 18px;
        border-radius: 20px;
        font-size: 14px;
        margin: 4px 6px 4px 0;
    }
    a.link-pill:hover { background: #35496B; }
    .contact-line {
        font-size: 14px;
        color: #4B5A6A;
        margin-bottom: 6px;
    }
    .subsection-label {
        font-size: 14px;
        font-weight: 700;
        color: #4B5A6A;
        margin-top: 20px;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- hero ----------
st.markdown(
    f"""
    <div class="hero">
        <img src="data:image/jpeg;base64,{profile_b64}">
        <div>
            <div class="hero-name">Sagar Khurana</div>
            <div class="hero-headline">Finance & Business Operations | Process Optimization | Data-Driven Insights</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    I'm a finance-focused management professional pursuing a PGDM at Fortune Institute of
    International Business, with 2.5 years of experience in financial business operations at
    Sun Life Financial. My background spans retirement plan operations, insurance processing,
    and MIS reporting, with a consistent focus on process optimization, data accuracy, and
    resolving operational discrepancies at scale. I'm skilled at translating high-volume,
    detail-heavy processes into reliable, well-documented workflows, and I'm now looking to
    bring that operational rigor into broader financial planning and business roles.
    """
)

col1, col2, col3 = st.columns(3)
col1.markdown('<a class="link-pill" href="https://www.linkedin.com/in/sagarkhurana22/" target="_blank">LinkedIn</a>', unsafe_allow_html=True)
col2.markdown('<a class="link-pill" href="https://github.com/SagarKhurana22" target="_blank">GitHub</a>', unsafe_allow_html=True)
col3.markdown('<span class="contact-line">📧 Sagarkhurana112@gmail.com &nbsp; | &nbsp; 📞 +91 7206166690</span>', unsafe_allow_html=True)

# ---------- education ----------
st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <div class="card-title">Post Graduate Diploma in Management (PGDM)</div>
        <div class="card-meta">Fortune Institute of International Business (FIIB) &nbsp;|&nbsp; 2025 – 2027</div>
    </div>
    <div class="card">
        <div class="card-title">Bachelor of Business Administration (BBA)</div>
        <div class="card-meta">Guru Gobind Singh Indraprastha University &nbsp;|&nbsp; 2018 – 2021</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- skills ----------
st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)

def badges(items):
    return "".join(f'<span class="skill-badge">{i}</span>' for i in items)

st.markdown('<div class="skill-group-label">Operations & Analytical</div>', unsafe_allow_html=True)
st.markdown(badges(["Operations Management", "Problem Solving"]), unsafe_allow_html=True)

st.markdown('<div class="skill-group-label">Professional Skills</div>', unsafe_allow_html=True)
st.markdown(badges(["Communication", "Team Leadership"]), unsafe_allow_html=True)

st.markdown('<div class="skill-group-label">Tools</div>', unsafe_allow_html=True)
st.markdown(badges(["MS Excel"]), unsafe_allow_html=True)

# ---------- experience ----------
st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="card">
        <div class="card-title">Finance Intern</div>
        <div class="card-meta">Aditya Birla Capital, Delhi &nbsp;|&nbsp; April 2026 – Aug 2026</div>
        <ul>
            <li>Managed 1,000+ insurance application registrations, coordinating documentation, data
            verification, and end-to-end processing to support timely policy issuance.</li>
            <li>Facilitated 350+ insurance sales closures, managing the process from application to
            final issuance while ensuring accurate documentation and process compliance.</li>
            <li>Prepared and maintained financial records and Excel-based MIS, while developing
            practical knowledge of financial markets, derivatives, and trading.</li>
        </ul>
    </div>

    <div class="card">
        <div class="card-title">Process Associate (promoted from Junior Process Associate)</div>
        <div class="card-meta">Sun Life Financial – Group Retirement Services, Gurgaon &nbsp;|&nbsp; 2022 – 2024 &middot; 2 years</div>
        <ul>
            <li>Managed end-to-end retirement plan operations, processing 1,000+ client
            transactions/records involving policy updates, data processing, contributions, and
            fund changes with high accuracy.</li>
            <li>Performed detailed data verification and reconciliation, identifying and resolving
            300+ operational discrepancies while maintaining quality standards and improving
            turnaround time.</li>
            <li>Collaborated with Quality, Compliance, and Client Services teams to ensure SLA
            adherence and timely resolution across high-volume workflows.</li>
        </ul>
    </div>

    <div class="card">
        <div class="card-title">Social Intern</div>
        <div class="card-meta">Udayan Care Foundation, Delhi &nbsp;|&nbsp; Jan 2026</div>
        <ul>
            <li>Engaged with 35+ students aged 6–15 through educational and mentoring activities.</li>
            <li>Conducted academic support and interactive learning sessions, helping students
            strengthen foundational knowledge and communication skills.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="subsection-label">Earlier Experience</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="compact-card">
        <div class="compact-title">Operation Trainee</div>
        <div class="compact-meta">Aston Carter &nbsp;|&nbsp; Jan 2022 – Aug 2022</div>
        Supported daily operational tasks including data processing and documentation; performed
        quality checks and coordinated workflows to improve process efficiency.
    </div>
    <div class="compact-card">
        <div class="compact-title">Wealth Management & Travel Tourism Intern</div>
        <div class="compact-meta">UAS International, Delhi &nbsp;|&nbsp; Jun 2020 – Jul 2020</div>
        Completed internship achieving an 80% performance score; conducted financial and market
        research to support wealth management project deliverables.
    </div>
    <div class="compact-card">
        <div class="compact-title">Teaching & Social Impact Intern</div>
        <div class="compact-meta">SK Children Foundation &nbsp;|&nbsp; Apr 2020 – Sep 2020</div>
        Taught academic subjects and values to underprivileged students as part of a community
        education initiative; recognized for discipline and commitment to social welfare programs.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- contact ----------
st.markdown('<div class="section-title">Contact</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact-line">Email: Sagarkhurana112@gmail.com</div>
    <div class="contact-line">Phone: +91 7206166690</div>
    """,
    unsafe_allow_html=True,
)
col1, col2 = st.columns(2)
col1.markdown('<a class="link-pill" href="https://www.linkedin.com/in/sagarkhurana22/" target="_blank">Connect on LinkedIn</a>', unsafe_allow_html=True)
col2.markdown('<a class="link-pill" href="https://github.com/SagarKhurana22" target="_blank">View GitHub</a>', unsafe_allow_html=True)
