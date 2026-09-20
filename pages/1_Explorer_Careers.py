import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Explore Careers | EduPath",
    page_icon="💼",
    layout="wide"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: #f7f9fc;
}

.title {
    font-size: 45px;
    font-weight: 700;
    color: #172554;
}

.subtitle {
    font-size: 19px;
    color: #64748b;
}

.career-card {
    background-color: white;
    padding: 28px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    min-height: 300px;
    box-shadow: 0 5px 18px rgba(0,0,0,0.05);
}

.career-icon {
    font-size: 45px;
}

.career-title {
    font-size: 24px;
    font-weight: 700;
    color: #172554;
}

.description {
    color: #64748b;
    min-height: 70px;
}

.skill {
    display: inline-block;
    background-color: #dbeafe;
    color: #1d4ed8;
    padding: 6px 10px;
    border-radius: 12px;
    margin: 3px;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="title">💼 Explore Careers</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find a career path and discover the skills you need.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- SEARCH ----------------

search = st.text_input(
    "🔎 Search Career",
    placeholder="Example: Software Engineer"
)


# ---------------- CAREERS ----------------

careers = [

    {
        "icon": "💻",
        "name": "Software Engineer",
        "description":
        "Build software applications and solve programming problems.",
        "skills": [
            "Python",
            "C++",
            "Java",
            "Data Structures",
            "Algorithms",
            "SQL"
        ]
    },

    {
        "icon": "📊",
        "name": "Data Scientist",
        "description":
        "Use data, statistics and machine learning to solve problems.",
        "skills": [
            "Python",
            "SQL",
            "Data Science",
            "Machine Learning",
            "Statistics"
        ]
    },

    {
        "icon": "🤖",
        "name": "Machine Learning Engineer",
        "description":
        "Build intelligent systems using machine learning and AI.",
        "skills": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "Data Science",
            "SQL"
        ]
    },

    {
        "icon": "🌐",
        "name": "Web Developer",
        "description":
        "Create modern websites and interactive web applications.",
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git"
        ]
    },

    {
        "icon": "📱",
        "name": "App Developer",
        "description":
        "Design and develop applications for mobile platforms.",
        "skills": [
            "Java",
            "Kotlin",
            "UI/UX",
            "APIs",
            "Git"
        ]
    },

    {
        "icon": "☁️",
        "name": "Cloud Engineer",
        "description":
        "Work with cloud infrastructure and scalable systems.",
        "skills": [
            "Cloud",
            "Linux",
            "Networking",
            "Docker",
            "Git"
        ]
    }
]


# ---------------- FILTER CAREERS ----------------

filtered_careers = []

for career in careers:

    if search.strip() == "":
        filtered_careers.append(career)

    elif search.lower() in career["name"].lower():
        filtered_careers.append(career)


# ---------------- CAREER CARDS ----------------

st.markdown("## 🚀 Career Paths")

columns = st.columns(3)

for index, career in enumerate(filtered_careers):

    with columns[index % 3]:

        st.markdown(
            f"""
            <div class="career-card">

            <div class="career-icon">
                {career["icon"]}
            </div>

            <div class="career-title">
                {career["name"]}
            </div>

            <p class="description">
                {career["description"]}
            </p>

            <b>Core Skills</b>

            <div>
            """,
            unsafe_allow_html=True
        )

        for skill in career["skills"]:

            st.markdown(
                f"""
                <span class="skill">
                    {skill}
                </span>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            "</div></div>",
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            f"🎯 Select {career['name']}",
            key=f"select_career_{index}",
            use_container_width=True
        ):

            st.session_state["selected_career"] = \
                career["name"]

            st.success(
                f"Selected: {career['name']}"
            )


# ---------------- SELECTED CAREER ----------------

if "selected_career" in st.session_state:

    st.divider()

    st.success(
        "🎯 Selected Career: "
        + st.session_state["selected_career"]
    )

    st.info(
        "Profile Analysis will be connected here next."
    )