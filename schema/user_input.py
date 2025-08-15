from pydantic import BaseModel,Field, computed_field,field_validator
from typing import Annotated,Literal

class InsuranceInput(BaseModel):
    """
    Pydantic model to define the input data structure for insurance premium prediction.
    """
    age: Annotated[int, Field(..., gt=0, description="Age of the primary beneficiary.")]
    sex: Annotated[Literal['Male','Female'],Field(..., description="Gender of the beneficiary (male or female).")]
    height: Annotated[float, Field(...,gt=0 ,description="Height of the beneficiary")]
    weight: Annotated[float, Field(...,gt=0,lt=3.5, description="Weight of the beneficiary")]
    income_USD: Annotated[float,Field(...,gt=0,description="Annual salary of the beneficiary")]
    children: Annotated[int, Field(..., ge=0, description="Number of children covered by the insurance.")]
    smoker: Annotated [bool, Field(..., description="Smoker status (True or False).")]
    region: Annotated[str, Field(..., description="The beneficiary's residential region.")]

    @field_validator('region')
    @classmethod
    def format_region(cls, region:str) -> str:
        region = region.split().title()
        return region
    
    @computed_field
    @property
    def bmi(self)-> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def life_risk(self)->str:
        if self.smoker and self.bmi >30:
            return "high"
        if self.smoker and self.bmi >25:
            return "medium"
        else:
            return "low"





