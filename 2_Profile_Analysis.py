import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="EduPath - Profile Analysis", page_icon="📊")

# ---------- DATA ----------
CAREERS = {
    "Software Engineer":["Python","C++","Java","DSA","SQL","Git"],
    "Frontend Developer":["HTML","CSS","JavaScript","React","Git"],
    "Backend Developer":["Python","Java","SQL","APIs","Git"],
    "Full Stack Developer":["HTML","CSS","JavaScript","React","Python","SQL"],
    "Web Developer":["HTML","CSS","JavaScript","React"],
    "Mobile App Developer":["Java","Kotlin","Flutter","Git"],
    "Data Scientist":["Python","SQL","Statistics","Data Science","Machine Learning"],
    "Data Analyst":["Python","SQL","Statistics","Data Analysis","Excel"],
    "Machine Learning Engineer":["Python","Machine Learning","Deep Learning","SQL"],
    "AI Engineer":["Python","AI","Machine Learning","Deep Learning"],
    "Cybersecurity Analyst":["Python","Linux","Networking","Cybersecurity"],
    "Cloud Engineer":["Python","Linux","Networking","Cloud"],
    "DevOps Engineer":["Python","Linux","Git","Docker","Cloud","CI/CD"],
    "Database Administrator":["SQL","Database Management","Python","Linux"],
    "Software Tester":["Python","Java","SQL","Testing"],
    "Embedded Systems Engineer":["C","C++","Microcontrollers","Embedded Systems"],
    "Electrical Engineer":["C","Python","Electrical Engineering"],
    "Electronics Engineer":["C","C++","Electronics","Microcontrollers"],
    "Robotics Engineer":["Python","C++","Robotics","AI","Machine Learning"],
    "Game Developer":["C++","C#","Unity","Game Development"],
    "Blockchain Developer":["Python","JavaScript","Blockchain","Cryptography"],
    "UI/UX Designer":["UI/UX Design","Figma","Communication"],
    "Product Manager":["Product Management","Communication","Leadership"],
    "Business Analyst":["SQL","Data Analysis","Excel","Communication"],
    "Network Engineer":["Networking","Linux","Python","Cybersecurity"],
}

TOPICS = {
    "Python":["Basics","Functions","OOP","Projects"],
    "C":["Basics","Arrays","Pointers","Structures"],
    "C++":["OOP","STL","DSA","Projects"],
    "Java":["OOP","Collections","Exception Handling"],
    "JavaScript":["Basics","DOM","Events","ES6"],
    "HTML":["Basics","Forms","Semantic HTML"],
    "CSS":["Selectors","Flexbox","Grid","Responsive Design"],
    "React":["Components","Props","State","Hooks"],
    "SQL":["SELECT","JOIN","GROUP BY","Subqueries"],
    "DSA":["Arrays","Linked List","Stack","Queue","Trees"],
    "Machine Learning":["Regression","Classification","Evaluation"],
    "Deep Learning":["Neural Networks","CNN","Training"],
    "AI":["AI Basics","Search","Applications"],
    "Data Science":["Cleaning","Statistics","Visualization"],
    "Statistics":["Probability","Distributions","Correlation"],
    "Git":["Repository","Commit","Branch","Merge"],
}

# ---------- HEADER ----------
st.title("📊 EduPath Profile Analysis")
st.write("Analyze your profile, identify skill gaps and build your learning path.")

# ---------- PROFILE ----------
c1, c2 = st.columns(2)

with c1:
    name = st.text_input("👤 Your Name")

with c2:
    role = st.selectbox("🎯 Career Role", list(CAREERS.keys()))

goal = st.text_area(
    "💡 Career Goal",
    placeholder="Example: I want to become a software engineer."
)

resume = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# ---------- ANALYSIS ----------
if st.button("🚀 Analyze My Profile", use_container_width=True):

    if not name or not goal or not resume:
        st.error("Please enter your name, career goal and upload your resume.")
        st.stop()

    try:
        reader = PdfReader(resume)
        text = " ".join(
            page.extract_text() or "" for page in reader.pages
        ).lower()

        found = [
            skill for skill in set(
                x for skills in CAREERS.values() for x in skills
            )
            if skill.lower() in text
        ]

        required = CAREERS[role]
        missing = [
            skill for skill in required
            if skill.lower() not in [x.lower() for x in found]
        ]

        st.session_state.found = found
        st.session_state.missing = missing
        st.session_state.role = role
        st.session_state.analyzed = True

        st.success("✅ Profile analyzed successfully!")

    except Exception as e:
        st.error(f"❌ Resume analysis failed: {e}")


# ---------- RESULTS ----------
if st.session_state.get("analyzed", False):

    found = st.session_state.found
    missing = st.session_state.missing
    role = st.session_state.role

    st.divider()
    st.header("📊 Analysis Result")

    a, b, c = st.columns(3)

    with a:
        st.metric("Career", role)

    with b:
        st.metric("Skills Found", len(found))

    with c:
        total = len(CAREERS[role])
        match = total - len(missing)
        percentage = int(match / total * 100) if total else 0
        st.metric("Skill Match", f"{percentage}%")

    # ---------- SKILLS ----------
    st.subheader("✅ Skills Found")

    if found:
        st.write(", ".join(found))
    else:
        st.info("No matching skills detected.")

    # ---------- SKILL GAP ----------
    st.subheader("🔍 Skill Gap")

    if missing:
        for skill in missing:
            st.warning(f"📚 {skill}")
    else:
        st.success("🎉 No major skill gap found!")

    # ---------- ROADMAP ----------
    st.header("🗺️ Learning Roadmap")

    for skill in missing:
        st.markdown(f"**📌 {skill}**")

        for i, topic in enumerate(
            TOPICS.get(
                skill,
                ["Learn fundamentals", "Practice", "Build a project"]
            )
        ):
            st.checkbox(
                topic,
                key=f"road_{skill}_{i}"
            )

    # ---------- WEEKLY PLAN ----------
    st.header("📅 Weekly Plan")

    week = [
        ("Monday", "Learn a new concept"),
        ("Tuesday", "Practice questions"),
        ("Wednesday", "Learn next topic"),
        ("Thursday", "Solve problems"),
        ("Friday", "Practical task"),
        ("Saturday", "Build a mini project"),
        ("Sunday", "Revision")
    ]

    done = 0

    for day, task in week:
        if st.checkbox(
            f"{day} — {task}",
            key=f"week_{day}"
        ):
            done += 1

    # ---------- PROGRESS ----------
    st.header("📈 Progress")

    progress = done / len(week)

    st.progress(progress)

    st.write(f"**{done}/{len(week)} tasks completed — {int(progress*100)}%**")

    if progress == 1:
        st.success("🎉 Weekly plan completed!")
    elif progress > 0:
        st.info("🔥 Keep going!")
    else:
        st.info("Select completed tasks to track progress.")

    # ---------- PROJECTS ----------
    st.header("💻 Project Suggestions")

    projects = [
        "Personal Portfolio",
        "Student Management System",
        "Career Recommendation System",
        "Resume Analyzer",
        "Learning Progress Dashboard"
    ]

    for project in projects:
        st.write("•", project)

    # ---------- INTERVIEW ----------
    st.header("🎤 Interview Preparation")

    questions = [
        "Tell me about yourself.",
        "Why did you choose this career?",
        "What are your strongest technical skills?",
        "Explain one of your projects.",
        "What challenges did you face?",
        "Why should we hire you?",
        "What are your career goals?",
        "Where do you see yourself in five years?"
    ]

    selected_question = st.selectbox(
        "📝 Select an interview question",
        questions
    )

    st.info(selected_question)

    answer = st.text_area(
        "✍️ Write your answer",
        height=120
    )

    if st.button("Check Answer", key="check_answer"):
        if answer.strip():
            st.success("✅ Answer recorded. Keep it clear and specific.")
        else:
            st.warning("Please write your answer first.")

    # ---------- OFFLINE AI ----------
    st.header("🤖 EduPath Offline AI Assistant")

    question = st.text_area(
        "💬 Ask AI",
        placeholder="Example: How can I become a software engineer?",
        height=100
    )

    if st.button("🤖 Ask AI", key="ask_ai"):

        q = question.lower().strip()

        if not q:
            st.warning("Please enter a question.")

        elif "roadmap" in q or "career path" in q:

            st.write(
                f"🎯 **{role} Roadmap**\n\n"
                "1. Learn fundamentals.\n"
                "2. Improve missing skills.\n"
                "3. Build projects.\n"
                "4. Create a GitHub portfolio.\n"
                "5. Prepare for interviews.\n"
                "6. Apply for internships/jobs."
            )

        elif "study plan" in q or "weekly plan" in q:

            st.write(
                "📚 **Weekly Study Plan**\n\n"
                "Monday — Learn\n"
                "Tuesday — Practice\n"
                "Wednesday — Learn\n"
                "Thursday — Problems\n"
                "Friday — Practical work\n"
                "Saturday — Project\n"
                "Sunday — Revision"
            )

        elif "skill" in q:

            st.write(
                f"🧠 **Skills to improve:** "
                f"{', '.join(missing) if missing else 'None'}"
            )

        elif "project" in q:

            st.write(
                "💻 Try building a Portfolio, "
                "Resume Analyzer, Student Management System "
                "or Career Recommendation System."
            )

        elif "interview" in q or "placement" in q:

            st.write(
                "🎤 Practice your introduction, "
                "projects, technical skills, strengths, "
                "weaknesses and career goals."
            )

        else:

            st.write(
                f"🤖 Based on your profile, focus on "
                f"**{role}**, improve your missing skills, "
                "build projects and prepare for interviews."
            )