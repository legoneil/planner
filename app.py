"""
Bolles MS Planner – Semester 2 2025-26
Single-file Streamlit app that serves the original HTML/CSS/JS website unchanged.
Deploy to Streamlit Community Cloud with just this file + requirements.txt.
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bolles MS Planner · Semester 2",
    page_icon="🎓",
    layout="wide",
)

# Hide Streamlit's own chrome so the embedded site fills the full viewport
st.markdown("""
<style>
  #MainMenu, header, footer { visibility: hidden; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { border: none; }
</style>
""", unsafe_allow_html=True)

# ── Complete website: HTML + CSS + JS bundled as one string ────────
# The site is 100% self-contained – localStorage persists homework
# across refreshes in the same browser, exactly as the original.
HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>Bolles MS Planner</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"/>
<style>
:root{--navy:#0a1f44;--navy-mid:#12306b;--navy-light:#1e4080;--gold:#c9952a;--gold-light:#e8b84b;--cream:#f5f0e8;--cream-dark:#ede6d8;--white:#fff;--text-dark:#0d1b35;--text-mid:#3a4f6e;--text-light:#6b7f99;--red:#c0392b;--green:#1a6b4a;--border:rgba(10,31,68,.12)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans',sans-serif;background:var(--cream);color:var(--text-dark);min-height:100vh}
header{background:var(--navy);padding:0;position:sticky;top:0;z-index:100;box-shadow:0 2px 20px rgba(0,0,0,.3)}
.header-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:0 2rem;height:64px}
.logo-area{display:flex;align-items:center;gap:.75rem}
.logo-icon{width:36px;height:36px;background:var(--gold);border-radius:4px;display:flex;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-weight:900;font-size:1.1rem;color:var(--navy)}
.logo-text{font-family:'Playfair Display',serif;font-size:1.05rem;font-weight:700;color:#fff;letter-spacing:.02em}
.logo-sub{font-size:.65rem;color:var(--gold-light);font-family:'DM Mono',monospace;letter-spacing:.1em;text-transform:uppercase;margin-top:1px}
.header-nav{display:flex;gap:.25rem}
.nav-btn{background:none;border:none;color:rgba(255,255,255,.6);font-family:'DM Sans',sans-serif;font-size:.8rem;font-weight:500;cursor:pointer;padding:.4rem .9rem;border-radius:20px;transition:all .2s;letter-spacing:.03em}
.nav-btn:hover{background:rgba(255,255,255,.1);color:#fff}
.nav-btn.active{background:var(--gold);color:var(--navy);font-weight:600}
.app{max-width:1200px;margin:0 auto;padding:2rem;display:grid;grid-template-columns:280px 1fr;gap:2rem}
.sidebar{display:flex;flex-direction:column;gap:1.25rem}
.card{background:#fff;border-radius:12px;border:1px solid var(--border);overflow:hidden;box-shadow:0 1px 8px rgba(0,0,0,.06)}
.card-header{background:var(--navy);color:#fff;padding:.75rem 1rem;font-family:'DM Mono',monospace;font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;display:flex;align-items:center;gap:.5rem}
.card-header .dot{width:6px;height:6px;border-radius:50%;background:var(--gold)}
.card-body{padding:1rem}
.mini-cal-nav{display:flex;align-items:center;justify-content:space-between;margin-bottom:.75rem}
.mini-cal-title{font-family:'Playfair Display',serif;font-size:.95rem;font-weight:700;color:var(--navy)}
.mini-nav-btn{background:none;border:1px solid var(--border);border-radius:6px;width:26px;height:26px;cursor:pointer;font-size:.75rem;color:var(--navy-mid);display:flex;align-items:center;justify-content:center;transition:all .15s}
.mini-nav-btn:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.mini-cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px}
.mini-day-label{text-align:center;font-size:.6rem;font-family:'DM Mono',monospace;color:var(--text-light);letter-spacing:.05em;padding-bottom:4px}
.mini-day{position:relative;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font-size:.72rem;border-radius:6px;cursor:pointer;transition:all .15s;font-family:'DM Mono',monospace;color:var(--text-mid)}
.mini-day:hover{background:var(--cream)}
.mini-day.today{background:var(--navy);color:#fff;font-weight:600}
.mini-day.has-event::after{content:'';position:absolute;bottom:2px;width:3px;height:3px;border-radius:50%;background:var(--gold)}
.mini-day.other-month{color:var(--text-light);opacity:.4}
.mini-day.selected{background:var(--gold);color:var(--navy);font-weight:700}
.mini-day.no-school{color:var(--red);opacity:.7}
.event-item{display:flex;gap:.6rem;padding:.5rem 0;border-bottom:1px solid var(--border);align-items:flex-start}
.event-item:last-child{border-bottom:none}
.event-dot{width:8px;height:8px;border-radius:50%;margin-top:4px;flex-shrink:0}
.event-content{flex:1;min-width:0}
.event-date{font-family:'DM Mono',monospace;font-size:.62rem;color:var(--text-light);letter-spacing:.05em;text-transform:uppercase}
.event-name{font-size:.8rem;font-weight:500;color:var(--text-dark);line-height:1.3}
.legend-item{display:flex;align-items:center;gap:.5rem;padding:.3rem 0;font-size:.78rem;color:var(--text-mid)}
.legend-dot{width:10px;height:10px;border-radius:3px;flex-shrink:0}
.cal-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem}
.cal-month{font-family:'Playfair Display',serif;font-size:2.2rem;font-weight:900;color:var(--navy);line-height:1}
.cal-year{font-family:'DM Mono',monospace;font-size:.8rem;color:var(--text-light);letter-spacing:.1em;margin-top:2px}
.cal-nav{display:flex;align-items:center;gap:.5rem}
.nav-arrow{width:38px;height:38px;border-radius:10px;border:1px solid var(--border);background:#fff;cursor:pointer;font-size:1rem;color:var(--navy);display:flex;align-items:center;justify-content:center;transition:all .15s}
.nav-arrow:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
.today-btn{padding:0 1rem;height:38px;border-radius:10px;border:1px solid var(--border);background:#fff;cursor:pointer;font-size:.8rem;font-family:'DM Sans',sans-serif;font-weight:500;color:var(--navy);transition:all .15s}
.today-btn:hover{background:var(--navy);color:#fff}
.big-cal{background:#fff;border-radius:16px;border:1px solid var(--border);overflow:hidden;box-shadow:0 2px 16px rgba(0,0,0,.07)}
.big-cal-days-header{display:grid;grid-template-columns:repeat(7,1fr);background:var(--navy)}
.day-header{padding:.65rem .5rem;text-align:center;font-family:'DM Mono',monospace;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:rgba(255,255,255,.6)}
.day-header.weekend{color:rgba(255,255,255,.35)}
.big-cal-grid{display:grid;grid-template-columns:repeat(7,1fr);border-left:1px solid var(--border);border-top:1px solid var(--border)}
.cal-day{border-right:1px solid var(--border);border-bottom:1px solid var(--border);min-height:90px;padding:.4rem;cursor:pointer;transition:background .1s;position:relative}
.cal-day:hover{background:var(--cream)}
.cal-day.other-month{background:rgba(0,0,0,.018)}
.cal-day.today{background:#eef2ff}
.cal-day.today .day-num{background:var(--navy);color:#fff}
.cal-day.selected{background:#fff8ec}
.cal-day.no-school{background:#fff5f5}
.cal-day.break{background:#f0faf5}
.day-num{position:relative;width:24px;height:24px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-family:'DM Mono',monospace;font-size:.75rem;font-weight:500;color:var(--text-mid);margin-bottom:3px}
.day-num.other{color:var(--text-light);opacity:.5}
.cal-events-list{display:flex;flex-direction:column;gap:2px}
.cal-event-chip{font-size:.62rem;padding:1px 5px;border-radius:4px;line-height:1.5;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:500}
.chip-holiday{background:#fde8e8;color:#9b2a2a}.chip-break{background:#d4f7e8;color:#1a6b4a}.chip-academic{background:#dce8ff;color:#1a3a7a}.chip-exam{background:#ffe0f0;color:#7a1a50}.chip-testing{background:#e8e0ff;color:#3a1a7a}.chip-event{background:#e0f4ff;color:#0a4a7a}
.day-detail{background:#fff;border-radius:12px;border:1px solid var(--border);margin-top:1.5rem;box-shadow:0 1px 8px rgba(0,0,0,.06);overflow:hidden}
.detail-header{background:linear-gradient(135deg,var(--navy),var(--navy-mid));padding:1.25rem 1.5rem;display:flex;align-items:center;justify-content:space-between}
.detail-date-big{font-family:'Playfair Display',serif;color:#fff}
.detail-date-big .day-name{font-size:.8rem;opacity:.7;font-family:'DM Mono',monospace;letter-spacing:.1em;text-transform:uppercase}
.detail-date-big .day-full{font-size:1.8rem;font-weight:900;line-height:1}
.rotation-badge{background:var(--gold);color:var(--navy);font-family:'DM Mono',monospace;font-size:.75rem;font-weight:700;padding:.35rem .75rem;border-radius:8px;letter-spacing:.08em}
.detail-body{padding:1.25rem 1.5rem}
.schedule-grid{display:grid;grid-template-columns:auto 1fr;gap:.25rem 1rem;align-items:start}
.sched-time{font-family:'DM Mono',monospace;font-size:.68rem;color:var(--text-light);padding-top:2px;white-space:nowrap}
.sched-item{font-size:.82rem;padding:.25rem .6rem;border-radius:6px;margin-bottom:3px}
.sched-period{background:var(--cream);color:var(--text-dark);font-weight:500}
.sched-advisory{background:#dce8ff;color:#1a3a7a}
.sched-lunch{background:#d4f7e8;color:#1a5a3a}
.sched-activity{background:#fef3d0;color:#7a5200}
.no-class-msg{text-align:center;padding:2rem;color:var(--text-light);font-family:'DM Mono',monospace;font-size:.8rem;letter-spacing:.05em}
.school-closed-msg{text-align:center;padding:1.5rem;background:#fff5f5;border-radius:10px;color:var(--red);font-weight:600;font-size:.9rem;display:flex;align-items:center;justify-content:center;gap:.5rem}
#schedule-view{display:none}
#schedule-view.active{display:block}
#calendar-view.hidden{display:none}
.sched-month-title{font-family:'Playfair Display',serif;font-size:1.4rem;font-weight:700;color:var(--navy);padding:1rem 0 .5rem;border-bottom:2px solid var(--navy);margin-bottom:.75rem}
.sched-row{display:grid;grid-template-columns:110px 1fr auto;gap:.75rem;align-items:center;padding:.6rem .75rem;border-radius:8px;transition:background .1s}
.sched-row:hover{background:var(--cream)}.sched-row.holiday{background:#fff5f5}.sched-row.break-row{background:#f0faf5}.sched-row.academic{background:#f0f5ff}
.sched-row-date{font-family:'DM Mono',monospace;font-size:.72rem;color:var(--text-light);letter-spacing:.04em}
.sched-row-name{font-size:.85rem;font-weight:500;color:var(--text-dark)}
.sched-row-badge{font-size:.62rem;padding:2px 8px;border-radius:20px;font-family:'DM Mono',monospace;white-space:nowrap}
.detail-events-bar{display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:1rem}
.sched-hint{font-family:'DM Mono',monospace;font-size:.65rem;color:var(--text-light);letter-spacing:.06em;margin-bottom:.75rem;text-transform:uppercase}
.sched-row-wrap{cursor:pointer;border-radius:8px;transition:background .15s,box-shadow .15s;border:1.5px solid transparent;margin-bottom:2px}
.sched-row-wrap:hover{background:#f0f5ff;border-color:rgba(30,64,128,.15);box-shadow:0 1px 6px rgba(0,0,0,.06)}
.sched-row-wrap.has-hw{border-color:var(--gold);background:#fffdf4}
.sched-row-wrap.has-hw:hover{background:#fff8e0}
.sched-period-inner{display:flex;flex-direction:column;gap:3px}
.hw-add-hint{font-size:.58rem;font-family:'DM Mono',monospace;color:var(--text-light);margin-left:.5rem;opacity:.7;letter-spacing:.04em;vertical-align:middle;transition:opacity .15s}
.sched-row-wrap:hover .hw-add-hint{opacity:1;color:var(--navy-mid)}
.hw-badge{font-size:.75rem;font-family:'DM Sans',sans-serif;color:#5a3e00;background:#fff3cc;border-left:3px solid var(--gold);padding:.3rem .6rem;border-radius:0 6px 6px 0;line-height:1.4;word-break:break-word}
.hw-editor{margin-top:.5rem;background:#fff;border:1.5px solid var(--gold);border-radius:10px;padding:.75rem;box-shadow:0 4px 16px rgba(0,0,0,.1)}
.hw-editor-label{font-family:'DM Mono',monospace;font-size:.68rem;color:var(--navy);letter-spacing:.06em;text-transform:uppercase;margin-bottom:.5rem;font-weight:600}
.hw-textarea{width:100%;min-height:80px;border:1px solid var(--border);border-radius:8px;padding:.5rem .65rem;font-family:'DM Sans',sans-serif;font-size:.85rem;color:var(--text-dark);resize:vertical;outline:none;transition:border-color .15s;line-height:1.5}
.hw-textarea:focus{border-color:var(--gold);box-shadow:0 0 0 3px rgba(201,149,42,.15)}
.hw-editor-actions{display:flex;gap:.5rem;margin-top:.5rem;align-items:center}
.hw-save-btn,.hw-cancel-btn,.hw-clear-btn{border:none;border-radius:7px;font-family:'DM Sans',sans-serif;font-size:.78rem;font-weight:600;cursor:pointer;padding:.35rem .85rem;transition:all .15s}
.hw-save-btn{background:var(--navy);color:#fff}.hw-save-btn:hover{background:var(--navy-mid)}
.hw-cancel-btn{background:var(--cream);color:var(--text-mid);border:1px solid var(--border)}.hw-cancel-btn:hover{background:var(--cream-dark)}
.hw-clear-btn{background:#fff0f0;color:var(--red);border:1px solid #fcc;margin-left:auto}.hw-clear-btn:hover{background:#ffe0e0}
.cal-hw-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--gold);margin-left:4px;vertical-align:middle}
@media(max-width:900px){.app{grid-template-columns:1fr;padding:1rem}.sidebar{display:none}}
</style>
</head>
<body>

<header>
  <div class="header-inner">
    <div class="logo-area">
      <div class="logo-icon">B</div>
      <div>
        <div class="logo-text">Bolles School</div>
        <div class="logo-sub">MS Planner &middot; Semester 2 &middot; 2025&ndash;26</div>
      </div>
    </div>
    <div class="header-nav">
      <button class="nav-btn active" onclick="switchView('calendar',this)">Calendar</button>
      <button class="nav-btn"        onclick="switchView('schedule',this)">All Events</button>
    </div>
  </div>
</header>

<div class="app">
  <aside class="sidebar">
    <div class="card">
      <div class="card-header"><span class="dot"></span>Quick Nav</div>
      <div class="card-body">
        <div class="mini-cal-nav">
          <button class="mini-nav-btn" onclick="miniPrev()">&lsaquo;</button>
          <div class="mini-cal-title" id="mini-title"></div>
          <button class="mini-nav-btn" onclick="miniNext()">&rsaquo;</button>
        </div>
        <div class="mini-cal-grid" id="mini-grid"></div>
      </div>
    </div>
    <div class="card">
      <div class="card-header"><span class="dot"></span>Upcoming Events</div>
      <div class="card-body" id="upcoming-list"></div>
    </div>
    <div class="card">
      <div class="card-header"><span class="dot"></span>Legend</div>
      <div class="card-body">
        <div class="legend-item"><div class="legend-dot" style="background:#fde8e8"></div>No School / Holiday</div>
        <div class="legend-item"><div class="legend-dot" style="background:#d4f7e8"></div>Break</div>
        <div class="legend-item"><div class="legend-dot" style="background:#dce8ff"></div>Academic Milestone</div>
        <div class="legend-item"><div class="legend-dot" style="background:#ffe0f0"></div>Exams</div>
        <div class="legend-item"><div class="legend-dot" style="background:#e8e0ff"></div>ERB Testing</div>
        <div class="legend-item"><div class="legend-dot" style="background:#e0f4ff"></div>Event</div>
      </div>
    </div>
  </aside>

  <main>
    <div id="calendar-view">
      <div class="cal-header">
        <div class="cal-title-area">
          <div class="cal-month" id="cal-month-title"></div>
          <div class="cal-year"  id="cal-year-title"></div>
        </div>
        <div class="cal-nav">
          <button class="nav-arrow" onclick="prevMonth()">&lsaquo;</button>
          <button class="today-btn" onclick="goToday()">Today</button>
          <button class="nav-arrow" onclick="nextMonth()">&rsaquo;</button>
        </div>
      </div>
      <div class="big-cal">
        <div class="big-cal-days-header">
          <div class="day-header">Mon</div><div class="day-header">Tue</div>
          <div class="day-header">Wed</div><div class="day-header">Thu</div>
          <div class="day-header weekend">Fri</div><div class="day-header weekend">Sat</div>
          <div class="day-header weekend">Sun</div>
        </div>
        <div class="big-cal-grid" id="big-grid"></div>
      </div>
      <div class="day-detail">
        <div class="detail-header">
          <div class="detail-date-big">
            <div class="day-name">Select a day to view details</div>
            <div class="day-full" id="detail-date-text">&mdash;</div>
          </div>
          <div class="rotation-badge" id="rotation-badge" style="display:none"></div>
        </div>
        <div class="detail-body" id="detail-body">
          <div class="no-class-msg">Click on any day to see schedule details</div>
        </div>
      </div>
    </div>

    <div id="schedule-view">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem">
        <div style="font-family:'Playfair Display',serif;font-size:1.8rem;font-weight:900;color:var(--navy)">All Events</div>
        <div style="font-family:'DM Mono',monospace;font-size:.7rem;color:var(--text-light);letter-spacing:.1em">SEMESTER 2 &middot; 2025&ndash;26</div>
      </div>
      <div class="card">
        <div class="card-body" id="all-events-list" style="padding:.5rem 1rem"></div>
      </div>
    </div>
  </main>
</div>

<script>
var EVENTS=[
  {date:'2026-01-01',name:"New Year's Day \u2014 Winter Break",type:'holiday'},
  {date:'2026-01-02',name:'Winter Break',type:'break'},
  {date:'2026-01-05',name:'Professional Development Day \u2014 No Classes',type:'holiday'},
  {date:'2026-01-06',name:'Classes Resume after Winter Break',type:'academic'},
  {date:'2026-01-19',name:'Martin Luther King Jr. Holiday \u2014 No School',type:'holiday'},
  {date:'2026-02-04',name:'Quarter 3 End of Interim',type:'academic'},
  {date:'2026-02-13',name:'Parent Conference Day \u2014 No Classes / End Trimester 2',type:'academic'},
  {date:'2026-02-16',name:"Presidents' Day \u2014 School Closed",type:'holiday'},
  {date:'2026-03-02',name:'ERB Testing Demo Day',type:'testing'},
  {date:'2026-03-09',name:'Spring Break Begins',type:'break'},
  {date:'2026-03-10',name:'Spring Break',type:'break'},
  {date:'2026-03-11',name:'Spring Break',type:'break'},
  {date:'2026-03-12',name:'Spring Break',type:'break'},
  {date:'2026-03-13',name:'Spring Break',type:'break'},
  {date:'2026-03-16',name:'Faculty Work Day \u2014 No Classes',type:'holiday'},
  {date:'2026-03-17',name:'Quarter 3 Ends / Classes Resume',type:'academic'},
  {date:'2026-03-17',name:'ERB Testing \u2014 Quantitative Reasoning',type:'testing'},
  {date:'2026-03-18',name:'ERB Testing \u2014 Reading Comprehension / Written Concepts',type:'testing'},
  {date:'2026-03-19',name:'ERB Testing \u2014 Math 1 / Written Mechanics / Verbal Reasoning',type:'testing'},
  {date:'2026-03-20',name:'Eid al-Fitr \u2014 No Quizzes or Tests',type:'event'},
  {date:'2026-03-23',name:'ERB Testing \u2014 Math 2 / Vocabulary',type:'testing'},
  {date:'2026-04-03',name:'Good Friday / Spring Holiday \u2014 School Closed',type:'holiday'},
  {date:'2026-04-05',name:'Easter',type:'event'},
  {date:'2026-04-06',name:'Spring Holiday \u2014 School Closed',type:'holiday'},
  {date:'2026-04-17',name:'Quarter 4 End of Interim',type:'academic'},
  {date:'2026-04-27',name:'Grade 8 Class Trip Begins',type:'event'},
  {date:'2026-04-28',name:'Grade 8 Class Trip',type:'event'},
  {date:'2026-04-29',name:'Grade 8 Class Trip',type:'event'},
  {date:'2026-05-01',name:'Grade 8 Class Trip Ends',type:'event'},
  {date:'2026-05-04',name:'Middle School Madness Week Begins',type:'event'},
  {date:'2026-05-15',name:'Last Day of Classes / Quarter 4 Ends',type:'academic'},
  {date:'2026-05-18',name:'Reading Day \u2014 No Classes',type:'academic'},
  {date:'2026-05-19',name:'MS/US Exam Week',type:'exam'},
  {date:'2026-05-20',name:'MS/US Exams',type:'exam'},
  {date:'2026-05-21',name:'MS/US Exams / Grade 8 Recognition Day',type:'exam'},
  {date:'2026-05-22',name:'MS/US Exams',type:'exam'},
  {date:'2026-05-23',name:'Commencement \u2014 Class of 2026',type:'event'},
  {date:'2026-05-25',name:'Memorial Day \u2014 School Closed',type:'holiday'},
  {date:'2026-05-26',name:'Make-up Exams',type:'exam'}
];

var ROTATIONS={
  '2026-01-06':'B','2026-01-07':'C','2026-01-08':'D','2026-01-09':'E',
  '2026-01-12':'F','2026-01-13':'G','2026-01-14':'A','2026-01-15':'B','2026-01-16':'C',
  '2026-01-20':'D','2026-01-21':'E','2026-01-22':'F','2026-01-23':'G',
  '2026-01-26':'A','2026-01-27':'B','2026-01-28':'C','2026-01-29':'D','2026-01-30':'E',
  '2026-02-02':'F','2026-02-03':'G','2026-02-04':'A','2026-02-05':'B','2026-02-06':'C',
  '2026-02-09':'D','2026-02-10':'E','2026-02-11':'F','2026-02-12':'G',
  '2026-02-17':'A','2026-02-18':'B','2026-02-19':'C','2026-02-20':'D',
  '2026-02-23':'E','2026-02-24':'F','2026-02-25':'G','2026-02-26':'A','2026-02-27':'B',
  '2026-03-02':'C','2026-03-03':'D','2026-03-04':'E','2026-03-05':'F','2026-03-06':'G',
  '2026-03-17':'A','2026-03-18':'B','2026-03-19':'C','2026-03-20':'D',
  '2026-03-23':'E','2026-03-24':'F','2026-03-25':'G','2026-03-26':'A','2026-03-27':'B',
  '2026-03-30':'C','2026-03-31':'D','2026-04-01':'E','2026-04-02':'F',
  '2026-04-07':'G','2026-04-08':'A','2026-04-09':'B','2026-04-10':'C',
  '2026-04-13':'D','2026-04-14':'E','2026-04-15':'F','2026-04-16':'G','2026-04-17':'A',
  '2026-04-20':'B','2026-04-21':'C','2026-04-22':'D','2026-04-23':'E','2026-04-24':'F',
  '2026-04-27':'G','2026-04-28':'A','2026-04-29':'B','2026-04-30':'C',
  '2026-05-01':'D','2026-05-04':'E','2026-05-05':'F','2026-05-06':'G','2026-05-07':'A','2026-05-08':'B',
  '2026-05-11':'C','2026-05-12':'D','2026-05-13':'E','2026-05-14':'F','2026-05-15':'G'
};

var NO_SCHOOL=new Set(['2026-01-01','2026-01-02','2026-01-05','2026-01-19','2026-02-13','2026-02-16','2026-03-09','2026-03-10','2026-03-11','2026-03-12','2026-03-13','2026-03-16','2026-04-03','2026-04-06','2026-05-18','2026-05-25']);
var MONTHS=['January','February','March','April','May','June','July','August','September','October','November','December'];

function getHW(d){try{return JSON.parse(localStorage.getItem('bolles_hw_'+d)||'{}')}catch(e){return{}}}
function setHW(d,l,t){var o=getHW(d);if(t.trim()===''){delete o[l]}else{o[l]=t.trim();}localStorage.setItem('bolles_hw_'+d,JSON.stringify(o))}
function hasAnyHW(d){return Object.keys(getHW(d)).length>0}

var today=new Date(),currentYear,currentMonth,miniYear,miniMonth,selectedDate=null;
function toKey(y,m,d){return y+'-'+String(m+1).padStart(2,'0')+'-'+String(d).padStart(2,'0')}
function eventsFor(k){return EVENTS.filter(function(e){return e.date===k})}
function esc(s){return String(s).replace(/\\/g,'\\\\').replace(/'/g,"\\'")}

function getSched(dateStr){
  var dow=new Date(dateStr).getDay(),isWed=dow===3,rot=ROTATIONS[dateStr];
  if(NO_SCHOOL.has(dateStr)||!rot)return null;
  if(isWed)return[
    {id:'zh', time:'8:00\u20138:30',  label:'Zero Hour',            cls:'sched-period',  isPeriod:false},
    {id:'p1', time:'8:30\u20139:25',  label:'Math',                 cls:'sched-period',  isPeriod:true},
    {id:'adv',time:'9:25\u201310:25', label:'Advisory + Activities',cls:'sched-advisory',isPeriod:false},
    {id:'p2', time:'10:25\u201311:10',label:'Spanish',              cls:'sched-period',  isPeriod:true},
    {id:'p3', time:'11:10\u201312:05',label:'English',              cls:'sched-period',  isPeriod:true},
    {id:'l8', time:'12:05\u201312:25',label:'Grade 8 Lunch',        cls:'sched-lunch',   isPeriod:false},
    {id:'l6', time:'12:25\u201312:40',label:'Grade 6 Lunch',        cls:'sched-lunch',   isPeriod:false},
    {id:'l7', time:'12:40\u20131:00', label:'Grade 7 Lunch \u2605', cls:'sched-lunch',   isPeriod:false},
    {id:'p4', time:'1:05\u20132:00',  label:'PE',                   cls:'sched-period',  isPeriod:true},
    {id:'p5', time:'2:05\u20133:00',  label:'Speech & Debate',      cls:'sched-period',  isPeriod:true}
  ];
  var S=['Math','Spanish','English','PE','Speech & Debate','Science','History'];
  var ri='ABCDEFG'.indexOf(rot);
  function s(o){return S[(ri+o)%7]}
  var mid=dow===1&&['A','C','E','G'].indexOf(rot)!==-1?'Convocation':'Activities';
  return[
    {id:'zh', time:'8:00\u20138:30',  label:'Zero Hour (Optional)', cls:'sched-period',  isPeriod:false},
    {id:'adv',time:'8:30\u20138:40',  label:'Advisory',             cls:'sched-advisory',isPeriod:false},
    {id:'p1', time:'8:45\u20139:40',  label:s(0),                   cls:'sched-period',  isPeriod:true},
    {id:'p2', time:'9:45\u201310:40', label:s(1),                   cls:'sched-period',  isPeriod:true},
    {id:'act',time:'10:40\u201311:10',label:mid,                    cls:'sched-activity',isPeriod:false},
    {id:'p3', time:'11:10\u201312:05',label:s(2),                   cls:'sched-period',  isPeriod:true},
    {id:'l8', time:'12:05\u201312:25',label:'Grade 8 Lunch',        cls:'sched-lunch',   isPeriod:false},
    {id:'l6', time:'12:25\u201312:40',label:'Grade 6 Lunch',        cls:'sched-lunch',   isPeriod:false},
    {id:'l7', time:'12:40\u20131:00', label:'Grade 7 Lunch \u2605', cls:'sched-lunch',   isPeriod:false},
    {id:'p4', time:'1:05\u20132:00',  label:s(3),                   cls:'sched-period',  isPeriod:true},
    {id:'p5', time:'2:05\u20133:00',  label:s(4),                   cls:'sched-period',  isPeriod:true},
    {id:'as', time:'3:00+',           label:'After School',         cls:'sched-activity',isPeriod:false}
  ];
}

function openHWEdit(dateStr,pid,lbl){
  document.querySelectorAll('.hw-editor').forEach(function(e){e.remove()});
  var row=document.querySelector('.sched-row-wrap[data-period="'+pid+'"]');if(!row)return;
  var ex=getHW(dateStr)[lbl]||'';
  var ed=document.createElement('div');ed.className='hw-editor';
  ed.innerHTML='<div class="hw-editor-label">\ud83d\udcda Homework \u2014 '+lbl+'</div>'
    +'<textarea class="hw-textarea" placeholder="Enter homework, due dates, notes\u2026">'+ex+'</textarea>'
    +'<div class="hw-editor-actions">'
    +'<button class="hw-save-btn">Save</button>'
    +'<button class="hw-cancel-btn">Cancel</button>'
    +(ex?'<button class="hw-clear-btn">Clear</button>':'')
    +'</div>';
  ed.querySelector('.hw-save-btn').onclick=function(){setHW(dateStr,lbl,ed.querySelector('textarea').value);refreshRow(dateStr,pid,lbl)};
  ed.querySelector('.hw-cancel-btn').onclick=function(){ed.remove()};
  if(ex)ed.querySelector('.hw-clear-btn').onclick=function(){setHW(dateStr,lbl,'');refreshRow(dateStr,pid,lbl)};
  ed.addEventListener('click',function(e){e.stopPropagation()});
  row.appendChild(ed);ed.querySelector('textarea').focus();
}

function refreshRow(dateStr,pid,lbl){
  var row=document.querySelector('.sched-row-wrap[data-period="'+pid+'"]');if(!row)return;
  var hw=getHW(dateStr)[lbl]||'';
  var inner=row.querySelector('.sched-period-inner');
  var badge=row.querySelector('.hw-badge');
  var hint=row.querySelector('.hw-add-hint');
  if(hw){row.classList.add('has-hw');if(!badge){badge=document.createElement('div');badge.className='hw-badge';inner.appendChild(badge)}badge.textContent=hw.length>70?hw.slice(0,67)+'\u2026':hw;if(hint)hint.textContent='\u270f\ufe0f edit';}
  else{row.classList.remove('has-hw');if(badge)badge.remove();if(hint)hint.textContent='+ add HW';}
  var e=row.querySelector('.hw-editor');if(e)e.remove();
  renderBigCal();
}

function renderBigCal(){
  document.getElementById('cal-month-title').textContent=MONTHS[currentMonth];
  document.getElementById('cal-year-title').textContent=currentYear+' \u00b7 Semester 2';
  var grid=document.getElementById('big-grid');grid.innerHTML='';
  var fd=new Date(currentYear,currentMonth,1),sd=fd.getDay();sd=sd===0?6:sd-1;
  var dim=new Date(currentYear,currentMonth+1,0).getDate();
  var dip=new Date(currentYear,currentMonth,0).getDate();
  var tc=Math.ceil((sd+dim)/7)*7;
  for(var i=0;i<tc;i++){
    var dn,yr,mo,io=false;
    if(i<sd){dn=dip-sd+i+1;mo=currentMonth-1;yr=currentYear;if(mo<0){mo=11;yr--;}io=true;}
    else if(i>=sd+dim){dn=i-sd-dim+1;mo=currentMonth+1;yr=currentYear;if(mo>11){mo=0;yr++;}io=true;}
    else{dn=i-sd+1;mo=currentMonth;yr=currentYear;}
    var k=toKey(yr,mo,dn);
    var iT=yr===today.getFullYear()&&mo===today.getMonth()&&dn===today.getDate();
    var iS=selectedDate===k,ns=NO_SCHOOL.has(k);
    var ib=EVENTS.some(function(e){return e.date===k&&e.type==='break'});
    var hw=!io&&hasAnyHW(k);
    var c=document.createElement('div');c.className='cal-day';
    if(iT)c.classList.add('today');if(iS)c.classList.add('selected');
    if(ns)c.classList.add('no-school');else if(ib)c.classList.add('break');
    if(io)c.classList.add('other-month');
    var ne=document.createElement('div');ne.className='day-num'+(io?' other':'');ne.textContent=dn;
    if(hw){var hd=document.createElement('span');hd.className='cal-hw-dot';hd.title='Homework';ne.appendChild(hd);}
    c.appendChild(ne);
    var el=document.createElement('div');el.className='cal-events-list';
    var evs=eventsFor(k);
    evs.slice(0,2).forEach(function(ev){var p=document.createElement('div');p.className='cal-event-chip chip-'+ev.type;p.textContent=ev.name;p.title=ev.name;el.appendChild(p);});
    if(evs.length>2){var m=document.createElement('div');m.className='cal-event-chip';m.style.cssText='color:var(--text-light);font-size:.58rem;';m.textContent='+'+(evs.length-2)+' more';el.appendChild(m);}
    if(!io&&ROTATIONS[k]){var re=document.createElement('div');re.style.cssText='font-family:"DM Mono",monospace;font-size:.58rem;color:var(--text-light);margin-top:2px;letter-spacing:.05em;';re.textContent='Rotation '+ROTATIONS[k]+(new Date(k).getDay()===3?' \u00b7 Late Start':'');el.appendChild(re);}
    c.appendChild(el);
    (function(key,y,m,d){c.addEventListener('click',function(){selectDay(key,y,m,d);});})(k,yr,mo,dn);
    grid.appendChild(c);
  }
}

function selectDay(k,y,m,d){selectedDate=k;renderBigCal();renderMiniCal();showDetail(k,y,m,d);}

function showDetail(k,y,m,d){
  var dt=new Date(y,m,d);
  var dn=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][dt.getDay()];
  document.querySelector('.day-name').textContent=dn;
  document.getElementById('detail-date-text').textContent=MONTHS[m]+' '+d+', '+y;
  var rot=ROTATIONS[k],badge=document.getElementById('rotation-badge');
  if(rot){badge.style.display='block';badge.textContent='Rotation '+rot+(dt.getDay()===3?' \u00b7 Late Start':'');}else{badge.style.display='none';}
  var body=document.getElementById('detail-body');
  var evs=eventsFor(k),ns=NO_SCHOOL.has(k),iw=dt.getDay()===0||dt.getDay()===6;
  var html='';
  if(evs.length){html+='<div class="detail-events-bar">';evs.forEach(function(ev){html+='<span class="cal-event-chip chip-'+ev.type+'">'+ev.name+'</span>';});html+='</div>';}
  if(iw){html+='<div class="no-class-msg">\ud83c\udf05 Weekend</div>';}
  else if(ns||!rot){html+='<div class="school-closed-msg">\ud83d\udeab '+(evs.length?evs[0].name:'No School')+'</div>';}
  else{
    var sc=getSched(k);
    if(sc){
      var hw=getHW(k);
      html+='<div class="sched-hint">\ud83d\udca1 Click any subject to add or edit homework</div><div class="schedule-grid">';
      sc.forEach(function(s){
        html+='<div class="sched-time">'+s.time+'</div>';
        if(s.isPeriod){
          var ht=hw[s.label]||'',hh=ht.length>0,sd2=esc(k),sl=esc(s.label);
          var bh=hh?'<div class="hw-badge">'+(ht.length>70?ht.slice(0,67)+'\u2026':ht)+'</div>':'';
          html+='<div class="sched-row-wrap'+(hh?' has-hw':'')+'" data-period="'+s.id+'" onclick="openHWEdit(\''+sd2+'\',\''+s.id+'\',\''+sl+'\')">'
            +'<div class="sched-period-inner"><div class="sched-item '+s.cls+'">'+s.label
            +'<span class="hw-add-hint">'+(hh?'\u270f\ufe0f edit':'+ add HW')+'</span></div>'+bh+'</div></div>';
        }else{html+='<div class="sched-item '+s.cls+'">'+s.label+'</div>';}
      });
      html+='</div>';
    }
  }
  body.innerHTML=html||'<div class="no-class-msg">No events today</div>';
}

function renderMiniCal(){
  var rt=MONTHS[miniMonth]+' '+miniYear;
  document.getElementById('mini-title').textContent=rt.length>12?MONTHS[miniMonth].slice(0,3)+' '+miniYear:rt;
  var g=document.getElementById('mini-grid');g.innerHTML='';
  ['M','T','W','T','F','S','S'].forEach(function(l){var e=document.createElement('div');e.className='mini-day-label';e.textContent=l;g.appendChild(e);});
  var fd=new Date(miniYear,miniMonth,1),sd=fd.getDay();sd=sd===0?6:sd-1;
  var dim=new Date(miniYear,miniMonth+1,0).getDate(),dip=new Date(miniYear,miniMonth,0).getDate();
  var tc=Math.ceil((sd+dim)/7)*7;
  for(var i=0;i<tc;i++){
    var dn,yr,mo,io=false;
    if(i<sd){dn=dip-sd+i+1;mo=miniMonth-1;yr=miniYear;if(mo<0){mo=11;yr--;}io=true;}
    else if(i>=sd+dim){dn=i-sd-dim+1;mo=miniMonth+1;yr=miniYear;if(mo>11){mo=0;yr++;}io=true;}
    else{dn=i-sd+1;mo=miniMonth;yr=miniYear;}
    var k=toKey(yr,mo,dn),el=document.createElement('div');el.className='mini-day';el.textContent=dn;
    if(io)el.classList.add('other-month');
    if(yr===today.getFullYear()&&mo===today.getMonth()&&dn===today.getDate())el.classList.add('today');
    if(selectedDate===k)el.classList.add('selected');
    if(NO_SCHOOL.has(k))el.classList.add('no-school');
    if(eventsFor(k).length)el.classList.add('has-event');
    (function(key,y,m,d){el.addEventListener('click',function(){currentYear=y;currentMonth=m;renderBigCal();selectDay(key,y,m,d);});})(k,yr,mo,dn);
    g.appendChild(el);
  }
}

function miniPrev(){miniMonth--;if(miniMonth<0){miniMonth=11;miniYear--;}renderMiniCal();}
function miniNext(){miniMonth++;if(miniMonth>11){miniMonth=0;miniYear++;}renderMiniCal();}

function renderUpcoming(){
  var now=new Date();
  var up=EVENTS.filter(function(e){return new Date(e.date)>=now;}).sort(function(a,b){return a.date.localeCompare(b.date);}).slice(0,6);
  var cm={holiday:'#e74c3c',break:'#27ae60',academic:'#2980b9',exam:'#8e44ad',testing:'#6c3483',event:'#16a085'};
  document.getElementById('upcoming-list').innerHTML=up.map(function(ev){
    var d=new Date(ev.date+'T00:00:00');
    return '<div class="event-item"><div class="event-dot" style="background:'+(cm[ev.type]||'#888')+'"></div><div class="event-content"><div class="event-date">'+MONTHS[d.getMonth()].slice(0,3).toUpperCase()+' '+d.getDate()+'</div><div class="event-name">'+ev.name+'</div></div></div>';
  }).join('');
}

function renderAllEvents(){
  var bm={};
  EVENTS.forEach(function(ev){var d=new Date(ev.date+'T00:00:00');var k=d.getFullYear()+'-'+d.getMonth();if(!bm[k])bm[k]={year:d.getFullYear(),month:d.getMonth(),events:[]};bm[k].events.push(ev);});
  var tl={holiday:'NO SCHOOL',break:'BREAK',academic:'ACADEMIC',exam:'EXAM',testing:'TESTING',event:'EVENT'};
  var tc={holiday:'#fde8e8',break:'#d4f7e8',academic:'#dce8ff',exam:'#ffe0f0',testing:'#e8e0ff',event:'#e0f4ff'};
  var tt={holiday:'#9b2a2a',break:'#1a6b4a',academic:'#1a3a7a',exam:'#7a1a50',testing:'#3a1a7a',event:'#0a4a7a'};
  var dl=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],html='';
  Object.values(bm).sort(function(a,b){return a.year-b.year||a.month-b.month;}).forEach(function(mb){
    html+='<div class="sched-month-title">'+MONTHS[mb.month]+' '+mb.year+'</div>';
    mb.events.forEach(function(ev){
      var d=new Date(ev.date+'T00:00:00');var rc=ev.type==='holiday'?'holiday':ev.type==='break'?'break-row':'academic';
      html+='<div class="sched-row '+rc+'"><div class="sched-row-date">'+dl[d.getDay()]+', '+MONTHS[mb.month].slice(0,3)+' '+d.getDate()+'</div><div class="sched-row-name">'+ev.name+'</div><div class="sched-row-badge" style="background:'+tc[ev.type]+';color:'+tt[ev.type]+'">'+(tl[ev.type]||ev.type.toUpperCase())+'</div></div>';
    });
  });
  document.getElementById('all-events-list').innerHTML=html;
}

function prevMonth(){currentMonth--;if(currentMonth<0){currentMonth=11;currentYear--;}miniMonth=currentMonth;miniYear=currentYear;renderBigCal();renderMiniCal();}
function nextMonth(){currentMonth++;if(currentMonth>11){currentMonth=0;currentYear++;}miniMonth=currentMonth;miniYear=currentYear;renderBigCal();renderMiniCal();}
function goToday(){currentYear=today.getFullYear();currentMonth=today.getMonth();miniYear=currentYear;miniMonth=currentMonth;renderBigCal();renderMiniCal();}
function switchView(v,btn){document.querySelectorAll('.nav-btn').forEach(function(b){b.classList.remove('active');});btn.classList.add('active');if(v==='calendar'){document.getElementById('calendar-view').classList.remove('hidden');document.getElementById('schedule-view').classList.remove('active');}else{document.getElementById('calendar-view').classList.add('hidden');document.getElementById('schedule-view').classList.add('active');}}

if(today>=new Date('2026-01-01')&&today<=new Date('2026-05-31')){currentYear=today.getFullYear();currentMonth=today.getMonth();}else{currentYear=2026;currentMonth=0;}
miniYear=currentYear;miniMonth=currentMonth;
renderBigCal();renderMiniCal();renderUpcoming();renderAllEvents();
</script>
</body>
</html>"""

components.html(HTML, height=1800, scrolling=True)
