import streamlit as st

st.set_page_config(page_title="EduPath Profile Analysis", page_icon="📊")

CAREERS = {
    "Software Engineer":["Python","C++","Java","DSA","SQL","Git"],
    "Frontend Developer":["HTML","CSS","JavaScript","React","Git"],
    "Backend Developer":["Python","Java","SQL","APIs","Git"],
    "Data Scientist":["Python","SQL","Statistics","Data Science","Machine Learning"],
    "Data Analyst":["Python","SQL","Statistics","Data Analysis","Excel"],
    "AI Engineer":["Python","AI","Machine Learning","Deep Learning"],
    "Cybersecurity Analyst":["Python","Linux","Networking","Cybersecurity"],
    "Cloud Engineer":["Python","Linux","Networking","Cloud"],
    "DevOps Engineer":["Python","Linux","Git","Docker","Cloud"],
    "Electrical Engineer":["C","Python","Electrical Engineering"],
    "Electronics Engineer":["C","C++","Electronics","Microcontrollers"],
    "Robotics Engineer":["Python","C++","Robotics","AI"],
    "UI/UX Designer":["UI/UX Design","Figma","Communication"]
}

TOPICS = {
    "Python":["Basics","Functions","OOP","Projects"],
    "C":["Basics","Arrays","Pointers","Structures"],
    "C++":["OOP","STL","DSA","Projects"],
    "Java":["OOP","Collections","Projects"],
    "HTML":["Basics","Forms","Semantic HTML"],
    "CSS":["Selectors","Flexbox","Grid"],
    "JavaScript":["Basics","DOM","ES6"],
    "SQL":["SELECT","JOIN","GROUP BY"],
    "DSA":["Arrays","Linked List","Stack","Queue","Trees"],
    "Machine Learning":["Regression","Classification","Evaluation"],
    "AI":["AI Basics","Search","Applications"],
    "Git":["Repository","Commit","Branch","Merge"]
}

st.title("📊 EduPath Profile Analysis")
st.write("Analyze your skills and create your career learning path.")

name = st.text_input("👤 Your Name")
role = st.selectbox("🎯 Career Role", list(CAREERS))
goal = st.text_area("💡 Career Goal")

resume_text = st.text_area(
    "📄 Paste your resume text",
    placeholder="Paste the text from your resume here..."
)

if st.button("🚀 Analyze My Profile", use_container_width=True):

    if not name or not goal or not resume_text:
        st.error("Please enter your name, goal and resume text.")
        st.stop()

    text = resume_text.lower()
    required = CAREERS[role]

    found = [s for s in required if s.lower() in text]
    missing = [s for s in required if s.lower() not in text]

    st.success("✅ Profile analyzed!")

    st.divider()
    st.header("📊 Analysis Result")

    a,b,c = st.columns(3)
    a.metric("Career", role)
    b.metric("Skills Found", len(found))

    match = len(found)
    percent = int(match / len(required) * 100)
    c.metric("Skill Match", f"{percent}%")

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
        for topic in TOPICS.get(skill, ["Learn fundamentals","Practice","Build project"]):
            st.checkbox(topic, key=f"{skill}_{topic}")

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

    done = sum(st.checkbox(x, key=x) for x in week)
    st.progress(done / 7)
    st.write(f"**{done}/7 tasks completed — {done*100//7}%**")

    st.header("💻 Project Suggestions")
    for p in ["Personal Portfolio","Resume Analyzer",
              "Student Management System","Career Recommendation System"]:
        st.write("•", p)

    st.header("🎤 Interview Preparation")
    questions = [
        "Tell me about yourself.",
        "Why did you choose this career?",
        "What are your technical skills?",
        "Explain your project.",
        "What are your career goals?"
    ]

    q = st.selectbox("📝 Interview Question", questions)
    st.info(q)

    answer = st.text_area("✍️ Your Answer")
    if st.button("Check Answer"):
        st.success("✅ Answer recorded.")

    st.header("🤖 EduPath Offline AI Assistant")

    question = st.text_input("💬 Ask AI")

    if st.button("🤖 Ask AI"):

        q = question.lower()

        if "roadmap" in q or "career" in q:
            st.write(
                f"🎯 **{role} Roadmap:** Learn fundamentals → "
                "Improve skills → Build projects → GitHub → Interviews."
            )

        elif "skill" in q:
            st.write(
                f"🧠 Improve: {', '.join(missing) if missing else 'No major gaps'}"
            )

        elif "project" in q:
            st.write(
                "💻 Build a Portfolio, Resume Analyzer or "
                "Career Recommendation System."
            )

        elif "interview" in q:
            st.write(
                "🎤 Practice introduction, projects, "
                "technical skills and career goals."
            )

        else:
            st.write(
                f"🤖 Focus on **{role}**, improve your skills, "
                "build projects and prepare for interviews."
            )
        else:
            st.write(
                f"🤖 Focus on **{role}**, improve your skills, "
                "build projects and prepare for interviews."
            )
