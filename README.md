# Restaurant-problem-decision_tree
Code Language - Python (version - 2 & 3)
Problem to wait for a table at a restaurant. A decision tree decides whether to wait or not in a given situation.
this is the basic implementation of it, dataset contains only 13 samples in total, as it is a very small dataset i have'nt splitted it and neither calculated the Entropy,
the code takes input from user, and based on that it predicts that one should wait or not.   
for running the code follow the steps.
## 1) Download dependencies.

windows/linux:-   
**python -m pip install scikit-learn   
python -m pip install pillow   
python -m pip install pandas   
python -m pip install random2 (random in linux)      
python -m pip install pydotplus**   
   
for visualising the graph we need to install Graphviz   
In Linux:- **sudo apt-get install graphviz**   
In Windows:- open **Windows PowerShell(Admin)** - copy and paste the below lines 

**Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))**  

wait.......after installation is completed, type the below command to install Graphviz   
**choco install Graphviz**   
and enter y when asked    

## 2) Download the csv [restaurant.csv]
## 3) Run the code
  
## Output:-
![output](https://github.com/akhtarnadeem915/Restaurant-problem-decision_tree/blob/master/output.png)
![output tree](https://github.com/akhtarnadeem915/Restaurant-problem-decision_tree/blob/master/output-tree.png)
