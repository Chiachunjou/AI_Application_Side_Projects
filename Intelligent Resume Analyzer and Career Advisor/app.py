# Library
from langchain_openai import OpenAI
import langchain
import streamlit as st
from dotenv import load_dotenv
from utils import *


def main():
    load_dotenv()
    # Frontend
    st.set_page_config("Resume Analysis Assistance")
    st.title("Intelligent Resume Analyzer and Career Advisor🤖")
    st.subheader("Upload your resume and I will provide suggestions to improve!")
    # Input
    position_pursue = st.text_input("Enter the name of job position or job description you pursue!")
    resume = st.file_uploader("Upload your resume here(PDF Only)",type=["pdf"],key="1")
    button = st.button("Analyze!")
    # Analysis
    if button:
        if position_pursue != None and resume != None:    
            with st.spinner("Analyzing..."):
                text = get_pdf_text(resume)
                response = suggestion(job_description=position_pursue,resume_text=text)
                st.subheader("Suggestions and Recommendations")
                st.write(response.choices[0].text)
                st.succes("")
        else:
            st.error("Please upload a PDF file or enter job description")

# Init
if __name__ == "__main__":
    main()

    