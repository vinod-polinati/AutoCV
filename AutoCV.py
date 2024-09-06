import os
import backend
from backend import generate_cover_letter,collect_input,create_pdf

def main():
    job_description, user_details, company_name, university = collect_input()
    cover_letter = generate_cover_letter(job_description, user_details, company_name, university)
    print("Generated Cover Letter:\n")
    print(cover_letter)
    create_pdf(cover_letter, "cover_letter.pdf")
    print("Cover letter generated and saved as cover_letter.pdf")