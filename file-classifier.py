from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def classify_file(file_path):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xls') or file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            return "Unsupported file format", None

        if 'UID' in df.columns and 'Timestamp' in df.columns:
            return "Sales Record", df
        elif any(df.apply(lambda row: row.astype(str).str.contains('INFO|ERROR|DEBUG').any(), axis=1)):
            return "Log File", df
        else:
            return "Unknown", df
    except Exception as e:
        return f"Error: {str(e)}", None

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            classification, preview = classify_file(file_path)

            # Rename the file
            new_filename = f"{classification.replace(' ','')}-{file.filename}"
            new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
            os.rename(file_path, new_file_path)

            return render_template('result.html', classification=classification, tables = [preview.to_html(classes='pure-table ', header="true")])
    app.logger.info('GET request accessed')
    return render_template('upload.html')

app.run(debug=True, port=5000)