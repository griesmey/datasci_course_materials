from csv import DictReader

import numpy as np
from pandas import *
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation


def generate_array(filename, predictor):
    train = []
    y = []
    for row in DictReader(open(filename)):
        for i, j in row.iteritems():
            if i == predictor:
                y.append(int(j))
            else:
                row[i] = str(j)
        if predictor in row:
            del row[predictor]
        train.append(row)
    vectorizer = DictVectorizer()
    vector_fit = vectorizer.fit_transform(train)
    X = vector_fit.toarray()
    return X, y, vectorizer

X, y, vectorizer = generate_array('../Downloads/amazon_priv.csv', 'ACTION')

X_vector = []
for row in DictReader(open('../Downloads/amazon_priv_test.csv')):
    for i, j in row.iteritems():
        row[i] = str(j)
    X_vector.append(row)
x = vectorizer.transform(X_vector)

X_train = X
y_train = y

clf = GaussianNB()
svc_model = clf.fit(X_train, y_train)
predictions = svc_model.predict(x.toarray())

np.savetxt("kaggle_amazon_1.csv", predictions, delimiter=",")
