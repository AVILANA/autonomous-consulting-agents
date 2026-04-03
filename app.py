import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Autonomous Consulting Agents", layout="wide", initial_sidebar_state="expanded")

if 'page' not in st.session_state:
    st.session_state.page = "System Architecture"

query_params = st.query_params
if 'page' in query_params:
    st.session_state.page = query_params['page']
    st.session_state.nav_override = True
    st.query_params.clear()

DIAGRAM_HTML = """
<html><body style="background:#0E1117;margin:0;display:flex;justify-content:center;">
<svg width="900" height="900" xmlns="http://www.w3.org/2000/svg">
<defs>
<filter id="glow"><feGaussianBlur stdDeviation="3" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<circle cx="450" cy="450" r="187.5" stroke="#374151" stroke-width="1" stroke-dasharray="8,4" fill="none">
<animateTransform attributeName="transform" type="rotate" from="0 450 450" to="360 450 450" dur="60s" repeatCount="indefinite"/>
</circle>
<circle cx="450" cy="450" r="362.5" stroke="#374151" stroke-width="1" stroke-dasharray="8,4" fill="none">
<animateTransform attributeName="transform" type="rotate" from="360 450 450" to="0 450 450" dur="90s" repeatCount="indefinite"/>
</circle>
<circle cx="450" cy="450" r="72.5" fill="#1E1E2E" stroke="#7C3AED" stroke-width="2.5" filter="url(#glow)"/>
<text x="450" y="443.75" text-anchor="middle" fill="#7C3AED" font-size="15" font-weight="bold" font-family="Arial">ORCHESTRATOR</text>
<text x="450" y="468.75" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Coordinates All</text>
<circle cx="450" cy="262.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="450" y="258.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 1</text><text x="450" y="277.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Research</text>
<circle cx="585" cy="300" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="585" y="296.25" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 2</text><text x="585" y="315" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Benchmark</text>
<circle cx="637.5" cy="437.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="637.5" y="433.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 3</text><text x="637.5" y="452.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Operating</text>
<circle cx="585" cy="587.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="585" y="583.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 4</text><text x="585" y="602.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">AI Value</text>
<circle cx="450" cy="637.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="450" y="633.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 5</text><text x="450" y="652.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Signals</text>
<circle cx="315" cy="587.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="315" y="583.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 6</text><text x="315" y="602.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Diligence</text>
<circle cx="262.5" cy="437.5" r="52.5" fill="#1E1E2E" stroke="#00D4FF" stroke-width="1.5" filter="url(#glow)"/><text x="262.5" y="433.75" text-anchor="middle" fill="#00D4FF" font-size="12.5" font-weight="bold" font-family="Arial">Agent 7</text><text x="262.5" y="452.5" text-anchor="middle" fill="#9CA3AF" font-size="10" font-family="Arial">Composer</text>
<line x1="450" y1="377.5" x2="450" y2="315" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="487.5" y1="393.75" x2="528.75" y2="337.5" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="506.25" y1="450" x2="585" y2="437.5" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="487.5" y1="506.25" x2="528.75" y2="562.5" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="450" y1="522.5" x2="450" y2="585" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="412.5" y1="506.25" x2="371.25" y2="562.5" stroke="#374151" stroke-dasharray="4,3"/>
<line x1="393.75" y1="450" x2="315" y2="437.5" stroke="#374151" stroke-dasharray="4,3"/>
<rect x="362.5" y="37.5" width="175" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#10B981" stroke-width="1.5"/><text x="450" y="65" text-anchor="middle" fill="#10B981" font-size="13.75" font-weight="bold" font-family="Arial">TOOLS</text><text x="450" y="83.75" text-anchor="middle" fill="#6B7280" font-size="10" font-family="Arial">Web Search, Files</text>
<line x1="450" y1="93.75" x2="450" y2="210" stroke="#10B981" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="718.75" y="212.5" width="162.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#10B981" stroke-width="1.5"/><text x="800" y="240" text-anchor="middle" fill="#10B981" font-size="13.75" font-weight="bold" font-family="Arial">MEMORY</text><text x="800" y="258.75" text-anchor="middle" fill="#6B7280" font-size="10" font-family="Arial">Quality Standards</text>
<line x1="718.75" y1="241.25" x2="637.5" y2="300" stroke="#10B981" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="743.75" y="500" width="137.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#10B981" stroke-width="1.5"/><text x="812.5" y="527.5" text-anchor="middle" fill="#10B981" font-size="13.75" font-weight="bold" font-family="Arial">SKILLS</text><text x="812.5" y="546.25" text-anchor="middle" fill="#6B7280" font-size="8" font-family="Arial">8 Commands</text>
<line x1="743.75" y1="528.75" x2="637.5" y2="575" stroke="#10B981" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="18.75" y="212.5" width="162.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#F59E0B" stroke-width="1.5"/><text x="100" y="240" text-anchor="middle" fill="#F59E0B" font-size="13.75" font-weight="bold" font-family="Arial">EVALUATOR</text><text x="100" y="258.75" text-anchor="middle" fill="#6B7280" font-size="10" font-family="Arial">11 Quality Checks</text>
<line x1="181.25" y1="241.25" x2="262.5" y2="387.5" stroke="#F59E0B" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="18.75" y="500" width="162.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#F59E0B" stroke-width="1.5"/><text x="100" y="527.5" text-anchor="middle" fill="#F59E0B" font-size="13.75" font-weight="bold" font-family="Arial">HUMAN LOOP</text><text x="100" y="546.25" text-anchor="middle" fill="#6B7280" font-size="8" font-family="Arial">Feedback to Memory</text>
<line x1="181.25" y1="528.75" x2="315" y2="550" stroke="#F59E0B" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="318.75" y="800" width="262.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#10B981" stroke-width="1.5"/><text x="450" y="827.5" text-anchor="middle" fill="#10B981" font-size="13.75" font-weight="bold" font-family="Arial">KNOWLEDGE / FILES</text><text x="450" y="846.25" text-anchor="middle" fill="#6B7280" font-size="10" font-family="Arial">SEC Filings, Reports, Transcripts</text>
<line x1="450" y1="800" x2="450" y2="690" stroke="#10B981" stroke-dasharray="4,3" opacity="0.4"/>
<rect x="718.75" y="356.25" width="162.5" height="56.25" rx="12.5" fill="#1E1E2E" stroke="#10B981" stroke-width="1.5"/><text x="800" y="383.75" text-anchor="middle" fill="#10B981" font-size="13.75" font-weight="bold" font-family="Arial">LLM ENGINE</text><text x="800" y="402.5" text-anchor="middle" fill="#6B7280" font-size="10" font-family="Arial">Claude Opus + Sonnet</text>
<line x1="718.75" y1="385" x2="690" y2="437.5" stroke="#10B981" stroke-dasharray="4,3" opacity="0.4"/>
</svg></body></html>
"""

CSS = """
<style>
.stApp {background-color: #0E1117;}
[data-testid="stSidebar"] {background-color: #0a0a14;}
.hero-box {background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); border-radius: 16px; padding: 40px; margin: 10px; border: 2px solid #00D4FF; text-align: center; transition: all 0.3s ease; width:100%; cursor: pointer;}
.hero-box:hover {border-color: #7C3AED; box-shadow: 0 0 30px rgba(124,58,237,0.3);}
.hero-box-client {background: linear-gradient(135deg, #1a1a2e 0%, #1a2e1a 100%); border: 2px solid #7C3AED;}
.hero-box h2, .hero-box-client h2 {color: #FFFFFF !important; margin: 0; font-size: 32px; font-weight: bold;}
.hero-box p {color: #9CA3AF; margin-top: 10px;}
.metric-box {background: #1a1a2e; border: none; border-radius: 12px; padding: 30px; text-align: center; width: 100%;}
.metric-box .number {font-size: 42px; font-weight: bold; color: #00D4FF;}
.metric-box .label {color: #9CA3AF; font-size: 14px; margin-top: 4px;}
div[data-testid="stMarkdownContainer"] h1 {color: #00D4FF;}
div[data-testid="stMarkdownContainer"] h2 {color: #E2E8F0;}
div[data-testid="stMarkdownContainer"] h3 {color: #E2E8F0;}
div[data-testid="stMarkdownContainer"] { font-size: 17px; line-height: 1.7; }
div[data-testid="stMarkdownContainer"] p { font-size: 17px; }
div[data-testid="stMarkdownContainer"] li { font-size: 17px; }
div[data-testid="stMarkdownContainer"] td { font-size: 15px; }
/* Default button style - subtle */
.stButton>button {
background: transparent;
border: 1px solid #374151;
color: #9CA3AF;
font-size: 13px;
padding: 6px 14px;
border-radius: 8px;
font-weight: normal;
transition: all 0.2s ease;
min-height: unset;
}
.stButton>button:hover {
color: #E2E8F0;
border-color: #6B7280;
box-shadow: none;
background: rgba(255,255,255,0.04);
}
/* Hero Internal button - scoped via marker div */
[data-testid="stColumn"]:has(#hero-int-marker) [data-testid="stButton"] button {
background: linear-gradient(135deg, #1a1a2e, #16213e) !important;
border: 2px solid #00D4FF !important;
border-radius: 16px !important;
padding: 45px 30px !important;
color: white !important;
font-size: 28px !important;
font-weight: bold !important;
width: 100% !important;
min-height: 160px !important;
transition: all 0.3s ease !important;
}
[data-testid="stColumn"]:has(#hero-int-marker) [data-testid="stButton"] button:hover {
border-color: #7C3AED !important;
box-shadow: 0 0 30px rgba(124,58,237,0.3) !important;
background: linear-gradient(135deg, #1a1a2e, #16213e) !important;
}
/* Hero Client button - scoped via marker div */
[data-testid="stColumn"]:has(#hero-cli-marker) [data-testid="stButton"] button {
background: linear-gradient(135deg, #1a1a2e, #1a2e1a) !important;
border: 2px solid #7C3AED !important;
border-radius: 16px !important;
padding: 45px 30px !important;
color: white !important;
font-size: 28px !important;
font-weight: bold !important;
width: 100% !important;
min-height: 160px !important;
transition: all 0.3s ease !important;
}
[data-testid="stColumn"]:has(#hero-cli-marker) [data-testid="stButton"] button:hover {
border-color: #00D4FF !important;
box-shadow: 0 0 30px rgba(0,212,255,0.3) !important;
background: linear-gradient(135deg, #1a1a2e, #1a2e1a) !important;
}
</style>
"""

def read_file(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except:
        return "File not available yet."

st.markdown(CSS, unsafe_allow_html=True)

out = Path("outputs")
companies = [d.name for d in out.iterdir() if d.is_dir() and d.name != ".gitkeep"] if out.exists() else []
company = st.sidebar.selectbox("Select Company", companies) if companies else None
st.sidebar.markdown("---")
st.sidebar.markdown("**AUTONOMOUS CONSULTING AGENTS**")
st.sidebar.markdown("*AI-Powered Pursuit Intelligence*")
st.sidebar.markdown("---")
_pages = ["System Architecture", "Internal Pursuit Memo", "Client Preview", "Agent Deep Dive", "Sources"]
if st.session_state.get('nav_override'):
    st.session_state.sidebar_nav = st.session_state.page
    st.session_state.nav_override = False
page = st.sidebar.radio("Navigation", _pages, key="sidebar_nav")
st.session_state.page = page
st.sidebar.markdown("---")
st.sidebar.markdown("*Powered by Claude Code*")

if company:
    base = out / company
    src_content = read_file(base/"sources"/"source_index.md")
    src_count = src_content.count("http") if src_content else len(list((base/"sources").glob("*")))
    file_count = len(list(base.glob("*.md")))
    q_count = read_file(base/"discovery_questions.md").count("?") if (base/"discovery_questions.md").exists() else 0

    if page != "System Architecture":
        if st.button("← Back to Overview", key="back"):
            st.session_state.page = "System Architecture"
            st.session_state.nav_override = True
            st.rerun()

    if page == "System Architecture":
        st.markdown(f'<div style="text-align:center;"><img src="https://upload.wikimedia.org/wikipedia/commons/2/20/Adidas_Logo.svg" width="160" style="filter:invert(1);margin-bottom:10px;"><p style="color:#9CA3AF;">Autonomous Consulting Agents Analysis</p></div>', unsafe_allow_html=True)
        c1, c2 = st.columns([1,1])
        with c1:
            st.markdown('<a href="?page=Internal+Pursuit+Memo" target="_self" style="text-decoration:none;display:block;"><div class="hero-box"><span style="display:block;color:#FFFFFF;font-size:28px;font-weight:bold;margin:0;">Internal Discovery Assessment</span><p style="color:#9CA3AF;margin-top:12px;">Full analytical dossier with source citations, peer benchmarking, and 15 prioritized discovery questions</p></div></a>', unsafe_allow_html=True)
        with c2:
            st.markdown('<a href="?page=Client+Preview" target="_self" style="text-decoration:none;display:block;"><div class="hero-box hero-box-client"><span style="display:block;color:#FFFFFF;font-size:28px;font-weight:bold;margin:0;">Client-Ready Executive Summary</span><p style="color:#9CA3AF;margin-top:12px;">Polished client-facing preview ready for executive presentation</p></div></a>', unsafe_allow_html=True)
        st.markdown("---")
        c1, c2, c3 = st.columns(3, gap="small")
        with c1:
            st.markdown(f'<div class="metric-box"><div class="number">7</div><div class="label">Specialized Agents</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="metric-box"><div class="number">{src_count}</div><div class="label">Sources Analyzed</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="metric-box"><div class="number">{q_count}</div><div class="label">Discovery Questions</div></div>', unsafe_allow_html=True)
        st.markdown("---")
        components.html(DIAGRAM_HTML, height=1000)
        st.markdown("---")
        if st.session_state.get('show_questions'):
            st.markdown("## Discovery Questions")
            st.markdown(read_file(base/"discovery_questions.md"))
            st.markdown("---")
        with st.expander("View Memory System"):
            st.markdown(read_file("memory.md"))
        st.markdown("---")
        st.markdown("## AGENT TEAM")
        agents = [
            {"name": "Orchestrator", "role": "Coordinates All", "tools": "Workflow Management"},
            {"name": "Agent 1", "role": "Company Research", "tools": "Web Search, File Reading"},
            {"name": "Agent 2", "role": "Peer Benchmark", "tools": "Data Analysis, Comparison"},
            {"name": "Agent 3", "role": "Operating Model", "tools": "Process Mapping, Tech Assessment"},
            {"name": "Agent 4", "role": "AI Value", "tools": "Value Modeling, Stream Ranking"},
            {"name": "Agent 5", "role": "Current Signals", "tools": "News Monitoring, Trend Analysis"},
            {"name": "Agent 6", "role": "Due Diligence", "tools": "Risk Assessment, Question Generation"},
            {"name": "Agent 7", "role": "Memo Composer", "tools": "Content Synthesis, Formatting"}
        ]
        agent_deep_dive_keys = [
            None,
            "Agent 1 - Company Research",
            "Agent 2 - Peer Benchmark",
            "Agent 3 - Operating Model",
            "Agent 4 - AI Value",
            "Agent 5 - Current Signals",
            "Agent 6 - Due Diligence",
            "Agent 7 - Memo Composer"
        ]
        cols = st.columns(4)
        for i, agent in enumerate(agents):
            with cols[i % 4]:
                st.markdown(f"<div style='background: linear-gradient(135deg, #1E1E2E, #252540); border-radius: 12px; padding: 24px; text-align: center; border: 2px solid #00D4FF; margin: 10px;'><h3 style='color:#00D4FF; margin:0;'>{agent['name']}</h3><p style='color:#E2E8F0; margin-top:10px;'>{agent['role']}</p><p style='color:#9CA3AF; margin-top:5px;'>{agent['tools']}</p><p style='color:#10B981; margin-top:5px;'>Completed</p></div>", unsafe_allow_html=True)
                if i < len(agent_deep_dive_keys) and agent_deep_dive_keys[i]:
                    if st.button("View Details →", key=f"agent_btn_{i}", use_container_width=True):
                        st.session_state.page = "Agent Deep Dive"
                        st.session_state.selected_agent = agent_deep_dive_keys[i]
                        st.session_state.nav_override = True
                        st.rerun()
                else:
                    st.markdown('<div style="height:38px;"></div>', unsafe_allow_html=True)
        st.markdown("## INFRASTRUCTURE")
        infra = [
            {"name": "Tools", "desc": "Web Search, File Reading, Data Processing"},
            {"name": "Knowledge", "desc": "SEC Filings, Reports, Transcripts"},
            {"name": "Files", "desc": "Generated Analysis Outputs"}
        ]
        cols = st.columns(3)
        for i, item in enumerate(infra):
            with cols[i]:
                st.markdown(f"<div style='background: linear-gradient(135deg, #1E1E2E, #252540); border-radius: 12px; padding: 24px; text-align: center; border: 2px solid #10B981; margin: 10px;'><h3 style='color:#10B981; margin:0;'>{item['name']}</h3><p style='color:#9CA3AF; margin-top:10px;'>{item['desc']}</p></div>", unsafe_allow_html=True)
        st.markdown("## GOVERNANCE AND LEARNING")
        gov = [
            {"name": "Memory", "desc": "Quality Standards and Best Practices"},
            {"name": "Evaluator", "desc": "11 Quality Checks for Outputs"},
            {"name": "Skills", "desc": "8 Specialized Command Sets"},
            {"name": "Human Feedback", "desc": "Loop for Improvement"}
        ]
        cols = st.columns(4)
        for i, item in enumerate(gov):
            with cols[i]:
                st.markdown(f"<div style='background: linear-gradient(135deg, #1E1E2E, #252540); border-radius: 12px; padding: 24px; text-align: center; border: 2px solid #7C3AED; margin: 10px;'><h3 style='color:#7C3AED; margin:0;'>{item['name']}</h3><p style='color:#9CA3AF; margin-top:10px;'>{item['desc']}</p></div>", unsafe_allow_html=True)

    elif page == "Internal Pursuit Memo":
        original_content = read_file(base/"final_memo.md")
        if "CLIENT-FACING PREVIEW" in original_content:
            original_content = original_content.split("CLIENT-FACING PREVIEW")[0]
        
        content = original_content  # Copy for processing
        
        # Find and process executive summary section
        exec_start = content.find("## 0. EXECUTIVE SUMMARY")
        exec_end = content.find("## 1.", exec_start)
        if exec_end == -1:
            exec_end = len(content)
        
        before_exec = content[:exec_start]
        exec_section = content[exec_start:exec_end]
        after_exec = content[exec_end:]
        
        # Process table in exec_section
        import re
        table_pattern = r'\| Agent \| Role \| Top 3 Findings \|\n\|---\|---\|---\|\n((?:\|.*?\|\n)+)'
        table_match = re.search(table_pattern, exec_section, re.MULTILINE)
        if table_match:
            table_content = table_match.group(1)
            rows = [row.strip('|').split('|') for row in table_content.strip().split('\n') if row.strip()]
            cards_html = '<div style="display: flex; flex-wrap: wrap; gap: 20px; margin: 20px 0;">'
            for row in rows:
                if len(row) >= 3:
                    agent, role, findings = row[0].strip(), row[1].strip(), row[2].strip()
                    findings_list = [f.strip() for f in findings.split('•') if f.strip()]
                    card_html = f'''
<div style="background: linear-gradient(135deg, #1E1E2E, #252540); border: 2px solid #00D4FF; border-radius: 12px; padding: 20px; flex: 1; min-width: 300px;">
<h3 style="color: #00D4FF; margin: 0 0 10px 0;">{agent}</h3>
<p style="color: #E2E8F0; margin: 0 0 15px 0; font-weight: bold;">{role}</p>
<ul style="color: #9CA3AF; margin: 0; padding-left: 20px;">
'''
                    for finding in findings_list[:3]:  # Limit to 3
                        card_html += f'<li style="margin-bottom: 8px; line-height: 1.4;">{finding}</li>'
                    card_html += '</ul></div>'
                    cards_html += card_html
            cards_html += '</div>'
            exec_section = exec_section.replace(table_match.group(0), cards_html)
        
        # Render before exec summary
        st.markdown(before_exec)
        
        # Render exec summary with HTML
        st.markdown(exec_section, unsafe_allow_html=True)
        
        # Now process the rest (after_exec) with charts
        content = after_exec
        
        # Hardcoded chart data
        peers_data = {
            'Company': ['adidas', 'Nike', 'PUMA', 'On Running', 'Lululemon', 'Deckers', 'Anta Sports', 'ASICS', 'Under Armour'],
            'Revenue': [24.8, 46.3, 8.8, 3.0, 10.6, 5.0, 9.2, 4.1, 5.2],
            'Gross_Margin': [51.0, 40.6, 47.4, 62.8, 59.2, 57.9, 63.4, 55.8, 47.9],
            'Operating_Margin': [8.3, 5.8, 7.1, 12.5, 23.7, 23.7, 26.3, 14.7, 3.8]
        }
        
        spider_data = {
            'categories': ['Gross Margin', 'Operating Margin', 'Revenue Growth', 'SG&A Efficiency', 'DTC Penetration', 'Rev/Employee'],
            'adidas': [46, 20, 15, 47, 23, 23],
            'peer_average': [61, 48, 35, 62, 21, 42],
            'best_in_class': [100, 100, 100, 100, 100, 100]
        }
        
        heatmap_data = [
            [46, 20, 15, 47, 23, 23],  # adidas
            [0, 9, 9, 97, 22, 58],     # Nike
            [30, 15, 15, 62, 4, 32],   # PUMA
            [97, 39, 100, 19, 24, 100], # On Running
            [82, 88, 36, 81, 100, 0],  # Lululemon
            [76, 88, 42, 100, 7, 77],  # Deckers
            [100, 100, 36, 83, 0, 23], # Anta Sports
            [67, 48, 42, 57, 14, 39],  # ASICS
            [32, 0, 0, 0, 0, 7]        # Under Armour
        ]
        
        diverging_data = {
            'SC Area': ['Procurement', 'Demand Planning', 'Warehousing', 'Inbound Transport', 'Outbound Transport', 'Transport Planning', 'Freight Audit', 'Returns'],
            'Score': [1, 1, 0.5, 1, 1, 1, 1, 1]  # 1 for BRAIN, 0.5 for mixed
        }
        
        # Find insertion positions
        peer_pos = content.find("## 3. WHAT WE BELIEVE MATTERS MOST")
        supply_pos = content.find("## 5. OTHER OPPORTUNITIES")
        body_pos = content.find("## 7. REINFORCING AND CHALLENGING MANAGEMENT STRATEGY")
        
        # Split content
        part1 = content[:peer_pos]
        part2 = content[peer_pos:supply_pos]
        part3 = content[supply_pos:body_pos]
        part4 = content[body_pos:]
        
        # Display part1
        st.markdown(part1)
        
        # Peer Visual Comparison
        st.subheader("Peer Visual Comparison")
        
        # Spider chart
        fig3 = go.Figure()
        fig3.add_trace(go.Scatterpolar(
            r=spider_data['adidas'],
            theta=spider_data['categories'],
            fill='toself',
            name='adidas',
            line_color='#00D4FF'
        ))
        fig3.add_trace(go.Scatterpolar(
            r=spider_data['peer_average'],
            theta=spider_data['categories'],
            fill='toself',
            name='Peer Average',
            line_color='#7C3AED'
        ))
        fig3.add_trace(go.Scatterpolar(
            r=spider_data['best_in_class'],
            theta=spider_data['categories'],
            fill='toself',
            name='Best-in-Class',
            line_color='#10B981'
        ))
        fig3.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title='Competitive Position Spider Chart',
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white'
        )
        st.plotly_chart(fig3)
        
        # Horizontal bar chart: Peer Revenue
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=peers_data['Revenue'],
            y=peers_data['Company'],
            orientation='h',
            marker_color='#00D4FF',
            name='Revenue (B)'
        ))
        fig1.update_layout(
            title='Peer Revenue Comparison (Billions)',
            xaxis_title='Revenue (B)',
            yaxis_title='Company',
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white',
            showlegend=False
        )
        st.plotly_chart(fig1)
        
        # Grouped bar chart: Margins
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=peers_data['Company'],
            y=peers_data['Gross_Margin'],
            name='Gross Margin (%)',
            marker_color='#00D4FF'
        ))
        fig2.add_trace(go.Bar(
            x=peers_data['Company'],
            y=peers_data['Operating_Margin'],
            name='Operating Margin (%)',
            marker_color='#7C3AED'
        ))
        fig2.update_layout(
            title='Peer Margins Comparison',
            xaxis_title='Company',
            yaxis_title='Margin (%)',
            barmode='group',
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white'
        )
        st.plotly_chart(fig2)
        
        # Display part2
        st.markdown(part2)
        
        # Opportunity Heatmap
        st.subheader("Opportunity Heatmap")
        
        # Heatmap
        fig4 = go.Figure(data=go.Heatmap(
            z=heatmap_data,
            x=spider_data['categories'],
            y=peers_data['Company'],
            colorscale='Blues'
        ))
        fig4.update_layout(
            title='Peer Performance Heatmap',
            xaxis_title='Metrics',
            yaxis_title='Company',
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white'
        )
        st.plotly_chart(fig4)
        
        # Display part3
        st.markdown(part3)
        
        # Body vs Brain Diagnosis
        st.subheader("Body vs Brain Diagnosis")
        
        # Diverging bar chart
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            x=diverging_data['Score'],
            y=diverging_data['SC Area'],
            orientation='h',
            marker_color=['#00D4FF' if s == 1 else '#7C3AED' for s in diverging_data['Score']],
            name='Bottleneck Type'
        ))
        fig5.update_layout(
            title='Body vs Brain Diagnosis',
            xaxis_title='Score (1=BRAIN, 0.5=Mixed)',
            yaxis_title='SC Area',
            paper_bgcolor='#0E1117',
            plot_bgcolor='#0E1117',
            font_color='white',
            showlegend=False
        )
        st.plotly_chart(fig5)
        
        # Display part4
        st.markdown(part4)
        
        st.download_button("Download Memo", original_content, file_name=f"{company}_memo.md")

    elif page == "Client Preview":
        content = read_file(base/"final_memo.md")
        if "CLIENT-FACING PREVIEW" in content:
            parts = content.split("CLIENT-FACING PREVIEW")
            if len(parts) > 1:
                st.markdown(parts[1])
                st.download_button("Download", parts[1], file_name=f"{company}_client.md")
        else:
            st.markdown("Client preview not found.")

    elif page == "Agent Deep Dive":
        af = {"Agent 1 - Company Research": ["company_snapshot.md","management_roadmap.md","sector_context.md"],"Agent 2 - Peer Benchmark": ["peer_set.md","benchmark_table.md"],"Agent 3 - Operating Model": ["tech_ops_footprint.md","transformation_capacity.md"],"Agent 4 - AI Value": ["value_levers.md","stream_ranking.md","body_brain_diagnosis.md","moat_analysis.md"],"Agent 5 - Current Signals": ["current_signals.md"],"Agent 6 - Due Diligence": ["due_diligence.md","discovery_questions.md"],"Agent 7 - Memo Composer": ["final_memo.md","visuals_data.md"]}
        agent_keys = list(af.keys())
        default_agent = st.session_state.get('selected_agent', agent_keys[0])
        if default_agent not in agent_keys:
            default_agent = agent_keys[0]
        sel = st.selectbox("Select Agent", agent_keys, index=agent_keys.index(default_agent))
        st.session_state.selected_agent = sel
        for f in af[sel]:
            with st.expander(f, expanded=True):
                st.markdown(read_file(base/f))

    elif page == "Sources":
        gate = read_file(base/"source_gate_report.md")
        if "PASS" in gate: st.success("Source Gate: PASS")
        elif "PARTIAL" in gate: st.warning("Source Gate: PARTIAL")
        elif "FAIL" in gate: st.error("Source Gate: FAIL")
        st.markdown(gate)
        if (base/"sources"/"source_index.md").exists():
            st.markdown(read_file(base/"sources"/"source_index.md"))
else:
    st.markdown("# No analysis found")
