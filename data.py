"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv("data/311-calls.csv", parse_dates=["created"])
    df["created"] = df["created"].dt.date
    df.drop(columns=["deviceid"], inplace=True)
    num_oem = df["oem"].value_counts()
    to_remove = num_oem[num_oem <= 30].index
    df.replace(to_remove, np.nan, inplace=True)
    return df
