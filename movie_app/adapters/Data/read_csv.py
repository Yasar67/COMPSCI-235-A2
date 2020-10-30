import pandas as pd


def read_csv(fname):
    data = pd.read_csv(fname)

    print(len(data.columns))
    print(data.columns)


file = 'Data1000Movies.csv'
read_csv(file)
