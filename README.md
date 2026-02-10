# AI Resume Analyser

A powerful tool leveraging Google's Gemini AI to analyze resumes against job descriptions, providing detailed feedback, compatibility scores, and improvement suggestions.

## 🚀 Features

*   **PDF Parsing**: robustly extracts text from uploaded PDF resumes.
*   **AI-Powered Analysis**: Uses Google Gemini (Generative AI) to evaluate resumes.
*   **Job Description Matching**: (Optional) specific analysis based on a provided job description.
*   **Compatibility Score**: Estimates how well the resume matches the job requirements.
*   **User-Friendly Interface**: Clean and responsive web UI built with Flask and HTML/CSS.
*   **Demo Mode**: Try the UI with mock data even without an API key.
*   **Dynamic API Key**: Enter your Google API key securely via the web interface or environment variables.

## 🛠️ Technologies Used

*   **Backend**: Python, Flask
*   **AI Model**: Google Gemini Pro (`google-generativeai`)
*   **PDF Processing**: `pypdf`
*   **Frontend**: HTML5, CSS3

## 📋 Prerequisites

*   Python 3.8 or higher
*   A Google Cloud Project with the Gemini API enabled (for real analysis)

## ⚙️ Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Trunal2005/ai-resume-analyser.git
    cd ai-resume-analyser
    ```

2.  **Create a virtual environment** (Recommended)
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration (Optional)**
    Create a `.env` file in the root directory and add your API key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

## ▶️ Usage

1.  **Run the application**
    ```bash
    python main.py
    ```

2.  **Open your browser**
    The app should open automatically at `http://127.0.0.1:5000`.

3.  **Analyze a Resume**
    *   Upload a PDF resume.
    *   (Optional) Paste the Job Description.
    *   Enter your **Google API Key** (if not set in `.env`).
    *   Click **Analyze Resume**.

    > **Note**: If you don't have an API key, leave the field blank to see a **Mock Analysis** (Demo Mode).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
