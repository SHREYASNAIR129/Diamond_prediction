import os
import pandas as pd

os.system("pip3 install -r requirements.txt")

def load_data():
    data = pd.read_csv("./diamonds.csv")
    return data
