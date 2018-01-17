import pdb
import pandas as pd
from datetime import datetime 

class DataframeBuilder:
	'Builds a dataframe from multiple stocks'

	def __init__(self, datasets, daterange, column='Adj Close'):
		__daterange = self.__parse_daterange(daterange)
		self.dataframe = pd.DataFrame(index=__daterange)
		for stock_symbol in datasets:
			self.__add_dataset_to_dataframe(stock_symbol, column)


	def __parse_daterange(self, daterange):
		start_date_string, end_date_string = daterange[0], daterange[1]
		start_date = datetime.strptime(start_date_string, "%m/%d/%Y")
		end_date = datetime.strptime(end_date_string, "%m/%d/%Y")
		if start_date > end_date:
			raise ValueError('Start date must be before end date')
		else:
			return pd.date_range(start_date_string, end_date_string)

	def __add_dataset_to_dataframe(self, symbol, column):
		temp_df = pd.read_csv("../data/{}.csv".format(symbol), index_col='Date',
			parse_dates=True, usecols=['Date', column], na_values=['nan'])
		temp_df = temp_df.rename(columns={column: symbol})
		self.dataframe = self.dataframe.join(temp_df, how='inner')

date_range = ['01/01/2015', '01/16/2018']
datasets = ['SGOL', 'GLW', 'PHO', 'PALL']
dfb = DataframeBuilder(datasets, date_range)
print(dfb.dataframe)
