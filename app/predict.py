from .model import model

def make_prediction(data):
    prediction = model.predict([data])
    return int(prediction[0])
