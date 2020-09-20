from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        uploadedFile = request.files['upload_file']
        if uploadedFile != '':        
            data = pd.read_csv(uploadedFile)
            return render_template("data.html", data=data.to_html())

if __name__ == "__main__":
    app.run(debug=True)