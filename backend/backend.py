from flask import Flask, request, jsonify, send_from_directory
from AutoCV import generate_cover_letter  
import os
from fpdf import FPDF
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

# Ensure the static folder exists for storing PDFs
if not os.path.exists("static"):
    os.makedirs("static")

@app.route('/')
def home():
    return "AI COVER LETTER GENERATOR"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    cover_letter = generate_cover_letter(
        job_description=data.get("job_description", ""),
        company_name=data.get("company_name", ""),
        user_name=data.get("user_name", ""),
        email=data.get("email", ""),
        phone=data.get("phone", ""),
        experience=data.get("experience", ""),
        uni_name=data.get("uni_name", ""),
        degree=data.get("degree", ""),
        major=data.get("major", "")
    )

    return jsonify({"cover_letter": cover_letter})

def create_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 5, text.encode('latin-1', 'replace').decode('latin-1'))
    pdf.output(filename)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json()
    text = data.get("cover_letter", "")
    filename = "cover_letter.pdf"  # Filename only, no directory
    
    create_pdf(text, os.path.join("static", filename))
    
    response = send_from_directory(directory="static", filename=filename, as_attachment=True)
    response.headers["Content-Disposition"] = f"attachment; filename={filename}"
    response.headers["Content-Type"] = "application/pdf"
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
