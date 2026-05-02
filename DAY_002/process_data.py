import pandas as pd

def filter_electronics_under_price(input_file, output_file, max_price):
	df = pd.read_csv(input_file)
	filtered_df = df[
		(df['category'] == 'Electronics') &
		(df['price'] < max_price)
	]

	print(filtered_df)

	filtered_df.to_csv(output_file, index=False)

filter_electronics_under_price(
	input_file='products.csv',
	output_file='filtered_electronics.csv',
	max_price=100
)
