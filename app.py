import streamlit as st
import json
import calendar
from datetime import date, datetime, timedelta

# ── Page config ────────────────────────────────────────────────────
st.set_page_config(
    page_title="Bolles MS Planner · Semester 2",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Data ───────────────────────────────────────────────────────────
EVENTS = [
    {"date": "2026-01-01", "name": "New Year's Day — Winter Break",                        "type": "holiday"},
    {"date": "2026-01-02", "name": "Winter Break",                                          "type": "break"},
    {"date": "2026-01-05", "name": "Professional Development Day — No Classes",             "type": "holiday"},
    {"date": "2026-01-06", "name": "Classes Resume after Winter Break",                     "type": "academic"},
    {"date": "2026-01-19", "name": "Martin Luther King Jr. Holiday — No School",            "type": "holiday"},
    {"date": "2026-02-04", "name": "Quarter 3 End of Interim",                              "type": "academic"},
    {"date": "2026-02-13", "name": "Parent Conference Day — No Classes / End Trimester 2",  "type": "academic"},
    {"date": "2026-02-16", "name": "Presidents' Day — School Closed",                       "type": "holiday"},
    {"date": "2026-03-02", "name": "ERB Testing Demo Day",                                  "type": "testing"},
    {"date": "2026-03-09", "name": "Spring Break Begins",                                   "type": "break"},
    {"date": "2026-03-10", "name": "Spring Break",                                          "type": "break"},
    {"date": "2026-03-11", "name": "Spring Break",                                          "type": "break"},
    {"date": "2026-03-12", "name": "Spring Break",                                          "type": "break"},
    {"date": "2026-03-13", "name": "Spring Break",                                          "type": "break"},
    {"date": "2026-03-16", "name": "Faculty Work Day — No Classes",                         "type": "holiday"},
    {"date": "2026-03-17", "name": "Quarter 3 Ends / Classes Resume",                       "type": "academic"},
    {"date": "2026-03-17", "name": "ERB Testing — Quantitative Reasoning",                  "type": "testing"},
    {"date": "2026-03-18", "name": "ERB Testing — Reading Comprehension / Written Concepts","type": "testing"},
    {"date": "2026-03-19", "name": "ERB Testing — Math 1 / Written Mechanics / Verbal Reasoning", "type": "testing"},
    {"date": "2026-03-20", "name": "Eid al-Fitr — No Quizzes or Tests",                    "type": "event"},
    {"date": "2026-03-23", "name": "ERB Testing — Math 2 / Vocabulary",                    "type": "testing"},
    {"date": "2026-04-03", "name": "Good Friday / Spring Holiday — School Closed",          "type": "holiday"},
    {"date": "2026-04-05", "name": "Easter",                                                "type": "event"},
    {"date": "2026-04-06", "name": "Spring Holiday — School Closed",                        "type": "holiday"},
    {"date": "2026-04-17", "name": "Quarter 4 End of Interim",                              "type": "academic"},
    {"date": "2026-04-27", "name": "Grade 8 Class Trip Begins",                             "type": "event"},
    {"date": "2026-04-28", "name": "Grade 8 Class Trip",                                    "type": "event"},
    {"date": "2026-04-29", "name": "Grade 8 Class Trip",                                    "type": "event"},
    {"date": "2026-05-01", "name": "Grade 8 Class Trip Ends",                               "type": "event"},
    {"date": "2026-05-04", "name": "Middle School Madness Week Begins",                     "type": "event"},
    {"date": "2026-05-15", "name": "Last Day of Classes / Quarter 4 Ends",                  "type": "academic"},
    {"date": "2026-05-18", "name": "Reading Day — No Classes",                              "type": "academic"},
    {"date": "2026-05-19", "name": "MS/US Exam Week",                                       "type": "exam"},
    {"date": "2026-05-20", "name": "MS/US Exams",                                           "type": "exam"},
    {"date": "2026-05-21", "name": "MS/US Exams / Grade 8 Recognition Day",                 "type": "exam"},
    {"date": "2026-05-22", "name": "MS/US Exams",                                           "type": "exam"},
    {"date": "2026-05-23", "name": "Commencement — Class of 2026",                          "type": "event"},
    {"date": "2026-05-25", "name": "Memorial Day — School Closed",                          "type": "holiday"},
    {"date": "2026-05-26", "name": "Make-up Exams",                                         "type": "exam"},
]

ROTATIONS = {
    "2026-01-06":"B","2026-01-07":"C","2026-01-08":"D","2026-01-09":"E",
    "2026-01-12":"F","2026-01-13":"G","2026-01-14":"A","2026-01-15":"B","2026-01-16":"C",
    "2026-01-20":"D","2026-01-21":"E","2026-01-22":"F","2026-01-23":"G",
    "2026-01-26":"A","2026-01-27":"B","2026-01-28":"C","2026-01-29":"D","2026-01-30":"E",
    "2026-02-02":"F","2026-02-03":"G","2026-02-04":"A","2026-02-05":"B","2026-02-06":"C",
    "2026-02-09":"D","2026-02-10":"E","2026-02-11":"F","2026-02-12":"G",
    "2026-02-17":"A","2026-02-18":"B","2026-02-19":"C","2026-02-20":"D",
    "2026-02-23":"E","2026-02-24":"F","2026-02-25":"G","2026-02-26":"A","2026-02-27":"B",
    "2026-03-02":"C","2026-03-03":"D","2026-03-04":"E","2026-03-05":"F","2026-03-06":"G",
    "2026-03-17":"A","2026-03-18":"B","2026-03-19":"C","2026-03-20":"D",
    "2026-03-23":"E","2026-03-24":"F","2026-03-25":"G","2026-03-26":"A","2026-03-27":"B",
    "2026-03-30":"C","2026-03-31":"D","2026-04-01":"E","2026-04-02":"F",
    "2026-04-07":"G","2026-04-08":"A","2026-04-09":"B","2026-04-10":"C",
    "2026-04-13":"D","2026-04-14":"E","2026-04-15":"F","2026-04-16":"G","2026-04-17":"A",
    "2026-04-20":"B","2026-04-21":"C","2026-04-22":"D","2026-04-23":"E","2026-04-24":"F",
    "2026-04-27":"G","2026-04-28":"A","2026-04-29":"B","2026-04-30":"C",
    "2026-05-01":"D","2026-05-04":"E","2026-05-05":"F","2026-05-06":"G","2026-05-07":"A","2026-05-08":"B",
    "2026-05-11":"C","2026-05-12":"D","2026-05-13":"E","2026-05-14":"F","2026-05-15":"G",
}

NO_SCHOOL = {
    "2026-01-01","2026-01-02","2026-01-05","2026-01-19",
    "2026-02-13","2026-02-16",
    "2026-03-09","2026-03-10","2026-03-11","2026-03-12","2026-03-13","2026-03-16",
    "2026-04-03","2026-04-06",
    "2026-05-18","2026-05-25",
}

SUBJECTS = ["Math","Spanish","English","PE","Speech & Debate","Science","History"]

TYPE_COLORS = {
    "holiday": ("#fde8e8", "#9b2a2a"),
    "break":   ("#d4f7e8", "#1a6b4a"),
    "academic":("#dce8ff", "#1a3a7a"),
    "exam":    ("#ffe0f0", "#7a1a50"),
    "testing": ("#e8e0ff", "#3a1a7a"),
    "event":   ("#e0f4ff", "#0a4a7a"),
}
TYPE_LABELS = {
    "holiday":"NO SCHOOL","break":"BREAK","academic":"ACADEMIC",
    "exam":"EXAM","testing":"TESTING","event":"EVENT",
}
TYPE_DOT_COLORS = {
    "holiday":"#e74c3c","break":"#27ae60","academic":"#2980b9",
    "exam":"#8e44ad","testing":"#6c3483","event":"#16a085",
}

MONTH_NAMES = ["January","February","March","April","May","June",
               "July","August","September","October","November","December"]

# ── Helpers ────────────────────────────────────────────────────────
def date_key(d: date) -> str:
    return d.strftime("%Y-%m-%d")

def events_for(key: str):
    return [e for e in EVENTS if e["date"] == key]

def get_rotation(key: str):
    return ROTATIONS.get(key)

def is_no_school(key: str) -> bool:
    return key in NO_SCHOOL

def get_schedule(key: str):
    """Returns list of schedule slots for a school day."""
    d = datetime.strptime(key, "%Y-%m-%d").date()
    dow = d.weekday()  # 0=Mon … 6=Sun
    rot = get_rotation(key)
    if is_no_school(key) or not rot or dow >= 5:
        return None

    is_wed = (dow == 2)
    if is_wed:
        return [
            {"time":"8:00–8:30",   "label":"Zero Hour",             "is_period":False},
            {"time":"8:30–9:25",   "label":"Math",                  "is_period":True,  "subject":"Math"},
            {"time":"9:25–10:25",  "label":"Advisory + Activities", "is_period":False},
            {"time":"10:25–11:10", "label":"Spanish",               "is_period":True,  "subject":"Spanish"},
            {"time":"11:10–12:05", "label":"English",               "is_period":True,  "subject":"English"},
            {"time":"12:05–12:25", "label":"Grade 8 Lunch",         "is_period":False},
            {"time":"12:25–12:40", "label":"Grade 6 Lunch",         "is_period":False},
            {"time":"12:40–1:00",  "label":"Grade 7 Lunch ★",       "is_period":False},
            {"time":"1:05–2:00",   "label":"PE",                    "is_period":True,  "subject":"PE"},
            {"time":"2:05–3:00",   "label":"Speech & Debate",       "is_period":True,  "subject":"Speech & Debate"},
        ]

    rot_idx = "ABCDEFG".index(rot)
    def subj(offset):
        return SUBJECTS[(rot_idx + offset) % 7]

    mid = "Convocation" if (dow == 0 and rot in "ACEG") else "Activities"
    return [
        {"time":"8:00–8:30",   "label":"Zero Hour (Optional)", "is_period":False},
        {"time":"8:30–8:40",   "label":"Advisory",             "is_period":False},
        {"time":"8:45–9:40",   "label":subj(0),                "is_period":True,  "subject":subj(0)},
        {"time":"9:45–10:40",  "label":subj(1),                "is_period":True,  "subject":subj(1)},
        {"time":"10:40–11:10", "label":mid,                    "is_period":False},
        {"time":"11:10–12:05", "label":subj(2),                "is_period":True,  "subject":subj(2)},
        {"time":"12:05–12:25", "label":"Grade 8 Lunch",        "is_period":False},
        {"time":"12:25–12:40", "label":"Grade 6 Lunch",        "is_period":False},
        {"time":"12:40–1:00",  "label":"Grade 7 Lunch ★",      "is_period":False},
        {"time":"1:05–2:00",   "label":subj(3),                "is_period":True,  "subject":subj(3)},
        {"time":"2:05–3:00",   "label":subj(4),                "is_period":True,  "subject":subj(4)},
        {"time":"3:00+",       "label":"After School",         "is_period":False},
    ]

# ── Homework storage (session_state) ──────────────────────────────
# st.session_state.hw = { "2026-01-06": { "Math": "read ch 3", ... }, ... }
if "hw" not in st.session_state:
    st.session_state.hw = {}

def get_hw(key: str, subject: str) -> str:
    return st.session_state.hw.get(key, {}).get(subject, "")

def set_hw(key: str, subject: str, text: str):
    if key not in st.session_state.hw:
        st.session_state.hw[key] = {}
    if text.strip():
        st.session_state.hw[key][subject] = text.strip()
    else:
        st.session_state.hw[key].pop(subject, None)

def day_has_hw(key: str) -> bool:
    return bool(st.session_state.hw.get(key))

# ── Session state for navigation ───────────────────────────────────
today = date.today()
if "selected_date" not in st.session_state:
    if date(2026, 1, 1) <= today <= date(2026, 5, 31):
        st.session_state.selected_date = today
    else:
        st.session_state.selected_date = date(2026, 1, 6)

if "view_month" not in st.session_state:
    d = st.session_state.selected_date
    st.session_state.view_month = (d.year, d.month)

if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Calendar"

if "editing_subject" not in st.session_state:
    st.session_state.editing_subject = None   # (date_key, subject_label)

# ── CSS ────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600&display=swap');

/* Global */
html, body, [data-testid="stAppViewContainer"] {
    background: #f5f0e8 !important;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stSidebar"] {
    background: #0a1f44 !important;
}
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebar"] .stMarkdown h3 {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #c9952a !important;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 0.4rem;
    margin-bottom: 0.5rem;
}
/* Header bar */
.bolles-header {
    background: #0a1f44;
    padding: 0.9rem 1.5rem;
    border-radius: 12px;
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.bolles-logo-icon {
    width:40px;height:40px;background:#c9952a;border-radius:6px;
    display:flex;align-items:center;justify-content:center;
    font-family:'Playfair Display',serif;font-weight:900;font-size:1.2rem;color:#0a1f44;
}
.bolles-logo-text { font-family:'Playfair Display',serif;font-size:1.1rem;font-weight:700;color:white; }
.bolles-logo-sub  { font-family:'DM Mono',monospace;font-size:0.6rem;letter-spacing:0.1em;
                    text-transform:uppercase;color:#e8b84b; }

/* Calendar grid */
.cal-grid { display:grid;grid-template-columns:repeat(7,1fr);gap:2px; }
.cal-day-header {
    text-align:center;padding:0.5rem;background:#0a1f44;
    font-family:'DM Mono',monospace;font-size:0.65rem;letter-spacing:0.1em;
    text-transform:uppercase;color:rgba(255,255,255,0.6);
}
.cal-day-header.weekend { color:rgba(255,255,255,0.35); }
.cal-day {
    min-height:80px;padding:0.35rem;background:white;
    border:1px solid rgba(10,31,68,0.1);cursor:pointer;transition:background 0.1s;
    font-family:'DM Mono',monospace;
}
.cal-day:hover { background:#f5f0e8; }
.cal-day.other  { background:rgba(0,0,0,0.02); }
.cal-day.today  { background:#eef2ff; }
.cal-day.selected { background:#fff8ec; outline:2px solid #c9952a; }
.cal-day.no-school { background:#fff5f5; }
.cal-day.break  { background:#f0faf5; }
.day-num {
    font-size:0.78rem;font-weight:600;color:#3a4f6e;
    width:22px;height:22px;border-radius:5px;display:inline-flex;
    align-items:center;justify-content:center;margin-bottom:3px;
}
.day-num.today-num { background:#0a1f44;color:white; }
.day-num.other-num { opacity:0.35; }
.chip {
    font-size:0.58rem;padding:1px 5px;border-radius:4px;
    display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
    font-weight:500;margin-bottom:2px;font-family:'DM Sans',sans-serif;
}
.rot-label { font-size:0.55rem;color:#6b7f99;margin-top:2px; }
.hw-dot { display:inline-block;width:6px;height:6px;border-radius:50%;background:#c9952a;
          margin-left:3px;vertical-align:middle; }

/* Day detail */
.detail-header {
    background:linear-gradient(135deg,#0a1f44,#12306b);
    border-radius:12px 12px 0 0;padding:1.2rem 1.5rem;
    display:flex;align-items:center;justify-content:space-between;
}
.detail-day-name { font-family:'DM Mono',monospace;font-size:0.7rem;
                   letter-spacing:0.1em;text-transform:uppercase;color:rgba(255,255,255,0.6); }
.detail-date-big { font-family:'Playfair Display',serif;font-size:1.8rem;
                   font-weight:900;color:white;line-height:1; }
.rot-badge { background:#c9952a;color:#0a1f44;font-family:'DM Mono',monospace;
             font-size:0.75rem;font-weight:700;padding:0.35rem 0.75rem;
             border-radius:8px;letter-spacing:0.06em; }

/* Schedule rows */
.sched-table { width:100%;border-collapse:collapse; }
.sched-table td { padding:0.3rem 0.5rem;vertical-align:top; }
.sched-time-td { font-family:'DM Mono',monospace;font-size:0.68rem;
                 color:#6b7f99;white-space:nowrap;width:90px; }
.sched-cell {
    font-size:0.82rem;padding:0.28rem 0.6rem;border-radius:6px;
    font-family:'DM Sans',sans-serif;
}
.cell-period   { background:#f5f0e8;color:#0d1b35;font-weight:500; }
.cell-advisory { background:#dce8ff;color:#1a3a7a; }
.cell-lunch    { background:#d4f7e8;color:#1a5a3a; }
.cell-activity { background:#fef3d0;color:#7a5200; }
.cell-period.clickable { cursor:pointer;transition:background 0.15s; }
.cell-period.clickable:hover { background:#dbeafe;outline:1.5px solid #93c5fd; }
.hw-preview {
    font-size:0.72rem;font-style:italic;color:#3a4f6e;
    border-left:2px solid #c9952a;padding-left:6px;margin-top:4px;line-height:1.4;
}
.hw-hint { font-size:0.65rem;color:#6b7f99;float:right;font-family:'DM Mono',monospace; }

/* Event chips in detail */
.detail-events { margin-bottom:0.75rem; }
.no-class-msg { text-align:center;padding:2rem;color:#6b7f99;
                font-family:'DM Mono',monospace;font-size:0.85rem; }
.closed-msg { text-align:center;padding:1.2rem;background:#fff5f5;border-radius:10px;
              color:#c0392b;font-weight:600;font-size:0.9rem; }

/* All events list */
.ev-month-title {
    font-family:'Playfair Display',serif;font-size:1.3rem;font-weight:700;color:#0a1f44;
    border-bottom:2px solid #0a1f44;padding-bottom:0.3rem;margin:1rem 0 0.5rem;
}
.ev-row { display:flex;align-items:center;gap:0.75rem;padding:0.5rem 0.6rem;
          border-radius:8px;margin-bottom:2px; }
.ev-row-date { font-family:'DM Mono',monospace;font-size:0.7rem;color:#6b7f99;
               min-width:90px; }
.ev-row-name { font-size:0.85rem;font-weight:500;flex:1; }
.ev-badge { font-size:0.6rem;padding:2px 8px;border-radius:20px;
            font-family:'DM Mono',monospace;white-space:nowrap; }

/* Upcoming events sidebar */
.up-item { display:flex;gap:0.5rem;padding:0.4rem 0;
           border-bottom:1px solid rgba(255,255,255,0.1);align-items:flex-start; }
.up-item:last-child { border-bottom:none; }
.up-dot { width:8px;height:8px;border-radius:50%;flex-shrink:0;margin-top:4px; }
.up-date { font-family:'DM Mono',monospace;font-size:0.58rem;
           letter-spacing:0.05em;text-transform:uppercase;opacity:0.6; }
.up-name { font-size:0.78rem;font-weight:500;line-height:1.3; }

/* Legend */
.leg-item { display:flex;align-items:center;gap:0.5rem;
            padding:0.25rem 0;font-size:0.78rem;opacity:0.85; }
.leg-dot { width:10px;height:10px;border-radius:3px;flex-shrink:0; }

/* Streamlit button overrides */
div[data-testid="stHorizontalBlock"] .stButton button {
    border-radius: 20px !important;
    font-family: 'DM Sans', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────
st.markdown("""
<div class="bolles-header">
  <div class="bolles-logo-icon">B</div>
  <div>
    <div class="bolles-logo-text">Bolles School</div>
    <div class="bolles-logo-sub">Middle School Planner · Semester 2 · 2025–26</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ───────────────────────────────────────────────────────────
tab_cal, tab_all, tab_hw = st.tabs(["📅 Calendar", "📋 All Events", "📚 Homework"])

# ══════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 📅 Jump to Date")
    jump = st.date_input(
        "Select date",
        value=st.session_state.selected_date,
        min_value=date(2026, 1, 1),
        max_value=date(2026, 5, 31),
        label_visibility="collapsed",
    )
    if jump != st.session_state.selected_date:
        st.session_state.selected_date = jump
        st.session_state.view_month = (jump.year, jump.month)
        st.rerun()

    st.markdown("---")
    st.markdown("### 🔔 Upcoming Events")
    now = date.today()
    upcoming = sorted(
        [e for e in EVENTS if datetime.strptime(e["date"], "%Y-%m-%d").date() >= now],
        key=lambda e: e["date"]
    )[:6]

    up_html = ""
    for ev in upcoming:
        d = datetime.strptime(ev["date"], "%Y-%m-%d").date()
        color = TYPE_DOT_COLORS.get(ev["type"], "#888")
        mo = d.strftime("%b").upper()
        up_html += f"""
        <div class="up-item">
          <div class="up-dot" style="background:{color}"></div>
          <div>
            <div class="up-date">{mo} {d.day}</div>
            <div class="up-name">{ev['name']}</div>
          </div>
        </div>"""
    st.markdown(up_html, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎨 Legend")
    leg_html = ""
    for typ, (bg, fg) in TYPE_COLORS.items():
        label = TYPE_LABELS[typ]
        leg_html += f'<div class="leg-item"><div class="leg-dot" style="background:{bg};border:1px solid {fg}33"></div> {label}</div>'
    st.markdown(leg_html, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# CALENDAR TAB
# ══════════════════════════════════════════════════════════════════
with tab_cal:
    yr, mo = st.session_state.view_month

    # Month navigation
    col_prev, col_title, col_next, col_today = st.columns([1, 4, 1, 1.2])
    with col_prev:
        if st.button("‹", key="prev_month", use_container_width=True):
            mo -= 1
            if mo < 1: mo = 12; yr -= 1
            st.session_state.view_month = (yr, mo)
            st.rerun()
    with col_title:
        st.markdown(f"""
        <div style="text-align:center">
          <div style="font-family:'Playfair Display',serif;font-size:2rem;font-weight:900;color:#0a1f44;line-height:1">{MONTH_NAMES[mo-1]}</div>
          <div style="font-family:'DM Mono',monospace;font-size:0.75rem;color:#6b7f99;letter-spacing:0.1em">{yr} · SEMESTER 2</div>
        </div>""", unsafe_allow_html=True)
    with col_next:
        if st.button("›", key="next_month", use_container_width=True):
            mo += 1
            if mo > 12: mo = 1; yr += 1
            st.session_state.view_month = (yr, mo)
            st.rerun()
    with col_today:
        if st.button("Today", key="go_today", use_container_width=True):
            t = date.today()
            if date(2026,1,1) <= t <= date(2026,5,31):
                st.session_state.selected_date = t
                st.session_state.view_month = (t.year, t.month)
            else:
                st.session_state.view_month = (2026, 1)
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Build calendar HTML
    cal = calendar.Calendar(firstweekday=0)  # Monday first
    month_days = cal.monthdatescalendar(yr, mo)

    day_headers = "".join(
        f'<div class="cal-day-header{"  weekend" if i>=4 else ""}">{d}</div>'
        for i, d in enumerate(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    )

    cells_html = ""
    for week in month_days:
        for d in week:
            key = date_key(d)
            is_other   = d.month != mo
            is_today   = d == today
            is_sel     = d == st.session_state.selected_date
            no_school  = key in NO_SCHOOL
            is_break   = any(e["date"]==key and e["type"]=="break" for e in EVENTS)
            has_hw     = day_has_hw(key)
            is_weekend = d.weekday() >= 5

            cls = "cal-day"
            if is_other:   cls += " other"
            if is_today:   cls += " today"
            if is_sel:     cls += " selected"
            if no_school:  cls += " no-school"
            elif is_break: cls += " break"

            num_cls = "day-num"
            if is_today:   num_cls += " today-num"
            if is_other:   num_cls += " other-num"

            hw_dot = '<span class="hw-dot"></span>' if (has_hw and not is_other) else ""

            # Event chips
            chips = ""
            evs = events_for(key)
            for ev in evs[:2]:
                bg, fg = TYPE_COLORS.get(ev["type"], ("#eee","#333"))
                name = ev["name"][:22] + "…" if len(ev["name"]) > 22 else ev["name"]
                chips += f'<span class="chip" style="background:{bg};color:{fg}">{name}</span>'
            if len(evs) > 2:
                chips += f'<span class="chip" style="color:#6b7f99">+{len(evs)-2} more</span>'

            # Rotation label
            rot_html = ""
            if not is_other:
                rot = get_rotation(key)
                if rot:
                    is_late = d.weekday() == 2
                    rot_html = f'<div class="rot-label">Rot. {rot}{"  · Late Start" if is_late else ""}</div>'

            cells_html += f"""
            <div class="{cls}" onclick="void(0)" data-date="{key}">
              <div class="{num_cls}">{d.day}{hw_dot}</div>
              {chips}{rot_html}
            </div>"""

    # Render calendar (read-only display; clicks handled via buttons below)
    st.markdown(
        f'<div class="cal-grid">{day_headers}{cells_html}</div>',
        unsafe_allow_html=True
    )

    # Date picker row for clicking days (more reliable than JS in Streamlit)
    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("👆 Pick a date below to view its schedule and add homework:")
    picked = st.date_input(
        "View day",
        value=st.session_state.selected_date,
        min_value=date(2026,1,1),
        max_value=date(2026,5,31),
        label_visibility="collapsed",
        key="cal_day_picker",
    )
    if picked != st.session_state.selected_date:
        st.session_state.selected_date = picked
        st.session_state.view_month = (picked.year, picked.month)
        st.session_state.editing_subject = None
        st.rerun()

    # ── Day Detail Panel ──────────────────────────────────────────
    sel = st.session_state.selected_date
    sel_key = date_key(sel)
    rot = get_rotation(sel_key)
    evs = events_for(sel_key)
    no_school = is_no_school(sel_key)
    is_weekend = sel.weekday() >= 5

    day_name = sel.strftime("%A").upper()
    date_str = sel.strftime("%B %-d, %Y")

    rot_badge = ""
    if rot:
        is_late = sel.weekday() == 2
        rot_badge = f'<span class="rot-badge">Rotation {rot}{"  · Late Start" if is_late else ""}</span>'

    st.markdown(f"""
    <div class="detail-header" style="margin-top:1.5rem">
      <div>
        <div class="detail-day-name">{day_name}</div>
        <div class="detail-date-big">{date_str}</div>
      </div>
      {rot_badge}
    </div>
    <div style="background:white;border-radius:0 0 12px 12px;padding:1.2rem 1.5rem;
                border:1px solid rgba(10,31,68,0.1);border-top:none;">
    """, unsafe_allow_html=True)

    # Events bar
    if evs:
        ev_chips = ""
        for ev in evs:
            bg, fg = TYPE_COLORS.get(ev["type"], ("#eee","#333"))
            ev_chips += f'<span class="chip" style="background:{bg};color:{fg};font-size:0.75rem;padding:3px 8px">{ev["name"]}</span> '
        st.markdown(f'<div class="detail-events">{ev_chips}</div>', unsafe_allow_html=True)

    if is_weekend:
        st.markdown('<div class="no-class-msg">🌅 Weekend</div>', unsafe_allow_html=True)
    elif no_school or not rot:
        reason = evs[0]["name"] if evs else "No School"
        st.markdown(f'<div class="closed-msg">🚫 {reason}</div>', unsafe_allow_html=True)
    else:
        sched = get_schedule(sel_key)
        if sched:
            st.caption("💡 Click **+ add HW** on any subject to log homework")
            for slot in sched:
                t_col, s_col = st.columns([1, 5])
                with t_col:
                    st.markdown(
                        f'<div class="sched-time-td" style="padding-top:6px">{slot["time"]}</div>',
                        unsafe_allow_html=True
                    )
                with s_col:
                    if slot["is_period"]:
                        subject = slot["subject"]
                        hw_text = get_hw(sel_key, subject)
                        hw_preview = f'<div class="hw-preview">{hw_text}</div>' if hw_text else ""
                        hint = "✏️ edit" if hw_text else "+ add HW"

                        st.markdown(
                            f'<div class="sched-cell cell-period">'
                            f'  {slot["label"]}'
                            f'  <span class="hw-hint">{hint}</span>'
                            f'  {hw_preview}'
                            f'</div>',
                            unsafe_allow_html=True
                        )
                        if st.button(f"{'Edit' if hw_text else 'Add'} HW — {subject}",
                                     key=f"hwbtn_{sel_key}_{subject}",
                                     use_container_width=True):
                            st.session_state.editing_subject = (sel_key, subject)
                            st.rerun()
                    else:
                        # Non-period slot styling
                        if "Lunch" in slot["label"]:
                            cell_cls = "cell-lunch"
                        elif "Advisory" in slot["label"] or "Convocation" in slot["label"] or "Activities" in slot["label"] or "After" in slot["label"]:
                            cell_cls = "cell-activity"
                        else:
                            cell_cls = "cell-advisory"
                        st.markdown(
                            f'<div class="sched-cell {cell_cls}">{slot["label"]}</div>',
                            unsafe_allow_html=True
                        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ── Homework edit form ─────────────────────────────────────────
    if st.session_state.editing_subject:
        edit_key, edit_subj = st.session_state.editing_subject
        edit_date = datetime.strptime(edit_key, "%Y-%m-%d").date()
        current_hw = get_hw(edit_key, edit_subj)

        with st.form(key="hw_form", clear_on_submit=True):
            st.markdown(f"""
            <div style="background:#0a1f44;border-radius:10px 10px 0 0;padding:0.9rem 1.2rem;margin-bottom:0">
              <div style="font-family:'DM Mono',monospace;font-size:0.6rem;color:rgba(255,255,255,0.5);
                          letter-spacing:0.1em;text-transform:uppercase">
                {edit_date.strftime("%B %-d, %Y")}
              </div>
              <div style="font-family:'Playfair Display',serif;font-size:1.2rem;font-weight:700;color:white">
                📚 {edit_subj}
              </div>
            </div>
            """, unsafe_allow_html=True)

            new_hw = st.text_area(
                "Homework / Notes",
                value=current_hw,
                height=120,
                placeholder="Write your homework, due dates, notes…",
                label_visibility="collapsed",
            )
            c1, c2, c3 = st.columns([2, 2, 3])
            with c1:
                save = st.form_submit_button("💾 Save", use_container_width=True, type="primary")
            with c2:
                clear = st.form_submit_button("🗑️ Clear", use_container_width=True)
            with c3:
                cancel = st.form_submit_button("Cancel", use_container_width=True)

            if save:
                set_hw(edit_key, edit_subj, new_hw)
                st.session_state.editing_subject = None
                st.rerun()
            if clear:
                set_hw(edit_key, edit_subj, "")
                st.session_state.editing_subject = None
                st.rerun()
            if cancel:
                st.session_state.editing_subject = None
                st.rerun()

# ══════════════════════════════════════════════════════════════════
# ALL EVENTS TAB
# ══════════════════════════════════════════════════════════════════
with tab_all:
    st.markdown("### All Events — Semester 2 · 2025–26")
    by_month = {}
    for ev in EVENTS:
        d = datetime.strptime(ev["date"], "%Y-%m-%d").date()
        mk = (d.year, d.month)
        by_month.setdefault(mk, []).append((d, ev))

    for (y, m) in sorted(by_month.keys()):
        st.markdown(f'<div class="ev-month-title">{MONTH_NAMES[m-1]} {y}</div>', unsafe_allow_html=True)
        for d, ev in by_month[(y,m)]:
            bg, fg = TYPE_COLORS.get(ev["type"], ("#eee","#333"))
            label = TYPE_LABELS.get(ev["type"], ev["type"].upper())
            day_name = d.strftime("%a")
            st.markdown(f"""
            <div class="ev-row" style="background:{bg}22">
              <div class="ev-row-date">{day_name}, {MONTH_NAMES[m-1][:3]} {d.day}</div>
              <div class="ev-row-name" style="color:#0d1b35">{ev['name']}</div>
              <div class="ev-badge" style="background:{bg};color:{fg}">{label}</div>
            </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# HOMEWORK TAB
# ══════════════════════════════════════════════════════════════════
with tab_hw:
    st.markdown("### 📚 All Homework")

    hw_data = st.session_state.hw
    if not hw_data or not any(hw_data.values()):
        st.info("No homework logged yet. Click **+ add HW** on any subject in the Calendar tab to get started.")
    else:
        # Group by date
        entries = []
        for dk, subjects in hw_data.items():
            for subj, text in subjects.items():
                if text:
                    d = datetime.strptime(dk, "%Y-%m-%d").date()
                    entries.append((d, dk, subj, text))
        entries.sort()

        # Filter controls
        f_col1, f_col2 = st.columns([2,3])
        with f_col1:
            filter_subj = st.selectbox(
                "Filter by subject",
                ["All"] + SUBJECTS,
                key="hw_filter_subj"
            )
        with f_col2:
            show_past = st.checkbox("Show past dates", value=True, key="hw_show_past")

        filtered = [
            e for e in entries
            if (filter_subj == "All" or e[2] == filter_subj)
            and (show_past or e[0] >= today)
        ]

        if not filtered:
            st.info("No homework matches the current filters.")
        else:
            for d, dk, subj, text in filtered:
                is_past = d < today
                with st.expander(
                    f"{'✅' if is_past else '📌'} {d.strftime('%b %-d')} · {subj}",
                    expanded=(not is_past)
                ):
                    st.markdown(f"**{d.strftime('%A, %B %-d, %Y')}**")
                    rot = get_rotation(dk)
                    if rot:
                        st.caption(f"Rotation {rot}")
                    st.markdown(text)
                    if st.button(f"✏️ Edit", key=f"hw_edit_{dk}_{subj}"):
                        st.session_state.editing_subject = (dk, subj)
                        st.session_state.selected_date = d
                        st.session_state.view_month = (d.year, d.month)
                        st.rerun()

    st.markdown("---")
    if hw_data and any(hw_data.values()):
        if st.button("🗑️ Clear ALL homework", type="secondary"):
            st.session_state.hw = {}
            st.rerun()
