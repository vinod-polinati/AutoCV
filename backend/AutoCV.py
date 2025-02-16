import os
from fpdf import FPDF
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def collect_input():
    job_description = input("Enter the job description: ")
    company_name = input("Enter company name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email address: ")
    name = input("Enter your name: ")

    has_experience = input("Do you have any previous internship or full-time experience? (yes/no): ").strip().lower()
    if has_experience == "yes":
        experience = input("Describe your past experience: ")
    else:
        experience = None  # No experience

    university = input("Enter your college or university: ")
    degree = input("Enter your degree: ")
    major = input("Enter your major: ")

    return job_description, company_name, name, email, phone, experience, university, degree, major

def generate_cover_letter(job_description, company_name, user_name, email, phone, experience, uni_name, degree, major):
    experience_text = f"With my experience in {experience}" if experience else "With my experience in this field"
    
    cover_letter = f"""
Dear Hiring Manager at {company_name},

I am excited to apply for this position at {company_name}. {experience_text} and my educational background in {degree} with a major in {major} from {uni_name}, I am confident in my ability to contribute to your team.

The job description mentions {job_description}, which aligns with my skills and expertise. My past experiences have prepared me to excel in this role.

I am eager to bring my knowledge and skills to {company_name}. Please feel free to contact me at {phone} or {email} to discuss this opportunity further.

Sincerely,  
{user_name}
    """
    return cover_letter.strip()

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, text.encode('latin-1', 'replace').decode('latin-1'))
    pdf.output(filename)

if __name__ == "__main__":
    job_description, company_name, name, email, phone, experience, university, degree, major = collect_input()
    
    if job_description and company_name and name:
        cover_letter = generate_cover_letter(job_description, company_name, name, email, phone, experience, university, degree, major)
        print("\nGenerated Cover Letter:\n")
        print(cover_letter)

        # Create PDF
        create_pdf(cover_letter, "cover_letter.pdf")
        print("\nCover Letter saved as 'cover_letter.pdf'")
    else:
        print("Please provide all required inputs.")
