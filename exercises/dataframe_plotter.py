import matplotlib.pyplot as plot
class DataframePlotter:
	'Plots a dataframe; accepts options for naming and normalizing'

	def __init__(self, dataframe, label_dict = {}, normalize = True):
		self.dataframe = self._normalize(dataframe) if normalize else dataframe
		self.title = label_dict.get('title', 'Stock Prices')
		self.xlabel = label_dict.get('xlabel', None)
		self.ylabel = label_dict.get('ylabel', None)

	def plot(self):
		axes = self.dataframe.plot(fontsize=12)
		self._label_axes(axes)
		plot.show()

	def _label_axes(self, axes):
		axes.set_title(self.title)
		axes.set_xlabel(self.xlabel) if self.xlabel else False
		axes.set_ylabel(self.ylabel) if self.ylabel else False

	def _normalize(self, dataframe):
		return dataframe / dataframe.ix[0,:]