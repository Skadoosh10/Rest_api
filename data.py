import pandas as pd

data = pd.read_csv("books.csv", usecols=[0, 1]);
data.to_csv("new_books.csv", index=False)