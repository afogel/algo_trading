import pandas as pd

def test_run():
	# print_last_five_lines()
	calculate_mean_volumes()

def print_last_five_lines():
	data_frame = pd.read_csv("../data/HCP.csv")
	print(data_frame.tail(5))


def calculate_mean_volumes():
	for symbol in ['GOOG', 'HCP']:
		data_frame = pd.read_csv("../data/{}.csv".format(symbol))
		get_mean_volume(data_frame, symbol)

# Private

def get_mean_volume(data_frame, symbol):
	print("Mean Volume: {}".format(symbol))
	print(data_frame['Volume'].mean())

if __name__ == '__main__':
	test_run()