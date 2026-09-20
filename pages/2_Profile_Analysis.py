import streamlit as st

st.set_page_config(
    page_title="EduPath - Profile Analysis",
    page_icon="📊"
)

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

st.title("📊 EduPath Profile Analysis")
st.write("Analyze your skills and build your career learning path.")

name = st.text_input("👤 Your Name")
role = st.selectbox("🎯 Career Role", list(CAREERS.keys()))
goal = st.text_area("💡 Career Goal")

resume = st.text_area(
    "📄 Paste Resume Text",
    placeholder="Paste your resume text here..."
)

if st.button("🚀 Analyze My Profile", use_container_width=True):

    if not name or not goal or not resume:
        st.error("Please enter your name, career goal and resume text.")
        st.stop()

    text = resume.lower()
    required = CAREERS[role]

    found = [skill for skill in required if skill.lower() in text]
    missing = [skill for skill in required if skill.lower() not in text]

    st.success("✅ Profile analyzed successfully!")

    st.header("📊 Analysis Result")

    a, b, c = st.columns(3)

    a.metric("Career", role)
    b.metric("Skills Found", len(found))

    percentage = int(len(found) / len(required) * 100)
    c.metric("Skill Match", f"{percentage}%")

    st.subheader("✅ Skills Found")
    st.write(", ".join(found) if found else "No matching skills found.")

    st.subheader("🔍 Skill Gap")

    if missing:
        for skill in missing:
            st.warning(f"📚 {skill}")
    else:
        st.success("🎉 No major skill gap!")

    st.header("🗺️ Learning Roadmap")

    for skill in missing:
        st.markdown(f"**📌 {skill}**")

        topics = TOPICS.get(
            skill,
            ["Learn fundamentals", "Practice", "Build a project"]
        )

        for i, topic in enumerate(topics):
            st.checkbox(
                topic,
                key=f"road_{skill}_{i}"
            )

    st.header("📅 Weekly Plan")

    week = [
        "Monday — Learn",
        "Tuesday — Practice",
        "Wednesday — Learn",
        "Thursday — Problems",
        "Friday — Practical Work",
        "Saturday — Project",
        "Sunday — Revision"
    ]

    done = 0

    for day in week:
        if st.checkbox(day):
            done += 1

    st.progress(done / 7)
    st.write(f"**{done}/7 tasks completed — {done * 100 // 7}%**")

    st.header("💻 Project Suggestions")

    projects = [
        "Personal Portfolio",
        "Resume Analyzer",
        "Student Management System",
        "Career Recommendation System"
    ]

    for project in projects:
        st.write("•", project)

    st.header("🎤 Interview Preparation")

    questions = [
        "Tell me about yourself.",
        "Why did you choose this career?",
        "What are your technical skills?",
        "Explain one of your projects.",
        "What are your career goals?"
    ]

    question = st.selectbox("📝 Interview Question", questions)
    st.info(question)

    answer = st.text_area("✍️ Your Answer")

    if st.button("Check Answer"):
        if answer.strip():
            st.success("✅ Answer recorded.")
        else:
            st.warning("Please write your answer.")

    st.header("🤖 EduPath Offline AI Assistant")

    user_question = st.text_input(
        "💬 Ask AI",
        placeholder="Example: Give me a roadmap"
    )

    if st.button("🤖 Ask AI"):

        q = user_question.lower().strip()

        if not q:
            st.warning("Please enter a question.")

        elif "roadmap" in q or "career" in q:
            st.write(
                f"🎯 **{role} Roadmap**\n\n"
                "1. Learn fundamentals\n"
                "2. Improve missing skills\n"
                "3. Build projects\n"
                "4. Create GitHub portfolio\n"
                "5. Prepare for interviews"
            )

        elif "skill" in q:
            st.write(
                "🧠 Skills to improve: "
                + (", ".join(missing) if missing else "None")
            )

        elif "project" in q:
            st.write(
                "💻 Try a Portfolio, Resume Analyzer, "
                "Student Management System or Career Recommendation System."
            )

        elif "interview" in q:
            st.write(
                "🎤 Practice your introduction, projects, "
                "technical skills and career goals."
            )

        else:
            st.write(
                f"🤖 Focus on {role}, improve your skills, "
                "build projects and prepare for interviews."
            )
