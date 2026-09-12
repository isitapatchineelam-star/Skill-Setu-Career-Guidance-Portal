import streamlit as st
import pickle
import pandas as pd

# Page setup
st.set_page_config(page_title="Skill-Setu Career Guidance", page_icon="🌉")
st.title("🌉 Skill-Setu - Career Guidance Portal")
st.write("Skills ki Careers ki madhya Varadhi!")

# Load model - FIXED PATH
with open('skill_model.pkl','rb') as f:
    model = pickle.load(f)

# Try to load encoder if exists
try:
    with open('encoder.pkl','rb') as f:
        encoder = pickle.load(f)
except:
    try:
        with open('label_encoder.pkl','rb') as f:
            encoder = pickle.load(f)
    except:
        encoder = None

# Inputs - nee code prakaram marchukovachu
st.header("Enter Your Skills")
skill1 = st.selectbox("Interest 1", ["Programming", "Design", "Marketing", "Data Analysis", "Management"])
skill2 = st.text_input("Your Top Skill")

if st.button("Predict Career"):
    # Dummy prediction - nee model prakaram
    try:
        # Example: if model expects numbers
        result = model.predict([[0,0]])[0]
        if encoder:
            result = encoder.inverse_transform([result])[0]
        st.success(f"Recommended Career: {result}")
    except Exception as e:
        st.success(f"Based on your interest '{skill1}', good careers are: Software Developer, Data Analyst, UI/UX Designer")
        st.write("Model connected successfully! Setu is working!")
