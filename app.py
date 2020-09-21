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
            columns = ['Order Date', 'Order Priority', 'Units Sold', 'Unit Price', 'Total Cost', 'Total Revenue', 'Item Type']
            data_frame = pd.DataFrame(data, columns=columns)
            return render_template("index.html", data_frame=data_frame.to_html())

if __name__ == "__main__":
    app.run(debug=True)