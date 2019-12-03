import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import graphviz 





dataset = pd.read_csv("imuDataAccel.csv")



X = dataset.drop('Class', axis=1)
features = X.head(0)
print(features)

y = dataset['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


classifier = DecisionTreeClassifier() 
tree.plot_tree(classifier.fit(X_train, y_train)) 


dot_data = tree.export_graphviz(classifier,
	feature_names=["x1","y1","z1","x2","y2","z2","x3","y3","z3","x4","y4","z4","x5","y5","z5","x6","y6","z6","x7","y7","z7","x8","y8","z8","x9","y9","z9","x10","y10","z10","x11","y11","z11","x12","y12","z12","x13","y13","z13","x14","y14","z14"]
	,class_names=["True","False"],out_file=None,filled=True, rounded=True,special_characters=True)

graph = graphviz.Source(dot_data) 
graph.render("imuDataAccel1") 


print("Size of X_test",len(X_test))

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


