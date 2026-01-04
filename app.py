import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Guidance Agent",
    page_icon="🎓",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🎓 AI Career Guidance & Skill Recommendation Agent")
st.subheader("SDG 8 – Decent Work and Economic Growth")

st.markdown("""
This advanced AI-based system analyzes **multiple skills across all streams**
to recommend **career paths, skill gaps, and learning directions**.
""")

st.divider()

# ---------------- INPUT SECTION ----------------
st.header("📋 Candidate Profile")

education = st.text_input(
    "🎓 Education / Stream",
    placeholder="BSc IT / BE / BCom / BA / MSc / Diploma"
)

skills = st.text_area(
    "💡 Skills (comma separated)",
    placeholder="Python, Java, HTML, SQL, Excel, Communication, Accounting"
)

interest = st.selectbox(
    "🎯 Primary Career Interest",
    [
        "Technology & Software",
        "Data & Analytics",
        "Business & Commerce",
        "Design & Creative",
        "Teaching & Research",
        "Not Sure"
    ]
)

experience = st.slider(
    "📊 Years of Experience",
    0, 15, 0
)

# ---------------- AI LOGIC ----------------
if st.button("🔍 Generate Career Guidance"):

    if skills.strip() == "":
        st.warning("⚠️ Please enter at least one skill.")
    else:
        skills_list = [s.strip().lower() for s in skills.split(",")]

        careers = set()
        skill_gap = set()
        domain = set()

        for skill in skills_list:

            # ---------- PROGRAMMING ----------
            if skill in ["python", "java", "c", "c++"]:
                domain.add("Software Engineering")
                careers.update([
                    "Software Developer",
                    "Backend Developer",
                    "Application Engineer"
                ])
                skill_gap.update([
                    "Data Structures",
                    "Algorithms",
                    "Git & GitHub"
                ])

            # ---------- WEB ----------
            if skill in ["html", "css", "javascript", "bootstrap"]:
                domain.add("Web Development")
                careers.update([
                    "Frontend Developer",
                    "Full Stack Developer",
                    "UI Developer"
                ])
                skill_gap.update([
                    "React",
                    "Node.js",
                    "REST APIs"
                ])

            # ---------- DATA ----------
            if skill in ["sql", "excel", "power bi", "tableau"]:
                domain.add("Data & Analytics")
                careers.update([
                    "Data Analyst",
                    "Business Analyst",
                    "MIS Executive"
                ])
                skill_gap.update([
                    "Advanced SQL",
                    "Data Visualization",
                    "Statistics"
                ])

            # ---------- AI / ML ----------
            if skill in ["machine learning", "ai", "deep learning"]:
                domain.add("AI & Machine Learning")
                careers.update([
                    "ML Engineer",
                    "AI Engineer",
                    "Research Analyst"
                ])
                skill_gap.update([
                    "Python Libraries",
                    "Model Deployment",
                    "Mathematics"
                ])

            # ---------- COMMERCE ----------
            if skill in ["accounting", "tally", "gst", "taxation"]:
                domain.add("Commerce & Finance")
                careers.update([
                    "Accountant",
                    "Tax Consultant",
                    "Finance Executive"
                ])
                skill_gap.update([
                    "Financial Analysis",
                    "Compliance Knowledge",
                    "Excel Automation"
                ])

            # ---------- MANAGEMENT ----------
            if skill in ["management", "leadership", "planning"]:
                domain.add("Management")
                careers.update([
                    "Project Manager",
                    "Operations Manager",
                    "Business Manager"
                ])
                skill_gap.update([
                    "Agile Methodology",
                    "People Management",
                    "Strategic Planning"
                ])

            # ---------- COMMUNICATION ----------
            if skill in ["communication", "presentation", "public speaking"]:
                domain.add("Professional Skills")
                careers.update([
                    "HR Executive",
                    "Trainer",
                    "Corporate Relations Officer"
                ])
                skill_gap.update([
                    "Negotiation Skills",
                    "Interview Skills"
                ])

            # ---------- DESIGN ----------
            if skill in ["photoshop", "figma", "ui/ux", "graphic design"]:
                domain.add("Design & Creative")
                careers.update([
                    "UI/UX Designer",
                    "Graphic Designer",
                    "Product Designer"
                ])
                skill_gap.update([
                    "Design Thinking",
                    "User Research",
                    "Portfolio Building"
                ])

            # ---------- TEACHING ----------
            if skill in ["teaching", "training", "research"]:
                domain.add("Education & Research")
                careers.update([
                    "Teacher",
                    "Academic Trainer",
                    "Research Assistant"
                ])
                skill_gap.update([
                    "Curriculum Design",
                    "Assessment Methods",
                    "Digital Teaching Tools"
                ])

        # ---------- DEFAULT ----------
        if not careers:
            careers.add("Entry-Level Professional")
            skill_gap.update([
                "Basic Computer Skills",
                "Communication",
                "Problem Solving"
            ])

        # ---------------- OUTPUT ----------------
        st.success("✅ AI Career Analysis Completed")

        st.subheader("📌 Career Guidance Report")

        st.write("🎓 **Education:**", education if education else "Not specified")
        st.write("📊 **Experience:**", f"{experience} years")

        st.write("🧭 **Identified Domains:**")
        st.markdown("- " + "\n- ".join(domain))

        st.write("💼 **Recommended Career Paths:**")
        st.markdown("- " + "\n- ".join(careers))

        st.write("📚 **Skill Gap – What to Learn Next:**")
        st.markdown("- " + "\n- ".join(skill_gap))

        st.write("🏫 **Recommended Platform:** IBM SkillsBuild")

        st.info("""
        📈 **SDG 8 Impact**
        - Improves employability across multiple sectors  
        - Encourages skill-based economic growth  
        - Supports decent work opportunities
        """)

# ---------------- FOOTER ----------------
st.divider()
st.caption("CSRBOX – IBM SkillsBuild Applied AI Internship 2025")
