import pandas as pd

class Records(object):

    def __init__(self):
        self.records = []
        self.date_range = []

    def loadAllColumnsTable(self, uploadedFile):
        dataFrame = pd.read_csv(uploadedFile)
        self.records = dataFrame

    def showAllColumnsTable(self):
        return self.records
    
    def showTable(self):
        columns = ['Order Date', 'Order Priority', 
        'Units Sold', 'Unit Price', 'Total Cost', 'Total Revenue', 'Item Type']
        data_frame = pd.DataFrame(self.records, columns=columns)
        return data_frame.head(10)
    
    def loadDateRangeTotalProfit(self, strDate, endDate):
        self.records['Order Date'] = pd.to_datetime(self.records['Order Date'])
        mask = (self.records['Order Date'] > strDate) & (self.records['Order Date'] <= endDate)
        self.date_range = self.records.loc[mask]        
        totalProfit = self.date_range['Total Profit'].sum()
        return "{:,.2f}".format(totalProfit)
    
    def showDateRange(self, strDate, endDate):
        return "{} -- {}".format(strDate, endDate)
    
    def loadTop5ProfitableItems(self):
        columns = ['Item Type', 'Total Profit']
        ItemTypes = pd.DataFrame(self.date_range, columns=columns)
        groupedProfitableItems = ItemTypes.groupby(['Item Type']).sum()
        profitableItemTypes = groupedProfitableItems.sort_values(by='Total Profit', ascending=False)
        pd.options.display.float_format = '{:.2f}'.format        
        return profitableItemTypes.head()
