from dataframe_builder import DataframeBuilder

print('In the main!')
date_range = ['12/01/2017', '01/16/2018']
datasets = ['SPY', 'GLW', 'PHO', 'PALL', 'CEF']
dataframe = DataframeBuilder(datasets, date_range).build()
print(dataframe)

# plot_labels = {'xlabel': 'Dates', 'ylabel': 'Price'}
# dfp = DataframePlotter(dataframe, plot_labels).plot()