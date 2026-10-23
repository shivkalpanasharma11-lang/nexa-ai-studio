import streamlit as st, re
st.set_page_config(page_title="Nexa AI Studio",page_icon="✦",layout="wide")
KB=[
("Programming","Python","python","""# Python, explained\nPython is a readable, general-purpose language used for automation, web apps, data analysis, AI, and scripting.\n\n### Core concepts\n- **Variables:** `name = "Nexa"` stores a value.\n- **Conditions:** `if score >= 50:` makes decisions.\n- **Loops:** `for item in items:` repeats work.\n- **Functions:** `def greet(name):` packages reusable logic.\n- **Collections:** lists, dictionaries, tuples, and sets store data.\n\n```python\ndef greet(name):\n    return f"Hello, {name}!"\nprint(greet("Nexa"))\n```\n\nLearn by building small projects: a calculator, quiz, expense tracker, then a web app. Practise a little every day and learn to debug errors."""),
("Deployment","Deploy Streamlit","deploy streamlit cloud publish host public link","""# Deploy your Streamlit app\n1. Put `app.py` and `requirements.txt` in a GitHub repository.\n2. Open [Streamlit Community Cloud](https://share.streamlit.io/).\n3. Connect GitHub, select your repository, branch, and `app.py`.\n4. Click **Deploy** and wait for the build logs to finish.\n5. Share the generated `*.streamlit.app` URL.\n\nKeep passwords and API keys out of GitHub. If deployment fails, check the logs and make sure every dependency is listed in `requirements.txt`. This Nexa demo does not need an API key."""),
("Career","Interview preparation","interview placement hr round","""# Prepare for an interview\n- Research the company, role, product, and required skills.\n- Prepare stories using **STAR**: Situation, Task, Action, Result.\n- Practise “Tell me about yourself”, “Why this role?”, and explaining a project you built.\n- For technical interviews, clarify assumptions, explain your approach, test edge cases, and discuss trade-offs.\n- Prepare thoughtful questions for the interviewer and check your setup the day before.\n\nA good closing question: “What would success look like in the first 90 days?”"""),
("Learning","Study effectively","study studying exam learn faster concentration","""# Study effectively\n- **Active recall:** close the book and explain the concept from memory.\n- **Spaced repetition:** revisit material over increasing intervals.\n- **Practice questions:** use mistakes to identify gaps.\n- **Focused sessions:** try 25 minutes of work and a 5-minute break.\n- **Protect sleep** and keep your phone out of reach.\n\n### One-hour session\n5 min plan → 20 min learn → 20 min solve questions → 10 min review mistakes → 5 min plan the next session."""),
("Technology","Cybersecurity","cybersecurity security phishing password hacking","""# Cybersecurity basics\n- Use unique passwords and a password manager.\n- Enable multi-factor authentication.\n- Update your operating system, browser, and apps.\n- Verify suspicious links and urgent payment requests through another channel.\n- Back up important files and test recovery.\n- Never share one-time passwords.\n\nOrganisations also need access controls, monitoring, incident response, and tested backups."""),
("Projects","College project ideas","college project final year mini project idea","""# College project ideas\n**Beginner:** expense tracker, quiz app, study planner.\n\n**Intermediate:** campus lost-and-found, job application tracker, inventory dashboard.\n\n**Advanced:** accessibility checker, document search/Q&A prototype, energy-use dashboard.\n\nTo stand out, define the problem, show a working demo, include sample data, document limitations, and explain what you personally built. A finished simple project beats an unfinished ambitious one."""),
("Productivity","Beat procrastination","procrastination focus productivity time management","""# Beat procrastination\n1. Turn a big task into a tiny next action.\n2. Promise yourself just five minutes to begin.\n3. Prepare the files and tools before starting.\n4. Choose one priority before checking messages.\n5. Track completed steps, not just hours.\n\nTry this now: write one action that takes under ten minutes, set a timer, and start."""),
("Business","Business plan","business plan startup business idea market research","""# A simple business plan\n1. **Problem:** what need do you solve?\n2. **Customer:** who has this problem?\n3. **Solution:** what will you offer?\n4. **Competition:** what do people use today?\n5. **Revenue:** how will you earn and what will it cost?\n6. **Validation:** interview potential customers and test a small prototype.\n7. **Milestones:** choose evidence to collect over the next month.\n\nLabel assumptions clearly; real customer feedback is more useful than guesses."""),
("Finance","Budgeting basics","budget saving personal finance money","""# Budgeting basics\nTrack income, fixed costs, variable spending, debt, and savings. Review a month of spending, set realistic goals, automate savings if possible, and review recurring subscriptions. The popular 50/30/20 split is only a starting point; adapt it to your circumstances. This is general education, not personal financial advice."""),
("Web Development","HTML CSS JavaScript","html css javascript website frontend","""# HTML, CSS and JavaScript\n- **HTML** defines page structure and content.\n- **CSS** styles layout, spacing, colours, and responsive design.\n- **JavaScript** adds interaction and dynamic behaviour.\n\n```html\n<h1>Hello world</h1>\n<button onclick="alert('Hello!')">Click me</button>\n```\n\nSave as `index.html` and open it in a browser. For bigger projects, separate files and use browser developer tools."""),
("AI","Artificial intelligence","ai artificial intelligence machine learning chatbot llm","""# Artificial intelligence\nAI is a broad field of systems performing tasks such as recognising patterns, understanding language, planning, and prediction.\n- **Machine learning:** learns patterns from examples.\n- **Deep learning:** uses multi-layer neural networks.\n- **Generative AI:** creates text, images, code, and more.\n\nAI can make confident mistakes or reflect bias. Verify important claims and avoid sharing private data with tools unless you understand their privacy terms."""),
("Programming","Debug a Python error","error bug debug traceback not working","""# Debug a Python error\n1. Read the last line of the traceback first.\n2. Check the file and line number shown.\n3. Inspect spelling, indentation, variable names, and data types.\n4. Reduce the issue to a small reproducible example.\n5. Fix one thing at a time and rerun.\n\nCommon errors: `SyntaxError` (invalid syntax), `NameError` (undefined name), `TypeError` (wrong type), `ModuleNotFoundError` (missing package), and `FileNotFoundError` (wrong path). Paste the full traceback for specific help."""),
("Deployment","Git and GitHub","git github repository push code","""# Git and GitHub\nGit tracks file changes; GitHub hosts repositories online.\n```bash\ngit init\ngit add .\ngit commit -m "Initial commit"\n```\nCreate a repository on GitHub, then follow its instructions to connect and push your local folder. Use `.gitignore`, make meaningful commits, document setup in a README, and never commit secrets.""")
]
WELCOME="""Welcome to **Nexa AI Studio** ✨\n\nI’m a lightweight, no-API demo assistant. Ask about programming, deployment, interviews, studying, cybersecurity, projects, productivity, business, finance, web development, or AI.\n\n**Try:** “Explain Python in detail” or “How do I deploy a Streamlit app?”"""
def norm(s): return re.sub(r"[^a-z0-9\s]"," ",s.lower()).strip()
def reply(q):
    nq=norm(q); words=set(nq.split()); best=None; bs=0
    for cat,title,keys,ans in KB:
        score=0
        for k in [title]+keys.split():
            nk=norm(k)
            if nk and nk in nq: score+=5+len(nk.split())
            score+=len(set(nk.split())&words)*.6
        if score>bs: best,bs=ans,score
    if best and bs>=2.2:return best
    if any(x in nq for x in ["hello","hi","hey","namaste"]):return "Hey! 👋 What would you like help with? Try Python, web development, AI, projects, deployment, studying, or interviews."
    if "thank" in nq:return "You’re welcome! 😊 Ask a follow-up any time."
    return "I don’t have a prepared article for that exact question yet, but the chat is working. Try asking about **Python**, **AI**, **HTML/CSS/JavaScript**, **cybersecurity**, **college project ideas**, **interviews**, **study techniques**, **GitHub**, or **Streamlit deployment**. This version uses a curated knowledge base, not a live AI model."
if "theme" not in st.session_state: st.session_state.theme="Light"
if "messages" not in st.session_state: st.session_state.messages=[{"role":"assistant","content":WELCOME}]
if "history" not in st.session_state: st.session_state.history=[]
with st.sidebar:
    st.markdown("<h1>✦ Nexa<span style='color:#8873ff'>AI</span></h1><small>STUDIO · NO API REQUIRED</small>",unsafe_allow_html=True)
    st.markdown("---")
    theme=st.radio("Appearance",["Light","Dark"],horizontal=True,index=0 if st.session_state.theme=="Light" else 1)
    if theme!=st.session_state.theme: st.session_state.theme=theme; st.rerun()
    if st.button("＋ New conversation",use_container_width=True,type="primary"):
        st.session_state.messages=[{"role":"assistant","content":WELCOME}]; st.rerun()
    st.markdown("### Explore by topic")
    cats=["All topics"]+sorted(set(x[0] for x in KB))
    cat=st.selectbox("Choose category",cats)
    for i,(c,title,keys,ans) in enumerate(KB):
        if (cat=="All topics" or cat==c) and st.button("✧  "+title,key=f"topic{i}",use_container_width=True):
            st.session_state.messages.extend([{"role":"user","content":"Explain "+title},{"role":"assistant","content":ans}]); st.rerun()
    st.markdown("---")
    st.caption("Recent questions")
    for q in st.session_state.history[-5:]: st.caption("◌ "+q[:34])
    export="\n\n".join(("You: " if m["role"]=="user" else "Nexa: ")+m["content"] for m in st.session_state.messages)
    st.download_button("⬇ Export chat as TXT",export,file_name="nexa_conversation.txt",mime="text/plain",use_container_width=True)
dark=st.session_state.theme=="Dark"
bg,panel,fg,muted,border,inputbg=("#101323","#191e33","#f4f5ff","#aeb7d2","#303954","#1c2238") if dark else ("#f5f7ff","#ffffff","#202747","#727c9b","#e0e5f5","#ffffff")
st.markdown(f"""<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{{font-family:'DM Sans',sans-serif}}
.stApp{{background:radial-gradient(ellipse at 80% 0%,{'#25264a' if dark else '#e4eaff'} 0%,{bg} 50%);color:{fg}}}
[data-testid="stSidebar"]{{background:{panel};border-right:1px solid {border}}}
[data-testid="stSidebar"] *{{color:{fg}}}
.block-container{{max-width:1200px;padding-top:1.3rem}}
.hero{{padding:25px 28px;border:1px solid {border};border-radius:24px;background:linear-gradient(115deg,{panel},{'#222344' if dark else '#edf5ff'});margin-bottom:20px;box-shadow:0 14px 42px #4856a00c}}
.eyebrow{{color:#8873ff;font-size:11px;font-weight:800;letter-spacing:2px;text-transform:uppercase}}
.hero h1{{font-size:clamp(32px,4vw,46px);line-height:1.12;letter-spacing:-1.5px;margin:8px 0;color:{fg}}}
.hero p{{color:{muted};margin:0}}
.pill{{display:inline-block;padding:7px 11px;border:1px solid {border};border-radius:99px;background:{panel};color:{muted};font-size:11px;font-weight:700;margin:13px 5px 0 0}}
div[data-testid="stChatMessage"]{{border:1px solid {border};border-radius:18px;padding:14px 17px;background:{panel};margin-bottom:12px}}
div[data-testid="stChatMessage"] p,div[data-testid="stChatMessage"] li{{color:{fg};line-height:1.7}}
[data-testid="stChatInput"]{{border:1px solid {border}!important;border-radius:18px!important;background:{inputbg}!important;box-shadow:0 10px 35px #39436b12!important}}
[data-testid="stChatInput"] textarea{{color:{fg}!important}}
.stButton>button{{border-radius:12px;border:1px solid {border};min-height:42px;font-weight:600}}
.stButton>button:hover{{border-color:#8873ff;color:#8873ff}}
button[kind="primary"]{{background:linear-gradient(100deg,#7866f6,#4ebfe8)!important;border:0!important;color:white!important}}
footer{{visibility:hidden}}
</style>""",unsafe_allow_html=True)
st.markdown("""<div class="hero"><div class="eyebrow">✦ Your personal knowledge studio</div><h1>Ideas in. <span style="color:#8873ff">Clarity out.</span></h1><p>A clean, fast assistant for learning, building projects, and getting unstuck.</p><span class="pill">✧ No API key</span><span class="pill">⚡ Curated answers</span><span class="pill">◐ Light & dark themes</span></div>""",unsafe_allow_html=True)
st.markdown("### Chat with Nexa")
st.caption("Offline demo assistant · prepared answers, no live AI model")
if len(st.session_state.messages)==1:
    prompts=["Explain Python in detail","How do I deploy a Streamlit app?","How do I prepare for an interview?","Explain cybersecurity","Suggest college project ideas","How can I study effectively?"]
    cols=st.columns(3)
    for i,p in enumerate(prompts):
        with cols[i%3]:
            if st.button(["💻 ","🚀 ","🎯 ","🛡️ ","💡 ","🧠 "][i]+p,key="start"+str(i),use_container_width=True):
                st.session_state.messages.extend([{"role":"user","content":p},{"role":"assistant","content":reply(p)}]);st.session_state.history.append(p);st.rerun()
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
prompt=st.chat_input("Ask Nexa anything… try “explain Python” or “deploy my app”")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt});st.session_state.history.append(prompt)
    st.session_state.messages.append({"role":"assistant","content":reply(prompt)});st.rerun()
st.markdown(f"<p style='text-align:center;color:{muted};font-size:11px;margin-top:22px'>Nexa AI Studio · Built with Streamlit · No API calls</p>",unsafe_allow_html=True)
