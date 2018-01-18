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
		temp_df = pd.read_csv(
			"../data/{}.csv".format(symbol),
			index_col='Date',
			parse_dates=True,
			usecols=['Date', column],
			na_values=['nan']
		)
		temp_df = temp_df.rename(columns={column: symbol})
		self.dataframe = self.dataframe.join(temp_df, how='inner')

import matplotlib.pyplot as plot
class DataframePlotter:
	'Plots a dataframe; accepts options for naming and normalizing'

	def __init__(self, dataframe, label_dict = {}, normalize = True):
		self.dataframe = dataframe
		self.title = label_dict.get('title', 'Stock Prices')
		self.xlabel = label_dict.get('xlabel', None)
		self.ylabel = label_dict.get('ylabel', None)
		self.normalize = normalize

	def plot(self):
		axes = self.dataframe.plot(fontsize=12)
		self._label_axes(axes)
		plot.show()

	def _label_axes(self, axes):
		axes.set_title(self.title)
		axes.set_xlabel(self.xlabel) if self.xlabel else False
		axes.set_ylabel(self.ylabel) if self.ylabel else False


date_range = ['01/01/2015', '01/16/2018']
datasets = ['SPY', 'GLW', 'PHO', 'PALL', 'CEF']
dataframe = DataframeBuilder(datasets, date_range).build()
plot_labels = {'xlabel': 'Dates', 'ylabel': 'Price'}
dfp = DataframePlotter(dataframe, plot_labels).plot()
# print(dfp.title)
# print(dataframe)

