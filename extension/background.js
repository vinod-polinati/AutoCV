/* background.js - Handles data flow */
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log('Extracted Job Description:', message.jobDescription);
});