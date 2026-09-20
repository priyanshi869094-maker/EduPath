import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="EduPath",
    page_icon="🎓",
    layout="wide"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background-color: #f7f9fc;
}

.hero {
    background: linear-gradient(135deg, #172554, #2563eb);
    padding: 55px;
    border-radius: 25px;
    color: white;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 52px;
}

.hero p {
    font-size: 20px;
    color: #dbeafe;
}

.section-title {
    font-size: 30px;
    font-weight: 700;
    color: #172554;
    margin-top: 35px;
    margin-bottom: 20px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 5px 18px rgba(0,0,0,0.05);
    min-height: 170px;
}

.card h3 {
    color: #172554;
}

.card p {
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown("## 🎓 EduPath")

    st.write(
        "AI-Powered Personalized Learning Platform"
    )

    st.divider()

    st.markdown("### Navigation")

    if st.button(
        "🏠 Home",
        use_container_width=True,
        key="home_button"
    ):
        st.switch_page("app.py")

    if st.button(
        "💼 Explore Careers",
        use_container_width=True,
        key="careers_button"
    ):
        st.switch_page(
            "pages/1_Explore_Careers.py"
        )


# ---------------- HERO ----------------

st.markdown("""
<div class="hero">

<h1>🎓 EduPath</h1>

<p>
Build the skills your dream career demands.
</p>

<p>
Discover your skill gaps, create a learning roadmap,
and track your learning progress.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- MAIN BUTTONS ----------------

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "💼 Explore Careers",
        use_container_width=True,
        key="main_careers"
    ):

        st.switch_page(
            "pages/1_Explore_Careers.py"
        )


with col2:

    if st.button(
        "🚀 Analyze My Resume",
        use_container_width=True,
        key="main_resume"
    ):

        st.info(
            "Resume Analysis page will be connected next."
        )


# ---------------- POPULAR CAREERS ----------------

st.markdown(
    '<div class="section-title">🔥 Popular Career Paths</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

career_data = [

    (
        "💻",
        "Software Engineer",
        "Programming • DSA • SQL"
    ),

    (
        "📊",
        "Data Scientist",
        "Python • SQL • Machine Learning"
    ),

    (
        "🤖",
        "ML Engineer",
        "AI • ML • Python"
    ),

    (
        "🌐",
        "Web Developer",
        "HTML • CSS • JavaScript"
    )
]

for col, data in zip(
    [col1, col2, col3, col4],
    career_data
):

    icon, title, description = data

    with col:

        st.markdown(
            f"""
            <div class="card">

            <h1>{icon}</h1>

            <h3>{title}</h3>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- HOW IT WORKS ----------------

st.markdown(
    '<div class="section-title">⚡ How EduPath Works</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

steps = [

    (
        "1️⃣",
        "Upload Resume",
        "Upload your resume and career information."
    ),

    (
        "2️⃣",
        "Analyze Skills",
        "Find the skills already present in your profile."
    ),

    (
        "3️⃣",
        "Find Skill Gaps",
        "Compare your skills with your target career."
    ),

    (
        "4️⃣",
        "Get Roadmap",
        "Follow a personalized learning roadmap."
    )
]

for col, step in zip(
    [col1, col2, col3, col4],
    steps
):

    icon, title, description = step

    with col:

        st.markdown(
            f"""
            <div class="card">

            <h1>{icon}</h1>

            <h3>{title}</h3>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        padding:25px;
        color:#64748b;
    ">

    <h3>🎓 EduPath</h3>

    <p>
    Learn Better • Plan Smarter • Grow Faster
    </p>

    </div>
    """,
    unsafe_allow_html=True
)