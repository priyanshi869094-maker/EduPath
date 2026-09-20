import streamlit as st

home = st.Page(
    "app.py",
    title="Home",
    icon="🏠",
    url_path="home"
)

careers = st.Page(
    "pages/1_Explore_Careers.py",
    title="Explore Careers",
    icon="💼",
    url_path="careers"
)

profile = st.Page(
    "pages/2_Profile_Analysis.py",
    title="Profile Analysis",
    icon="📄",
    url_path="profile-analysis"
)

pg = st.navigation({
    "EduPath": [
        home,
        careers,
        profile
    ]
})

pg.run()