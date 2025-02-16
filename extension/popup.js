document.addEventListener("DOMContentLoaded", function () {
    const generateBtn = document.getElementById("generate");
    const downloadBtn = document.getElementById("download");
    const coverLetterOutput = document.getElementById("cover-letter");

    generateBtn.addEventListener("click", function () {
        // Get values from input fields
        const jobDescription = document.getElementById("job-description").value.trim();
        const companyName = document.getElementById("company-name").value.trim();
        const userName = document.getElementById("user-name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const experience = document.getElementById("experience").value.trim();
        const uniName = document.getElementById("uni-name").value.trim();
        const degree = document.getElementById("degree").value.trim();
        const major = document.getElementById("major").value.trim();

        // Validation: Ensure all fields are filled
        if (!jobDescription || !companyName || !userName || !email || !phone || !experience || !uniName || !degree || !major) {
            alert("Please fill in all fields.");
            return;
        }

        // Generate the cover letter text
        const coverLetter = `
Dear Hiring Manager at ${companyName},

I am excited to apply for this position at ${companyName}. With my experience as ${experience} and my educational background in ${degree} with a major in ${major} from ${uniName}, I am confident in my ability to contribute to your team.

The job description mentions:  
${jobDescription}  

This aligns perfectly with my skills and expertise. My past experiences have prepared me to excel in this role.

I am eager to bring my knowledge and skills to ${companyName}. Please feel free to contact me at ${phone} or ${email} to discuss this opportunity further.

Sincerely,  
${userName}
        `;

        // Display the cover letter in the <pre> tag
        coverLetterOutput.textContent = coverLetter;

        // Enable the "Download PDF" button
        downloadBtn.disabled = false;
    });

    // Download PDF functionality
    downloadBtn.addEventListener("click", function () {
        // Load jsPDF
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();

        const coverLetterText = coverLetterOutput.textContent;
        const margin = 10;
        const pageWidth = doc.internal.pageSize.getWidth() - 2 * margin;

        doc.setFont("times", "normal");
        doc.setFontSize(12);
        doc.text(coverLetterText, margin, margin, { maxWidth: pageWidth });

        // Save the PDF
        doc.save("Cover_Letter.pdf");
    });
});
