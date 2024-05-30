# Library
from langchain_openai import OpenAI
from pypdf import PdfReader
import openai
# get text in pdf
def get_pdf_text(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text = text + page.extract_text()
    return text
# Call OpenAI to analyze the resume and provide suggestion
def suggestion(job_description,resume_text):
    # Prompt
    prompt = f"""
    Job Description or the name of job position: {job_description}
    Resume: {resume_text}
    Analyze the resume based on the job description and provide detailed suggestions for improvement. Include the following:
    - Highlight missing or weak skills.
    - Provide examples of better phrasing or formatting.
    - Suggest additional qualifications or certifications.
    - Identify key skills the user needs to learn or improve.
    - Recommend relevant courses, certifications, or resources for skill enhancement.
    """
    # 
    response = openai.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = prompt,
        max_tokens=1500,
        temperature = 0.5
    )
    return response
    

    
