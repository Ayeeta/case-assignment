from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import datetime as dt

app = Flask(__name__)
df = pd.DataFrame(columns=['Order Date'])


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
            global df
            df = data_frame.head(10)
            return render_template("data.html", df=df.to_html(classes="table table-striped"))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        if request.form.get("mini_dashboard"):
            pageTitle = 'Mini Dash Board'
            return render_template("dashboard.html", pageTitle=pageTitle)
        if request.form.get("Load"):
            strDate = request.form['startDate']
            endDate = request.form['toDate']            
            global df
            df['Order Date'] = pd.to_datetime(df['Order Date']) 
            mask = (df['Order Date'] > strDate) & (df['Order Date'] <= endDate)
            dateRangeResult = df.loc[mask]
           
            return render_template("dashboard.html", dateRangeResult=dateRangeResult.to_html())

if __name__ == "__main__":
    app.run(debug=True)