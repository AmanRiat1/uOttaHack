import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

def SVM():
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel

    # Split dataset into training set and test set
    train_data_df = pd.read_csv('../data/processed/cleaned_data.csv')
    target = train_data_df['Dalc']
    train_data_df.drop(['Dalc'],axis=1,inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(train_data_df, target, test_size=0.3,random_state=109)

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    print(confusion_matrix(y_test,y_pred))


    class_names = [0,1,2,3,4,5,6,7,8,9,10]
    titles_options = [("Confusion matrix, without normalization", None),
                      ("Normalized confusion matrix", 'true')]
    for title, normalize in titles_options:
        disp = plot_confusion_matrix(clf, X_test, y_test,
                                     display_labels=class_names,
                                     cmap=plt.cm.Blues,
                                     normalize=normalize)
        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

    plt.show()

def RandomForest():
    rf = RandomForestClassifier()
    train_data_df = pd.read_csv('../data/processed/cleaned_data.csv')
    target = train_data_df['Dalc']
    train_data_df.drop(['Dalc'], axis=1, inplace=True)
    X_train, X_test, y_train, y_test = train_test_split(train_data_df, target, test_size=0.3, random_state=109)

    print (target.shape)
    print(train_data_df.shape)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_train)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


RandomForest()
