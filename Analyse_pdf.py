import os
from dotenv import load_dotenv
import google.generativeai as genai
from pypdf import PdfReader

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    # Handle the case where the API key is missing, potentially log a warning
    # For now, we'll just print to console, but in production, use logging
    print("Warning: GOOGLE_API_KEY not found in environment variables.")

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    return text

def analyze_resume(resume_text, job_description=None, api_key=None):
    """
    Analyzes the resume text using Gemini AI.

    Args:
        resume_text (str): The text content of the resume.
        job_description (str, optional): The job description to compare against.
        api_key (str, optional): The Google API Key to use for this request.

    Returns:
        str: The analysis result from Gemini.
    """
    # Configure API key if provided, otherwise check environment variable
    if api_key:
        genai.configure(api_key=api_key)
    elif not os.getenv("GOOGLE_API_KEY"):
        return "Error: Google API Key is missing. Please provide it in the form or configure it in the .env file."

    model = genai.GenerativeModel('gemini-pro')

    prompt = f"""
    You are an expert HR and Resume Analyser.
    I will provide you with a resume text and optionally a job description.
    
    Resume Text:
    {resume_text}
    """

    if job_description:
        prompt += f"""
        \nJob Description:
        {job_description}
        
        Please analyze the resume against the job description. 
        Provide a compatibility score (0-100%), matching skills, missing skills, and detailed suggestions for improvement.
        """
    else:
        prompt += """
        \nPlease analyze this resume. 
        Provide an overview of strengths, weaknesses, and detailed suggestions for improvement to increase the chances of getting hired.
        Highlight key skills and experience found.
        """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Fallback to mock response if API fails
        print(f"API Error: {e}")
        return """
        **[MOCK ANALYSIS - API KEY INVALID OR MISSING]**

        **Compatibility Score:** 85%

        **Strengths:**
        *   strong background in Python and backend development.
        *   Experience with Flask and API integration is relevant.
        *   Good understanding of project structure and deployment.

        **Weaknesses:**
        *   Resume formatting could be improved for ATS.
        *   Lack of specific metrics (e.g., "improved performance by 20%").

        **Suggestions:**
        *   Add more quantitative results to your experience section.
        *   Include a skills section with keywords from the job description.
        *   Proofread for minor typos.
        
        *(Please provide a valid Google API Key for real-time AI analysis)*
        """