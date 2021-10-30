'''
@Author ---> Bibek Rawat
'''

from flask import Flask,request,render_template
import pickle
from datetime import datetime



app=Flask(__name__)

#loading the model
model=pickle.load(open('Housing_Model','rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/',methods=['POST'])
def predict():
    try:
         '''
        Required input for machine learning model
        1. tradeTime
        2. followers
        3. square
        4. livingRoom
        5. drawingRoom
        6. kitchen
        7. bathRoom
        8. constructionTime
        9. communityAverage
        10. renovationCondition
        11. buildingStructure
        12. elevator
        '''
         #syntax-->  var_name=request.form['<name which in present in html form(index.html)>']
         query_tradetime=request.form['tradetime']
         query_followers=request.form['followers']
         query_square=request.form['square']
         query_livingroom=request.form['livingroom']
         query_drawingroom=request.form['drawingroom']
         query_kitchen=request.form['kitchen']
         query_bathroom=request.form['bathroom']
         query_constructiontime=request.form['constructiontime']
         query_communityaverage=request.form['communityaverage']
         query_renovationcondition=request.form['renovationcondition'] #Categorical Data
         query_buildingstructure=request.form['buildingstructure'] #Categorical Data
         query_elevator=request.form['elevator'] #Categorical Data

         if query_tradetime<query_constructiontime:
             return render_template('index.html')


         #For renovation condition
         if query_renovationcondition=="renovationCondition_1":
            renovationCondition_2=0
            renovationCondition_3=0
            renovationCondition_4=0
         elif query_renovationcondition=="renovationCondition_2":
            renovationCondition_2=1
            renovationCondition_3=0
            renovationCondition_4=0
         elif query_renovationcondition=="renovationCondition_3":
            renovationCondition_2=0
            renovationCondition_3=1
            renovationCondition_4=0
         else:
            renovationCondition_2=0
            renovationCondition_3=0
            renovationCondition_4=1


        # For building structure
         if query_buildingstructure=="buildingStructure_1":
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_2":
            buildingStructure_2=1
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_3":
            buildingStructure_2=0
            buildingStructure_3=1
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_4":
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=1
            buildingStructure_5=0
            buildingStructure_6=0
         elif query_buildingstructure=="buildingStructure_5":
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=1
            buildingStructure_6=0
         else:
            buildingStructure_2=0
            buildingStructure_3=0
            buildingStructure_4=0
            buildingStructure_5=0
            buildingStructure_6=1
        
        # For elevator
         if query_elevator=="elevator_0":
            elevator_1=0
         else:
            elevator_1=1

         model_data=[[query_tradetime,query_followers,query_square,query_livingroom,
                    query_drawingroom,query_kitchen,query_bathroom,query_constructiontime,
                    query_communityaverage,renovationCondition_2,renovationCondition_3,renovationCondition_4,
                    buildingStructure_2,buildingStructure_3,buildingStructure_4,buildingStructure_5,
                    buildingStructure_6,elevator_1]]
        
         result=model.predict(model_data)
         x=float(result)
         y="{:.3f}".format(x)

         return render_template('index.html',results=y)


    except ValueError:
        return render_template('index.html')
   

if __name__=="__main__":
    app.run(debug=True)






