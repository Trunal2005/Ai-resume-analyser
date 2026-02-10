import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from Analyse_pdf import extract_text_from_pdf, analyze_resume

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    analysis_result = None
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'resume' not in request.files:
            return redirect(request.url)
        
        file = request.files['resume']
        job_description = request.form.get('job_description')
        api_key = request.form.get('api_key')

        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Extract text and analyze
            resume_text = extract_text_from_pdf(filepath)
            if resume_text:
                analysis_result = analyze_resume(resume_text, job_description, api_key)
            else:
                analysis_result = "Error: Could not extract text from the PDF."
            
            # Clean up: remove the uploaded file after analysis
            try:
                os.remove(filepath)
            except:
                pass

    return render_template('index.html', result=analysis_result)

if __name__ == '__main__':
    import webbrowser
    from threading import Timer

    def open_browser():
        webbrowser.open_new('http://127.0.0.1:5000/')

    Timer(1, open_browser).start()
    app.run(debug=True)
