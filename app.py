import os
from flask import Flask, render_template, request

from parser import analyze_logs
from ai_service import analyze_with_ai

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():

    file = request.files.get('logfile')

    if not file or file.filename == '':
        return "No file uploaded", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    # DEBUG (temporary)
    print("Saved file at:", filepath)

    with open(filepath, "r") as f:
        log_text = f.read()

    print("LOG CONTENT:", log_text)

    results = analyze_logs(filepath)
    ai_result = analyze_with_ai(log_text)

    return render_template(
        "results.html",
        results=results,
        ai=ai_result
    )

if __name__ == '__main__':
    app.run(debug=True)