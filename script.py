from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai
import pypdf

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# extract data from the PDF file. 
def extract_text_from_pdf(uploaded_file):
    resume_text = ""
    with open(uploaded_file, 'rb') as file:
        pdf_reader = pypdf.PdfFileReader(file)
        num_pages = pdf_reader.numPages
        for page_number in range(num_pages):
            page = pdf_reader.getPage(page_number)
            ressume_text += page.extractText()
    return resume_text

# PDF-text file setup
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = pypdf.PdfFileReader(uploaded_file)
        
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        
        paragraphs = text.split('\n\n')  # You may need to adjust the splitting logic based on your PDF content
        
        return paragraphs
    else:
        raise FileNotFoundError("No file uploaded")



# Provide the path to your PDF file
pdf_file_path = "your_resume.pdf"
resume_text = extract_text_from_pdf(pdf_file_path)
print(resume_text)



# generate response from the model
def get_gemini_response(input_text, resume_content, job_description):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_text, resume_content, job_description])
    return response.text



## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
You are an experienced HR director with years of experience in Data Science, Full stack web development, DevOps, ML, AI, NLP, GenAI and every other major tech stack out there. You have been assigned the task of assisting a new junior HR with recruiting a new candidate.
Keep in mind that hiring the right candidate for this role is crucial for the company and selection of the wrong candidate might put your job in danger! Due to this reason, be brutally honest in your opinion, be it positive or negative.
You will be given the job description of the position you are recruiting for. Match the information you get from the candidate's resume against the job description provided to you. 

In your response, firstly include the candidate's name. 

Then, give a brief, honest and brutal breakdown of the candidate's strength's and weakensses. After that, give a summary on what you think about the candidate's fit for the role. Should he be hired or rejected? 
Keep in mind that your job is only to assist the junior HR in making a decision. You will not contact the candiate or talk to them in any form whatsoever. 
"""

input_prompt3 = """
You are an experienced HR director with years of experience in Data Science, Full stack web development, DevOps, ML, AI, NLP, GenAI and every other major tech stack out there. You have been assigned the task of assisting a new junior HR with recruiting a new candidate.
Keep in mind that hiring the right candidate for this role is crucial for the company and selection of the wrong candidate might put your job in danger! Due to this reason, be brutally honest in your opinion, be it positive or negative.
You will be given the job description of the position you are recruiting for. Match the information you get from the candidate's resume against the job description provided to you. 

In your response, firstly include the candidate's name. 

Then, give a percentage match of the candidate for the given role. Then, mention the keywords from the job description that are missing in the candidate's resume. 
Mention which tasks from the job description, or tasks that are relevant to the opening position can the candidate perform well. Also include tasks that the candidate would struggle with.
After that, give a summary on what you think about the candidate's fit for the role. Should he be hired or rejected? 

Keep in mind that your job is only to assist the junior HR in making a decision. You will not contact the candiate or talk to them in any form whatsoever.  
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        # st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        # st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")
