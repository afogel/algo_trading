import pandas as pd
import matplotlib.pyplot as plot
import pdb

def test_run():
	df = pd.read_csv('../data/GOOG.csv')
	print(df['High'])
	df[['High', 'Low']].plot()
	plot.show()


if __name__ == '__main__':
	test_run()