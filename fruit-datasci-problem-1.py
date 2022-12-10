import pandas as pd

data = {'Apples': [3, 10, 3],
        'Pears': [2, 20, 3],
        }

df = pd.DataFrame(data, index=['James', 'John', 'Jane'])

print(df)
