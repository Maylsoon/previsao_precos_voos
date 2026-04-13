import pandas as pd

def load_data():
    path = "../base/Data_Train.xlsx"
    df = pd.read_excel(path)
    return df