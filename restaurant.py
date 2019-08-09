from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from PIL import Image
import pydotplus
import pandas as pd
import random

data = pd.read_csv('restaurant.csv')
feature_cols = ['Alternate','Bench','Hungry','Waiting','Costly','Rain','Reservation','Patrons']
# convert the string categorical values into an integer code using factorize method of the pandas library.
data['Alternate'],_ = pd.factorize(data['Alternate'])
data['Bench'],_ = pd.factorize(data['Bench'])
data['Hungry'],_ = pd.factorize(data['Hungry'])
data['Patrons'],_ = pd.factorize(data['Patrons'])
data['Costly'],_ = pd.factorize(data['Costly'])
data['Rain'],_ = pd.factorize(data['Rain'])
data['Reservation'],_ = pd.factorize(data['Reservation'])
data['Waiting'],_ = pd.factorize(data['Waiting'])

X = data[feature_cols]
y = data['Decision']

#Create the instance of DecisionTreeClassifier with max_depth = None i.e till leaf node & random_state=0 for maintaining state
tree_clf = DecisionTreeClassifier(max_depth=None, random_state=1)

#train the classifier
tree_clf.fit(X, y)

#input from user
print("enter 1 = Yes, 0 = No")
alternate = int(input("Is there any Alternate restaurant: "))
bench = int(input("Is there Bench to wait: "))
hungry = int(input("Are you Hungry: "))
rain = int(input("Is it Raining: "))
waiting = int(input("Is there Waiting: "))
costly = int(input("Is it Costly: "))
reservation = int(input("Do you have a Reservation: "))
patrons = int(input("Are there Patrons: "))
#predict
y_predict = tree_clf.predict([[alternate,bench,hungry,waiting,costly,rain,reservation,patrons]])
print("As per situaution it is better to",y_predict)

#visualization
dot_data = export_graphviz(tree_clf, out_file = None, 
	filled = True, rounded = True,	special_characters = True, 
	feature_names = feature_cols, class_names = data['Decision'])
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('output-tree.png')
decisionTree = Image.open('output-tree.png')
decisionTree.show()
