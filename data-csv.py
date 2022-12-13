# import pandas informs the library to import the panadas data analysis library
# as pd tells python allows a short form version to be easily read for the users

import pandas as pd

# read csv is used to load a CSV file as a pandas dataframe
# df stands for dataframe and it is a 2 dimensional data structure
df: str = pd.read_csv('aapl-yahoo.csv')

print(df)
