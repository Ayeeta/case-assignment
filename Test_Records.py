from classes.Records import *
import unittest
import pandas as pd

class TestRecords(unittest.TestCase):

    def setUp(self):
        d = {'Total Profit': [2111.11, 2111.11,1,2,3,4,5,6,7,8], 
        'Order Date': ['12-1-2020', '13-2-2020',1,2,3,4,5,6,7,8],
         'Order Priority':[1,2,3,4,5,6,7,8,9,0], 'Units Sold':[1,2,3,4,5,6,7,8,9,0],
          'Unit Price':[1,2,3,4,5,6,7,8,9,0], 'Total Cost':[1,2,3,4,5,6,7,8,9,0],
           'Total Revenue':[1,2,3,4,5,6,7,8,9,0], 'Item Type':[1,2,3,4,5,6,7,8,9,0]}
        df = pd.DataFrame(data=d)
        self.records = Records()
        self.records.records = df

    def test_showAllColumns(self):
        result = self.records.showAllColumnsTable()        
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_showDateRange_returns_formatted_string_date_range(self):
        strDate = '12-1-2020'
        endDate = '13-2-2020'
        result_date = '12-1-2020 -- 13-2-2020'
        self.assertTrue(result_date, self.records.showDateRange(strDate, endDate))

    def test_loadDateRangeTotalProfit_returns_formatted_total_profit(self):
        totalProfit = 4222.22
        result_totalProfit = "{:,.2f}".format(totalProfit)
        self.assertTrue(result_totalProfit, self.records.loadDateRangeTotalProfit('12-1-2020','13-2-2020'))

    def test_showTable_returns_ten_records(self):
        dataframe = self.records.showTable()
        index = len(dataframe.index)
        self.assertEqual(10, index)
    
    def test_loadTop5ProfitableItems_returns_correct_number_of_records(self):
        dataframe = self.records.loadTop5ProfitableItems()
        index = len(dataframe.index)
        self.assertEquals(0, index)

    def test_summarizedData_returns_data_frame(self):
        result = self.records.summarizedData()
        self.assertIsInstance(result, pd.DataFrame)

    