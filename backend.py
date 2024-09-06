import os
from groq import Groq
from fpdf import FPDF
from dotenv import load_dotenv

load_dotenv()
def collect_input():
    job_description = input("Enter the job description: ")
    company_name = input("Enter company name:")
    
    phone = input("Enter your 10-digit phone number: ")
    while len(phone) != 10 or not phone.isdigit():
        phone = input("Enter your 10-digit phone number: ")
        
    mail = input("Enter your email address (must end with .com): ")
    while not mail.endswith(".com") or "@" not in mail:
        mail = input("Enter your email address (must end with .com): ")
        
    user_details = {
        'name': input("Enter your name: "),
        'email': mail,
        'mobile number': phone,
        'experience': input("Enter your experience: ")
    }
    
    education ={
        'university': input("college or university"),
        'degree': input("Enter your degree: "),
        'major': input("Enter your major: "),
    }
    return job_description, user_details, company_name, education

def generate_cover_letter(job_description, user_details, company_name, education):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("LPU lang process unit failed will be live soon!")
    
    client = Groq(api_key=api_key)
    prompt = f"Generate a cover letter for the following job description: {job_description} and my details: {user_details} and my education {education} and company name: {company_name} dont add [Recipient’s Name],[Recipient’s Title],[Company Address],[City, State, ZIP] start with dear hiring manager and give my name mail and number at the end "
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

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
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
    
def main():
    job_description, user_details, company_name, university = collect_input()
    cover_letter = generate_cover_letter(job_description, user_details, company_name, university)
    print("Generated Cover Letter:\n")
    print(cover_letter)
    create_pdf(cover_letter, "cover_letter.pdf")
    print("Cover letter generated and saved as cover_letter.pdf")

if __name__ == '__main__':
    main()