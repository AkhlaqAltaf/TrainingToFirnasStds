from flask import jsonify
from model.model import BitcoiModel
class PredictionController:
    def __init__(self,request):
        self.open = request.get('Open')
        if self.validate_data:
            self.prediction()
        else :
            return jsonify("Inputs are not validated")
            
             
        pass
    def validate_data(self):
        if self.open > 234000:
            return False
        
        else:
            return True
        
    def prediction(self):
        self.preprocess()

        model = BitcoiModel()
        resp  = model.predict()
        return resp


        
        pass

    
    def preprocess():
        pass


            

