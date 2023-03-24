from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor_Final.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = 0
    
    # return "Hello World"

    if request.method == 'POST':
        
        OverallQual = request.form['OverallQual']
        GrLivArea = request.form['GrLivArea']
        MSZoning = request.form['MSZoning']
        SaleType = request.form['SaleType']
        SaleCondition = request.form['SaleCondition']
        GarageType = request.form['GarageType']
        LotShape = request.form['LotShape']
        HouseStyle = request.form['HouseStyle']
        

        feature_list = []

        feature_list.append(int(OverallQual))
        feature_list.append(int(GrLivArea))

        MSZoning_list = ['RL','RM','FV','RH','C']
        SaleType_list = ['WD' , 'New' , 'COD' , 'Other']
        SaleCondition_list = ['Normal','Partial','Abnorml','Family', 'Alloca' , 'AdjLand']
        GarageType_list = ['Attchd','Detchd','BuiltIn','Other']
        LotShape_list = ['Reg','IR1','IR2','IR3']
        HouseStyle_list = ['1Story','2Story','1.5Fin ','SLvl','SLvl','Other']
       


        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)

        traverse_list(MSZoning_list, MSZoning)
        traverse_list(SaleType_list, SaleType)
        traverse_list(SaleCondition_list, SaleCondition)
        traverse_list(GarageType_list, GarageType)
        traverse_list(LotShape_list, LotShape)
        traverse_list(HouseStyle_list, HouseStyle)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0])

       

    
    return render_template('my.html',pred_value = pred_value)


if __name__ == '__main__':
    app.run(debug=True)