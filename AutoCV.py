import os
import streamlit as st
from fpdf import FPDF
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

def collect_input():
    st.title("Cover Letter Generator")

    # Collect inputs from the user
    job_description = st.text_area("Enter the job description:")
    company_name = st.text_input("Enter company name:")

    phone = st.text_input("Enter your phone number:")

    mail = st.text_input("Enter your email address:")

    name = st.text_input("Enter your name:")
    experience = st.text_area("Enter your experience:")
    
    education = {
        'university': st.text_input("Enter your college or university:"),
        'degree': st.text_input("Enter your degree:"),
        'major': st.text_input("Enter your major:")
    }

    user_details = {
        'name': name,
        'email': mail,
        'mobile number': phone,
        'experience': experience
    }

    return job_description, user_details, company_name, education

def generate_cover_letter(job_description, user_details, company_name, education):
    api_key = "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" 
    if not api_key:
        st.error("Key not found in environment variables.")
        return ""

    client = Groq(api_key=api_key)
    prompt = f"Generate a cover letter for the following job description give me onlu the cover letter no other text at the end or starting: {job_description} and my details: {user_details} and my education {education} and company name: {company_name} start with dear hiring manager and add all my details and use name mail and number from the details "
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating cover letter: {e}")
        return ""

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    
    # Set font size dynamically based on text length
    text_length = len(text)
    if text_length > 2000:
        font_size = 10
    elif text_length > 1500:
        font_size = 12
    else:
        font_size = 14

    pdf.set_font("Arial", size=font_size)
    pdf.multi_cell(0, 5, text.encode('latin-1', 'replace').decode('latin-1'))
    pdf.output(filename)

# Streamlit app main logic
job_description, user_details, company_name, education = collect_input()

if st.button("Generate Cover Letter"):
    if job_description and user_details and company_name and education:
        cover_letter = generate_cover_letter(job_description, user_details, company_name, education)
        if cover_letter:
            st.success("Cover letter generated successfully!")
            st.text_area("Generated Cover Letter:", cover_letter, height=300)
            
            # Create PDF
            create_pdf(cover_letter, "cover_letter.pdf")
            with open("cover_letter.pdf", "rb") as file:
                st.download_button("Download PDF", file, file_name="cover_letter.pdf")
    else:
        st.error("Please fill in all fields before generating the cover letter.")
