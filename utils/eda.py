import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List


#def unique_values(df: pd.DataFrame) -> pd.DataFrame:

def missing_values(df: pd.DataFrame) -> pd.DataFrame:
    length = df.shape[0]
    missing_values_count = df.isnull().sum()
    missing_values_percentage = round((df.isnull().sum() / len(df)) * 100, 2)
    summary_df = pd.DataFrame({
        'Column': df.columns,
        'Missing Values': missing_values_count,
        'Percentage Missing': missing_values_percentage
    })
    return summary_df

def violin_boxplot(data: pd.DataFrame, columns: List[str], title: Optional[
    str] = None, figsize: Optional[tuple] = (10, 6)) -> None:
    plt.figure(figsize=figsize)
    sns.violinplot(data=data[columns], orient='h',
                   density_norm='count', inner=None)
    sns.boxplot(data=data[columns], width=0.2,
                showfliers=True,
                boxprops={'facecolor': 'None'}, orient='h')
    if title:
        plt.title(title)
    plt.show()


def countplot(data: pd.DataFrame, columns:List[str], title: Optional[str] =
None, nrows: int = 1, ncols: int = 1) -> None:


    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols*5,
                                                                nrows*4))
    fig.subplots_adjust(hspace=1, wspace=0.4)
    axes_flatten = axes.flatten()
    col_len = len(columns)
    axes_len = len(axes_flatten)


    for i, col in enumerate(columns):
        sns.countplot(data=data, x=col, ax=axes_flatten[i])
        axes_flatten[i].set_title(col, pad=15)
        for p in axes_flatten[i].patches:
            (axes_flatten[i]
             .annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p
                        .get_height()), ha='center',
                       va='center', xytext=(0, 10),
                       textcoords='offset points'))
        sns.despine(top=True, right=True, left=True, bottom=True)
        axes_flatten[i].tick_params(axis='x', which='both', length=0,
                                    labelbottom=True)
        axes_flatten[i].tick_params(axis='y', which='both', length=0,
                                    labelleft=False)
        axes_flatten[i].set(ylabel=None, xlabel=None)


    if col_len < axes_len:
        for j in range(col_len, len(axes_flatten)):
            axes_flatten[j].clear()
            axes_flatten[j].axis('off')

    if title:
        plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()

def percentageplot(data: pd.DataFrame, columns:List[str], title: Optional[
    str] = None, nrows: int = 1, ncols: int = 1) -> None:


    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols*5,
                                                                nrows*4))
    fig.subplots_adjust(hspace=1, wspace=0.4)
    axes_flatten = axes.flatten()
    col_len = len(columns)
    df_len = data.shape[0]
    axes_len = len(axes_flatten)

    for i, col in enumerate(columns):
        sns.countplot(data=data, x=col, ax=axes_flatten[i])
        axes_flatten[i].set_title(col, pad=15)
        for p in axes_flatten[i].patches:
            percentage = round((p.get_height() * 100 / df_len), 2)
            (axes_flatten[i]
             .annotate(f'{percentage}%',
                       (p.get_x() + p.get_width() / 2., p
                        .get_height()), ha='center',
                       va='center', xytext=(0, 10),
                       textcoords='offset points'))
        sns.despine(top=True, right=True, left=True, bottom=True)
        axes_flatten[i].tick_params(axis='x', which='both', length=0,
                                    labelbottom=True)
        axes_flatten[i].tick_params(axis='y', which='both', length=0,
                                    labelleft=False)
        axes_flatten[i].set(ylabel=None, xlabel=None)

    if col_len < axes_len:
        for j in range(col_len, len(axes_flatten)):
            axes_flatten[j].clear()
            axes_flatten[j].axis('off')

    if title:
        plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()

def stacked_bar_plot(df: pd.DataFrame, col: str, hue: str,
                     color: Optional[List[str]] = None,
                     title: Optional[str] = None, xlabel: Optional[str] = None,
                     ylabel: Optional[str] = None) -> None:
    """
    Plots a stacked bar chart with the given DataFrame and column,
    with stack segments defined by hue.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        col (str): The column name to be used as the x-axis.
        hue (str): The column name used to define the stack segments.
        color (Optional[List[str]]): A list of colors for each stack segment.
        title (Optional[str]): The title of the plot.
        xlabel (Optional[str]): The label for the x-axis.
        ylabel (Optional[str]): The label for the y-axis.

    """
    categories = df[col].unique()
    hues = df[hue].unique()

    if color is None:
        color = sns.color_palette('dark', n_colors=len(hues))

    fig, ax = plt.subplots()

    bottom = np.zeros(len(categories))

    for idx, h in enumerate(hues):
        group_data = df[df[hue] == h].groupby(col).size().reindex(categories,
                                                                  fill_value=0)
        plt.bar(categories, group_data, bottom=bottom, color=color[idx],
                label=h)
        bottom += group_data.values

    plt.xlabel(xlabel if xlabel else col)
    plt.ylabel(ylabel if ylabel else 'Count')
    plt.title(title if title else f'{col} Counts by {hue}')
    plt.legend(title=hue)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()
