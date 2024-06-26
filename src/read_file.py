import os
import pandas as pd

def read_data(file_path):
    _,file_ext = os.path.splitext(file_path)
    if file_ext == '.csv':
        return pd.read_csv(file_path)
    elif file_ext == '.json':
        return pd.read_json(file_path)
    elif file_ext in ['.xls','.xlsx']:
        return pd.read_excel(file_path)
    else:
        raise Exception
