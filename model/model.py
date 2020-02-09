import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import visualize_data

def SVM():
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel

    # Split dataset into training set and test set
    train_data_df = pd.read_csv('../data/processed/cleaned_data.csv')
    target = train_data_df['Dalc']
    train_data_df.drop(['Dalc'],axis=1,inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(train_data_df, target, test_size=0.3,random_state=42)

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    pickle.dump(clf, open("../trained_models/svm.p", "wb"))


def RandomForest():
    rf = RandomForestClassifier(n_estimators=300, max_depth=3)
    train_data_df = pd.read_csv('../data/processed/cleaned_data.csv')
    target = train_data_df['Dalc']
    train_data_df.drop(['Dalc'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(train_data_df, target, test_size=0.3, random_state=42)

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    pickle.dump(rf, open("../trained_models/rf.p", "wb"))
    visualize_data.FeatureImportance(train_data_df,rf)

def KNN():
    knn_model = KNeighborsClassifier()
    train_data_df = pd.read_csv('../data/processed/cleaned_data.csv')
    target = train_data_df['Dalc']
    train_data_df.drop(['Dalc'], axis=1, inplace=True)

    X_train, X_test, y_train, y_test = train_test_split(train_data_df, target, test_size=0.3, random_state=42)

    knn_model.fit(X_train,y_train)
    y_pred = knn_model.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    pickle.dump(knn_model, open("../trained_models/knn.p", "wb"))

SVM()
RandomForest()
KNN()