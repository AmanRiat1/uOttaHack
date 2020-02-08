import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def heatmap(df):
    plt.figure(figsize=(15,15))
    sns.heatmap(data.corr(),annot = True,fmt = ".2f",cbar = True)
    plt.xticks(rotation=90)
    plt.yticks(rotation = 0)

def FeatureImportance(df, rf):
    features = list(df.columns)
    importances = rf.feature_importances_
    indices = np.argsort(importances)

    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Relative Importance')
    plt.show()
