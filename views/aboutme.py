import streamlit as st
import st_tailwind as tw

# HERO Section
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image('./assets/moftfoto.png', width=200)
with col2:
    st.title("Mohammad Fattachul 'Alim", anchor=False)
    st.write("📍 East Java, Indonesia | 📧 mofttach@gmail.com | 🌐 [LinkedIn](https://linkedin.com/in/mofttach)")
    st.button("📄 Download CV")

# Summary Section
st.header("💼 Summary")
st.write("""
🎓 **Mohammad Fattachul 'Alim (Fattah)** is a 19-year-old Informatics student at Nahdlatul Ulama University of Yogyakarta, holding a cumulative GPA of 3.95/4.00. 
With a background in Computer and Network Engineering, he’s certified as a **Level 1 & 2 Technician of Hand-Held Products by Samsung** and as a **Junior Web Developer**. Fattah has a deep passion for **AI and Data Science**, actively exploring innovative solutions and previously secured **2nd place and the People’s Choice Award at the Samsung Innovation Campus**.
""")

# Education Section
st.header("🎓 Education")
st.write("**Universitas Nahdlatul Ulama Yogyakarta** — *Bachelor of Science in Informatics* (Cumulative GPA: 3.95/4.00)")
st.write("""
- **Clinic K2+ Peer Counselor**: Provided academic and emotional support, assisting fellow students in study strategies and mental well-being.
- **Lecturer’s Research Assistant**: Contributed to developing **DiFaMAP**, an Android-based application aiding students with deaf disabilities to avoid sexual violence, with a focus on accessibility features.
""")

# Experience Section
st.header("🧑‍💼 Work Experience")
st.write("#### Directorate Talent Dev & Academic Innovation Staff - Intern")
st.write("###### Sep 2024 - Oct 2024")
st.write("""
 - Be the youngest student that Intern in Rectorate 🌟
 - Assisted in organizing academic workshops and events to support student skill enhancement.
 - Engaged in program planning and execution to align university goals with student career development.
 - Provided research and administrative support to ensure smooth operations in talent development initiatives
""")
st.write("#### Dokter Laptop - Computer and Laptop Technician (Jan 2023 - May 2023)")
st.write("""
- 🖥 Diagnosed hardware/software issues, configured OS, and educated clients on maintenance practices.
""")
st.write("#### SMK Walisongo 2 Gempol - Toolman & Teacher Assistant (Aug 2020 - Jan 2022)")
st.write("""
- 🛠 Assisted in preparing laboratory equipment, performed network troubleshooting, and conducted basic computer classes.
""")

# Organizational Experience Section
st.header("🌐 Organizational Experience")
st.write("#### Python Conference Asia Pacific (PyCon APAC) 2024 - PIC of Event Division (Sep 2024 - Oct 2024)")
st.write("""
- Coordinated with **PythonID** for hosting, managed 80+ sessions with speakers from 13 countries.
""")
st.write("#### Informatics Student Association (HMP INF) - Vice Leader (Jul 2024 - Present)")
st.write("""
- Fostered partnerships with 5 tech communities, acted as PIC for the **Gen AI Tour Yogyakarta**.
""")
st.write("#### NU’s Student Association (IPNU) Jabon - General Vice Secretary (Nov 2022 - Present)")
st.write("""
- 📄 Managed 50+ organizational documents and handled 20+ official correspondences.
""")
st.write("#### NU’s Student Association (IPNU) SMK Walisongo 2 Gempol - Leader (Oct 2021 - Dec 2022)")
st.write("""
- Led the establishment of IPNU in school, fostering an Islamic cultural environment.
""")

# Awards and Achievements Section
st.header("🏆 Awards & Achievements")
st.write("""
- **2nd Winner Samsung Innovation Campus** (2024) 🥈
- **People’s Choice Award Samsung Innovation Campus** (2024) 🌟
- **School’s Delegate for IRC x RRO Robotic Competition by ITS** (2023) 🤖
- **School’s Delegate for National Robot Competition by Poltera** (2022) 🤖
""")

# Skills Section
st.header("🛠 Skills")
st.write("""
- **Programming Languages**: Python, JavaScript
- **Technologies**: Machine Learning, IoT, Data Analysis, Streamlit, Neo4j
- **Soft Skills**: Leadership, Event Management, Public Speaking, Team Collaboration
""")
#