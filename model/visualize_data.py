import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.tree import export_graphviz
import pydotplus

def heatmap(df):
    plt.figure(figsize=(15,15))
    sns.heatmap(df.corr(),annot = True,fmt = ".2f",cbar = True)
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

"""
def tree_visualization(df,rf):
    dot_data = export_graphviz(rf.estimators_[0], out_file=None, feature_names=df.columns, rounded=True, filled=True)

    pydot_graph = pydotplus.graph_from_dot_data(dot_data)
    pydot_graph.write_png('original_tree.png')
    pydot_graph.set_size('"5,5!"')
    pydot_graph.write_png('resized_tree.png')
"""
