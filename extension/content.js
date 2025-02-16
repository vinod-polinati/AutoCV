/* content.js - Extracts job descriptions */
let jobText = document.querySelector('article')?.innerText;
if (jobText) {
    chrome.runtime.sendMessage({ jobDescription: jobText });
}
