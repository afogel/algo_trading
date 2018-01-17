import pdb
import pandas as pd
from datetime import datetime 

class DataframeBuilder:
	'Builds a dataframe from multiple stocks'

	def __init__(self, datasets, daterange):
		self.datasets = datasets
		__daterange = self.__parse_daterange(daterange)
		self.dataframe = pd.DataFrame(index=__daterange)


	def __parse_daterange(self, daterange):
		start_date_string, end_date_string = daterange[0], daterange[1]
		start_date = datetime.strptime(start_date_string, "%m/%d/%Y")
		end_date = datetime.strptime(end_date_string, "%m/%d/%Y")
		if start_date > end_date:
			raise ValueError('Start date must be before end date')
		else:
			return pd.date_range(start_date_string, end_date_string)

	def __add_dataset_to_dataframe(dataset):
		pass

date_range = ['01/01/2015', '01/01/2018']
datasets = ['GOOG']
dfb = DataframeBuilder(datasets, date_range)

if __name__ == 'main':
	print('hi mom')
	# dfb = DataframeBuilder()
	# dfb = DataframeBuilder(['GOOG'],date_range)
	# print(DataframeBuilder([],date_range))