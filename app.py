from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import datetime as dt

app = Flask(__name__)
dataF = pd.DataFrame(columns=['Order Date'])


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        uploadedFile = request.files['upload_file']
        if uploadedFile != '':  
            global dataF      
            dataF = pd.read_csv(uploadedFile) 
                      
            columns = ['Order Date', 'Order Priority', 'Units Sold', 'Unit Price', 'Total Cost', 'Total Revenue', 'Item Type']
            data_frame = pd.DataFrame(dataF, columns=columns)            
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
            global dataF  

            dataF['Order Date'] = pd.to_datetime(dataF['Order Date']) 
            mask = (dataF['Order Date'] > strDate) & (dataF['Order Date'] <= endDate)
            dateRangeResult = dataF.loc[mask]
            totalProfit = dateRangeResult['Total Profit'].sum()
            columns = ['Item Type', 'Total Profit']
            valuableItems = pd.DataFrame(dateRangeResult, columns=columns)

            groupedItems = valuableItems.groupby(['Item Type']).sum()

            profitableItemTypes = groupedItems.sort_values(by='Total Profit', ascending=False)
            pItems = profitableItemTypes.head()
            # pItems = groupedItems.head()
            
            return render_template("dashboard.html", totalProfit=totalProfit, pItems=pItems.to_html())

if __name__ == "__main__":
    app.run(debug=True)