from dataframe_helpers.dataframe_builder import DataframeBuilder
from dataframe_helpers.dataframe_plotter import DataframePlotter
from technical_indicators.bollinger_bands_plotter import BollingerBandsPlotter

print('Starting Program!')

date_range = ['12/01/2017', '01/16/2018']
# datasets = ['SPY', 'GLW', 'PHO', 'PALL', 'CEF']
datasets = ['SPY']
dataframe = DataframeBuilder(datasets, date_range).build()
# plot_labels = {'xlabel': 'Dates', 'ylabel': 'Price'}
# dfp = DataframePlotter(dataframe, plot_labels).plot()
BollingerBandsPlotter(dataframe, window=20).plot()