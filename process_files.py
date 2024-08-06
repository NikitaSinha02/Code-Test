# -*- coding: utf-8 -*-

import pandas as pd

def read_csv_files(files):
    dataframes = []

    for file in files:
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
            print(f"Processed file: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    if dataframes:
        all_data = pd.concat(dataframes, ignore_index=True)
        return all_data
    else:
        return pd.DataFrame()

