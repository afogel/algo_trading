import matplotlib.pyplot as plot

class BollingerBandsPlotter():
	"""
	BollingerBandPlotter will plot the bollinger bands (R) for a series of stocks contained
	within a dataframe.
	Bollinger bands are two standard deviations above and below a simple moving average for a
	given stock. The bollinger hypothesis is that if the current price of a stock is above or 
	below a bollinger band, it signals a buy or sell signal.
	"""
	def __init__(self, dataframe, window):
		self.dataframe = dataframe
		self.window = window

	def plot(self):
		mean = self._calculate_rolling_mean()
		upperbound, lowerbound = self._calculate_bollinger_bands(mean)
		axis = self.dataframe.plot(fontsize=12, title='Bollinger Bands')
		mean.plot(label='Rolling Mean', ax=axis)
		upperbound.plot(label='upper band', ax=axis)
		lowerbound.plot(label='lower band', ax=axis)
		plot.show()

	def _calculate_rolling_mean(self):
		return self.dataframe.rolling(window = self.window).mean()

	def _calculate_bollinger_bands(self, mean):
		standard_deviation = self.dataframe.rolling(window = self.window).std()
		upperbound = mean + (2*standard_deviation)
		lowerbound = mean - (2*standard_deviation)
		return upperbound, lowerbound
		