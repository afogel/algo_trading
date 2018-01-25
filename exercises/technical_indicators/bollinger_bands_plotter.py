
class BollingerBandPlotter():
	"""
	BollingerBandPlotter will plot the bollinger bands (R) for a series of stocks contained
	within a dataframe.
	Bollinger bands are two standard deviations above and below a simple moving average for a
	given stock. The bollinger hypothesis is that if the current price of a stock is above or 
	below a bollinger band, it signals a buy or sell signal.
	"""
	def __init__(self, arg):
		self.arg = arg
		