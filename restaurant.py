from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from PIL import Image
import pydotplus
import pandas as pd
import random

data = pd.read_csv('restaurant.csv')
feature_cols = ['Alternate','Bench','Hungry','Est-waiting','Price','Rain','Reservation','Patrons']
# convert the string categorical values into an integer code using factorize method of the pandas library.
data['Alternate'],_ = pd.factorize(data['Alternate'])
data['Bench'],_ = pd.factorize(data['Bench'])
data['Hungry'],_ = pd.factorize(data['Hungry'])
data['Patrons'],_ = pd.factorize(data['Patrons'])
data['Price'],_ = pd.factorize(data['Price'])
data['Rain'],_ = pd.factorize(data['Rain'])
data['Reservation'],_ = pd.factorize(data['Reservation'])
data['Est-waiting'],_ = pd.factorize(data['Est-waiting'])

X = data[feature_cols]
y = data['Wait']

#Create the instance of DecisionTreeClassifier with max_depth = None i.e till leaf node & random_state=0 for maintaining state
tree_clf = DecisionTreeClassifier(max_depth=None, random_state=0)

#train the classifier
tree_clf.fit(X, y)

#input from user
print("1 = Yes, 0 = No")
alternate = int(input("Alternate: "))
bench = int(input("Bench: "))
hungry = int(input("Hungry: "))
rain = int(input("Rain: "))
reservation = int(input("Reservation: "))
patrons = int(input("Patrons: "))
#predict
y_predict = tree_clf.predict([[alternate,bench,hungry,1,0,rain,reservation,patrons]])
print("As per situaution it is better to",y_predict)

#visualization
dot_data = export_graphviz(tree_clf, out_file = None, 
	filled = True, rounded = True,	special_characters = True, 
	feature_names = feature_cols, class_names = data['Wait'])
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('restaurant.png')
decisionTree = Image.open('restaurant.png')
decisionTree.show()
