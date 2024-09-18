import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List


#def unique_values(df: pd.DataFrame) -> pd.DataFrame:

def missing_values(df: pd.DataFrame) -> pd.DataFrame:
    length = df.shape[0]
    missing_values_count = df.isnull().sum()
    missing_values_percentage = (df.isnull().sum() / len(df)) * 100).round(2)
    summary_df = pd.DataFrame({
        'Column': df.columns,
        'Missing Values': missing_values_count,
        'Percentage Missing': missing_values_percentage
    })
    return summary_df

def violin_boxplot(data: pd.DataFrame, columns: List[str], title: Optional[
    str] = None) -> plt.Figure:
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data[columns], orient='h',
                   density_norm='count', inner=None)
    sns.boxplot(data=data[columns], width=0.2,
                showfliers=True,
                boxprops={'facecolor': 'None'}, orient='h')
    if title:
        plt.title(title)
    plt.show()