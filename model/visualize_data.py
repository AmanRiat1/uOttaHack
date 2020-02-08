import matplotlib.pyplot as plt
import seaborn as sns


def heatmap(df):
    plt.figure(figsize=(15,15))
    sns.heatmap(data.corr(),annot = True,fmt = ".2f",cbar = True)
    plt.xticks(rotation=90)
    plt.yticks(rotation = 0)
