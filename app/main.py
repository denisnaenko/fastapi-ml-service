from fastapi import FastAPI
from .schemas import IrisRequest, IrisResponse
from .predict import make_prediction

app = FastAPI(title="Iris Classifier API")

@app.get("/")
def root():
    return {"message": "ML model is ready"}

@app.post("/predict", response_model=IrisResponse)
def predict(request: IrisRequest):
    result = make_prediction(request.data)
    return IrisResponse(prediction=result)
