# case-assignment

[![Build Status](https://travis-ci.org/Ayeeta/case-assignment.svg?branch=master)](https://travis-ci.org/Ayeeta/case-assignment)

A web-based app where a store manager can upload a .csv file into the system. On uploading the file,
a tabular display will show the following properties;
* Order Date 
* Unit Price
* Order Priority
* Total Cost
* Units Sold
* Item Type

The System has a mini-dashboard, where a user can input a given date range to show the following for the given date range;
* Total Profit made
* Top five profitable Item Types
* *Additional is a tabular display showing the data summary on the csv file*

## Pre-requisites ##

* Python
* Flask

### Getting Started ###

* Clone/download repository
* In your virtual environment run `pip install -r requirements.txt` to install the packages used
* Run `python app.py` to start the server. Link is most likely `http://127.0.0.1:5000/`

### Running Tests ###

* Run `nosetests`

### Author ###

Elijah Ayeeta
