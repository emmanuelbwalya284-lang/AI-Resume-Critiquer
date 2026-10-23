import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="@", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your particular needs!")

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

upload_file = st.file_uploader("upload your resume (PDF OR TXT)", type= ["pdf","txt"])
job_role = st.text_input("Enter the particular job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file. read().decode("utf-8")

if analyze and upload_file:
    try:
        file_content = extract_text_from_file(upload_file)

        if not file_content.strip():
            st.error("file does not have any content...")
            st.stop()

        prompt = f"""please analyze this resumer and provide construct feedback.
        focus on the following aspects:
        1. content clarity impact
        2. skills presentation
        3.experience descriptions
        4. specific improvements for {job_role if job_role else 'general job applications'}  

        Resumer content:
        {file_content} 

        please provide your analysis in a clear, structured format with specific recommendations."""

                # ... (Your prompt variable is above this)

        # --- REPLACE FROM HERE ---
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        client = OpenAI(
            api_key=GEMINI_API_KEY, 
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        
        response = client.chat.completions.create( 
            model="gemini-2.5-flash", 
            messages=[
                {"role":"system", "content": "you are an expert resume reviewer with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=4000
        
        )
        st.markdown("### Analysis Results") 
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occured:{str(e)}")




            





