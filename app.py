import streamlit as st
import pickle

with open('/content/skill_model.pkl','rb') as f:
    model = pickle.load(f)
with open('/content/vectorizer.pkl','rb') as f:
    vectorizer = pickle.load(f)

st.set_page_config(page_title="Skill-Setu", page_icon="💼")
st.title("💼 Skill-Setu - Career Guidance Portal")
st.write("Enter your skills and get the best career recommendation based on current market trends!")

skill_input = st.text_input("Enter Your Skills (e.g., Python, Video Editing, Graphic Design)")

if st.button("Find My Best Job"):
    if skill_input:
        job = model.predict(vectorizer.transform([skill_input]))[0]
        st.balloons()
        st.success(f"✅ Recommended Career for you: **{job}** 🚀")
        st.info("This recommendation is based on 2026 trending job market data.")
    else:
        st.warning("Please enter your skills first!")

st.markdown("---")
st.caption("Developed for Kaikaluru Rural Youth | Project: Skill-Setu")
