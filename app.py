from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
from classes.Records import Records
    
import pandas as pd
import datetime as dt

app = Flask(__name__)
records = Records()

dataF = pd.DataFrame(columns=['Order Date'])


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        uploadedFile = request.files['upload_file']
        if uploadedFile != '':             
            records.loadAllColumnsTable(uploadedFile)
            df = records.showTable()
            return render_template("data.html", df=df.to_html(classes="table table-striped"))
            

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        if request.form.get("upload_file"):
            return redirect(url_for('/'))        
        if request.form.get("Load"):
            pageTitle = 'Mini Dash Board'
            strDate = request.form['startDate']
            endDate = request.form['toDate']
            totalProfit = records.loadDateRangeTotalProfit(strDate, endDate) 
            profitableItemTypes = records.loadTop5ProfitableItems()
            dateRange = records.showDateRange(strDate, endDate)
            df = records.showTable()
            return render_template('dashboard.html',dateRange=dateRange, pageTitle=pageTitle, df=df.to_html(classes="table table-striped"), totalProfit=totalProfit, profitableItemTypes=profitableItemTypes.to_html(classes="table table-striped"))

@app.errorhandler(404)
def page_not_found(e):
    """Page not found"""
    return render_template('404.html'), 404


@app.errorhandler(400)
def bad_request(e):
    """Bad request."""
    return render_template('400.html'), 400


@app.errorhandler(500)
def server_error(e):    
        """Internal server error."""
        return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=False)