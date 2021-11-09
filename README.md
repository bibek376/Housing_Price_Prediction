# Housing_Price_Prediction

## Installation Guide
1. Clone or Fork the Project
2. Create a Virtual Enviroment
3. go to same virtual enviroment and write below cmd
4. pip install -r requirements.txt



## Table Of Content
1. [Project Descriptiom](https://www.kaggle.com/ruiqurm/lianjia)<br>
    A. Problem Statement<br>
    B. Best Possible Solutions<br>
    C. Introduction About Project<br>
    D. Tools and Libraries
2. [Data Collection](https://www.kaggle.com/ruiqurm/lianjia)
3. [EDA]()
4. [Choosing Best ML Model]()
5. [Model Creation]()
6. [Model Deployment]()
7. [Model Conclusion]()
8. [Project Innovation]()
9. [Limitation And Next Step]()



### 1. Project Description
#### A. Problem Statement

Thousands of houses are sold everyday. There are some questions every buyer asks himself like: What is the actual price that this house deserves? Am I paying a fair price?

#### B. Best Possible Solutions
a.Housing Expert<br>
b.Intuition About House<br>
c.Using Machine Learning

#### C. Introduction About Project
House Price prediction are very stressful work as we have to consider different things while buying a house like the structure and the rooms kitchen parking space and gardens. 
People don’t know about the factor which influence the house price.
But by using the Machine learning we can easily find the house which is to be prefect for us and helps to predict the price accurately.

#### D. Tools and Libraries
Tools<br><br>
a.Python<br>
b.Jupyter Notebook<br>

Libraries<br><br>
a.Pandas<br>
b.Scikit Learn<br>
c.Numpy<br>
d.Seaborn<br>
e.Matpoltlib<br>



### 2. Data Collection
For this project we used the data that is available on kaggle.([click here for data](https://www.kaggle.com/ruiqurm/lianjia)).There are 26 columns and 318851 Rows. These are the major point about the data set.<br>
url: the url which fetches the data<br>
id: the id of transaction<br>
Lng: and Lat coordinates, using the BD09 protocol.<br>
Cid: community id<br>
tradeTime: the time of transaction<br>
DOM: active days on market<br>
followers: the number of people follow the transaction.<br>
totalPrice: the total price<br>
price: the average price by square<br>
square: the square of house<br>
livingRoom: the number of living room<br>
drawingRoom: the number of drawing room<br>
kitchen: the number of kitchen<br>
bathroom the number of bathroom<br>
floor: the height of the house. I will turn the Chinese characters to English in the next version.<br>
buildingType: including tower( 1 ) , bungalow( 2 )，combination of plate and tower( 3 ), plate( 4 ).<br>
constructionTime: the time of construction<br>
renovationCondition: including other( 1 ), rough( 2 ),Simplicity( 3 ), hardcover( 4 )<br>
buildingStructure: including unknow( 1 ), mixed( 2 ), brick and wood( 3 ), brick and concrete( 4 ),steel( 5 ) and steel-concrete composite ( 6 ).<br>
ladderRatio: the proportion between number of residents on the same floor and number of elevator of ladder. It describes how many ladders a resident have on average.<br>
elevator: have ( 1 ) or not have elevator( 0 )<br>
fiveYearsProperty: if the owner have the property for less than 5 years.<br>


### 3. EDA
![alt_text](https://github.com/bibek376/Housing_Price_Prediction/blob/master/Picture_For_README/1.png)
#### A.Data Cleaning
we have 26 columns ,from these we don't want some column then we will perform data cleaning wich involve following steps.<br>
a. Impute/Remove missing values or Null values (NaN)
b. Remove unnecessary and corrupted data.
c. Date/Text parsing if required.



































































































