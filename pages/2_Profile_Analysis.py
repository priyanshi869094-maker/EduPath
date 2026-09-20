import streamlit as st

st.set_page_config(
    page_title="EduPath - Profile Analysis",
    page_icon="📊"
)

# ================= CAREERS =================

CAREERS = {
    "Software Engineer": ["Python", "C++", "Java", "DSA", "SQL", "Git"],
    "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "Backend Developer": ["Python", "Java", "SQL", "APIs", "Git"],
    "Data Scientist": ["Python", "SQL", "Statistics", "Data Science", "Machine Learning"],
    "Data Analyst": ["Python", "SQL", "Statistics", "Data Analysis", "Excel"],
    "AI Engineer": ["Python", "AI", "Machine Learning", "Deep Learning"],
    "Cybersecurity Analyst": ["Python", "Linux", "Networking", "Cybersecurity"],
    "Cloud Engineer": ["Python", "Linux", "Networking", "Cloud"],
    "DevOps Engineer": ["Python", "Linux", "Git", "Docker", "Cloud"],
    "Electrical Engineer": ["C", "Python", "Electrical Engineering"],
    "Electronics Engineer": ["C", "C++", "Electronics", "Microcontrollers"],
    "Robotics Engineer": ["Python", "C++", "Robotics", "AI"],
    "UI/UX Designer": ["UI/UX Design", "Figma", "Communication"]
}

TOPICS = {
    "Python": ["Basics", "Functions", "OOP", "Projects"],
    "C": ["Basics", "Arrays", "Pointers", "Structures"],
    "C++": ["OOP", "STL", "DSA", "Projects"],
    "Java": ["OOP", "Collections", "Projects"],
    "HTML": ["Basics", "Forms", "Semantic HTML"],
    "CSS": ["Selectors", "Flexbox", "Grid"],
    "JavaScript": ["Basics", "DOM", "ES6"],
    "SQL": ["SELECT", "JOIN", "GROUP BY"],
    "DSA": ["Arrays", "Linked List", "Stack", "Queue", "Trees"],
    "Machine Learning": ["Regression", "Classification", "Evaluation"],
    "AI": ["AI Basics", "Search", "Applications"],
    "Git": ["Repository", "Commit", "Branch", "Merge"]
}

# ================= HEADER =================

st.title("📊 EduPath Profile Analysis")
st.write("Analyze your profile and build your career learning path.")

# ================= PROFILE =================

name = st.text_input("👤 Your Name")

role = st.selectbox(
    "🎯 Career Role",
    list(CAREERS.keys())
)

goal = st.text_area(
    "💡 Career Goal",
    placeholder="Example: I want to become a software engineer."
)

resume = st.text_area(
    "📄 Paste Resume Text",
    placeholder="Paste your resume text here..."
)

# ================= ANALYSIS =================

if st.button("🚀 Analyze My Profile", use_container_width=True):

    if not name or not goal or not resume:
        st.error("Please enter your name, career goal and resume text.")
        st.stop()

    text = resume.lower()

    required = CAREERS[role]

    found = [
        skill for skill in required
        if skill.lower() in text
    ]

    missing = [
        skill for skill in required
        if skill.lower() not in text
    ]

    st.session_state["found"] = found
    st.session_state["missing"] = missing
    st.session_state["role"] = role
    st.session_state["analyzed"] = True


# ================= RESULTS =================

if st.session_state.get("analyzed", False):

    found = st.session_state["found"]
    missing = st.session_state["missing"]
    role = st.session_state["role"]

    st.success("✅ Profile analyzed successfully!")

    st.header("📊 Analysis Result")

    a, b, c = st.columns(3)

    a.metric("Career", role)
    b.metric("Skills Found", len(found))

    total = len(CAREERS[role])
    percentage = int(len(found) / total * 100)

    c.metric("Skill Match", f"{percentage}%")

    # ================= SKILLS =================

    st.subheader("✅ Skills Found")

    if found:
        st.write(", ".join(found))
    else:
        st.info("No matching skills detected.")

    # ================= SKILL GAP =================

    st.subheader("🔍 Skill Gap")

    if missing:

        for skill in missing:
            st.warning(f"📚 {skill}")

    else:
        st.success("🎉 No major skill gap!")

    # ================= ROADMAP =================

    st.header("🗺️ Learning Roadmap")

    for skill in missing:

        st.markdown(f"### 📌 {skill}")

        topics = TOPICS.get(
            skill,
            [
                "Learn fundamentals",
                "Practice",
                "Build a project"
            ]
        )

        for i, topic in enumerate(topics):

            st.checkbox(
                topic,
                key=f"road_{skill}_{i}"
            )

    # ================= WEEKLY PLAN =================

    st.header("📅 Weekly Study Plan")

    week = [
        ("Monday", "Learn a new concept"),
        ("Tuesday", "Practice questions"),
        ("Wednesday", "Learn next topic"),
        ("Thursday", "Solve problems"),
        ("Friday", "Practical task"),
        ("Saturday", "Build a mini project"),
        ("Sunday", "Revision")
    ]

    completed = 0

    for day, task in week:

        key = f"week_{day}"

        if st.checkbox(
            f"{day} — {task}",
            key=key
        ):
            completed += 1

    # ================= PROGRESS =================

    st.header("📈 Weekly Progress")

    progress = completed / len(week)

    st.progress(progress)

    st.write(
        f"**{completed}/{len(week)} tasks completed — "
        f"{int(progress * 100)}%**"
    )

    if progress == 1:
        st.success("🎉 Weekly plan completed!")

    elif progress > 0:
        st.info("🔥 Keep going! You are making progress.")

    else:
        st.info("📚 Start completing your weekly tasks.")

    # ================= PROJECTS =================

    st.header("💻 Project Suggestions")

    projects = [
        "Personal Portfolio",
        "Resume Analyzer",
        "Student Management System",
        "Career Recommendation System",
        "Learning Progress Dashboard"
    ]

    for project in projects:
        st.write("•", project)

    # ================= INTERVIEW =================

    st.header("🎤 Interview Preparation")

    questions = [
        "Tell me about yourself.",
        "Why did you choose this career?",
        "What are your strongest technical skills?",
        "Explain one of your projects.",
        "What challenges did you face?",
        "What are your career goals?",
        "Where do you see yourself in five years?"
    ]

    selected_question = st.selectbox(
        "📝 Select an interview question",
        questions
    )

    st.info(selected_question)

    answer = st.text_area(
        "✍️ Write your answer"
    )

    if st.button("Check Answer", key="check_answer"):

        if answer.strip():
            st.success("✅ Answer recorded. Keep it clear and specific.")

        else:
            st.warning("Please write your answer first.")

    # ================= OFFLINE AI =================

    st.header("🤖 EduPath Offline AI Assistant")

    st.write(
        "Ask basic questions about careers, skills, study plans "
        "and interviews."
    )

    user_question = st.text_input(
        "💬 Ask AI",
        placeholder="Example: What is Python?"
    )

    if st.button("🤖 Ask AI", key="offline_ai"):

        q = user_question.lower().strip()

        if not q:

            st.warning("Please enter a question.")

        elif "what is python" in q or "python" == q:

            st.write(
                "🐍 **Python** is a beginner-friendly programming "
                "language used for web development, automation, "
                "data science, AI and machine learning."
            )

        elif "what is c" in q:

            st.write(
                "💻 **C** is a powerful programming language used "
                "for system programming, embedded systems and "
                "learning programming fundamentals."
            )

        elif "what is ai" in q or "artificial intelligence" in q:

            st.write(
                "🤖 **Artificial Intelligence (AI)** is the field "
                "of creating systems that can perform tasks that "
                "normally require human intelligence."
            )

        elif "what is machine learning" in q:

            st.write(
                "🧠 **Machine Learning** is a branch of AI where "
                "computers learn patterns from data and use them "
                "to make predictions or decisions."
            )

        elif "what is dsa" in q:

            st.write(
                "📚 **DSA** means Data Structures and Algorithms. "
                "It helps you store, organize and process data "
                "efficiently."
            )

        elif "what is sql" in q:

            st.write(
                "🗄️ **SQL** is a language used to store, retrieve "
                "and manage data in relational databases."
            )

        elif "what is git" in q:

            st.write(
                "🔧 **Git** is a version-control system used to "
                "track code changes and collaborate on software projects."
            )

        elif "roadmap" in q or "career path" in q:

            st.write(
                f"🎯 **{role} Roadmap**\n\n"
                "1. Learn fundamentals\n"
                "2. Improve missing skills\n"
                "3. Practice regularly\n"
                "4. Build projects\n"
                "5. Create a GitHub portfolio\n"
                "6. Prepare for interviews"
            )

        elif "study plan" in q or "weekly plan" in q:

            st.write(
                "📅 **Weekly Study Plan**\n\n"
                "Monday — Learn\n"
                "Tuesday — Practice\n"
                "Wednesday — Learn\n"
                "Thursday — Solve problems\n"
                "Friday — Practical work\n"
                "Saturday — Project\n"
                "Sunday — Revision"
            )

        elif "skill" in q or "skills" in q:

            st.write(
                "🧠 **Skills to improve:** "
                + (
                    ", ".join(missing)
                    if missing
                    else "No major skill gaps detected."
                )
            )

        elif "project" in q:

            st.write(
                "💻 You can build a Personal Portfolio, "
                "Resume Analyzer, Student Management System "
                "or Career Recommendation System."
            )

        elif "interview" in q:

            st.write(
                "🎤 For interviews, practice your introduction, "
                "technical skills, projects, strengths, "
                "weaknesses and career goals."
            )

        elif "software engineer" in q:

            st.write(
                "👨‍💻 For Software Engineering, focus on "
                "Python/C++/Java, DSA, SQL, Git and projects."
            )

        elif "how to study" in q:

            st.write(
                "📚 Study regularly, understand concepts first, "
                "practice problems, build small projects and "
                "revise what you learned."
            )

        else:

            st.write(
                f"🤖 I am your offline EduPath assistant. "
                f"For **{role}**, focus on your missing skills, "
                "practice regularly, build projects and prepare "
                "for interviews."
            )
