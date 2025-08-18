from pydantic import BaseModel, Field
from typing import Dict

class PredicitonResponse(BaseModel):
    predicted_premium: str = Field(...,description ='The predicted insurance premium category',example = "High")
    confidence : float = Field (..., description ='Model confidence score about the prediction',example = 0.634)
    class_probabilities: Dict[str, float] = Field(..., description = 'Probabilities distribution across all output classes', example={'Low': 0.2,'Medium':0.1,'High':0.7})
