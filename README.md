# AI Resume Critiquer 

An AI-powered web application that provides instant, tailored feedback on resumes. Users can upload a PDF or TXT resume, specify a target job role, and receive constructive criticism on content clarity, skills presentation, and experience descriptions.

 **Live Demo App (https://ai-resume-critiquer-kvvfc2ntkx3wblyrgvseyg.streamlit.app/)**

## Tech Stack
*   **Frontend:** Streamlit
*   **Language:** Python
*   **AI Model:** Gemini 2.5 Flash (via OpenAI SDK compatibility layer)
*   **File Parsing:** PyPDF2

##  Features
*   Secure file uploading (PDF & TXT).
*   Custom prompts tailored to specific job roles.
*   Robust error handling for empty files.
*   Secure environment variable management for API keys.

## Run Locally
1. Clone the repo: `git clone https://github.com/emmanuelbwalya284-lang/AI-Resume-Critiquer.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your `GEMINI_API_KEY`.
4. Run the app: `streamlit run main.py`