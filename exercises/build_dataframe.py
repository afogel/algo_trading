import pdb
import pandas as pd
from datetime import datetime 

class DataframeBuilder:
	'Builds a dataframe from multiple stocks'

	def __init__(self, datasets, daterange, column='Adj Close'):
		_daterange = self._parse_daterange(daterange)
		self.dataframe = pd.DataFrame(index=_daterange)
		self.datasets = datasets
		self.column = column

	def build(self):
		for stock_symbol in self.datasets:
			self._add_dataset_to_dataframe(stock_symbol, self.column)
		return self.dataframe

	def _parse_daterange(self, daterange):
		start_date_string, end_date_string = daterange[0], daterange[1]
		start_date = datetime.strptime(start_date_string, "%m/%d/%Y")
		end_date = datetime.strptime(end_date_string, "%m/%d/%Y")
		if start_date > end_date:
			raise ValueError('Start date must be before end date')
		else:
			return pd.date_range(start_date_string, end_date_string)

	def _add_dataset_to_dataframe(self, symbol, column):
		temp_df = pd.read_csv("../data/{}.csv".format(symbol), index_col='Date',
			parse_dates=True, usecols=['Date', column], na_values=['nan'])
		temp_df = temp_df.rename(columns={column: symbol})
		self.dataframe = self.dataframe.join(temp_df, how='inner')

class DataframePlotter:
	'Plots a dataframe; accepts options for naming and normalizing'

	def __init__(self, dataframe, label_dict = {}, normalize = True):
		self.dataframe = dataframe
		self.title = label_dict['title']
		self.xlabel = label_dict['xlabel']
		self.ylabel = label_dict['ylabel']
		self.normalize = normalize

	def plot():
		pass

date_range = ['01/01/2015', '01/16/2018']
datasets = ['SPY', 'GLW', 'PHO', 'PALL', 'CEF']
dataframe = DataframeBuilder(datasets, date_range).build()
print(dataframe)

