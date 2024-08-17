class Model:
    def __init__(self,low , open):
        self.open= open
        self.low = low

    def predict(self):
        load = picke.load_model(...)
        load.predict(self.open,self.close)

