import pandas as pd

def load_data():
    data = pd.read_csv("./diamonds.csv")
    return data
