import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List


#def unique_values(df: pd.DataFrame) -> pd.DataFrame:

def missing_values(df: pd.DataFrame) -> pd.DataFrame:
    length = df.shape[0]
    missing_values = df.isnull().sum().reset_index()
    missing_values.columns = ['features', 'null_count']
    missing_values['null_%'] = (missing_values['null_count']*100 /
                                      length).round(2)
    return missing_values
