from pydantic import BaseModel
from typing import List

class IrisRequest(BaseModel):
    data: List[float]

class IrisResponse(BaseModel):
    prediction: int
