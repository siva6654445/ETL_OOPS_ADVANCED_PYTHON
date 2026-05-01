from pydantic import BaseModel,StrictInt,Field,EmailStr
from typing import Optional,Literal

class employee_schema(BaseModel):


    name :str = Field(...,min_length = 1 , max_length = 12)
    age : StrictInt = Field(...,gt= 17 , lt = 61)
    email : EmailStr = Field(...,description = "Employee's email address")
    department : Optional[str] = Field(None)
    gender : Literal['Male','Female','Shemale']


emp = employee_schema(
    name="siva",
    age=44,
    email="siva@gmail.com",
    gender="Male"
)

print(emp)
