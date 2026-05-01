### class creation and import it 

from pydantic import BaseModel
from pydantic import StrictInt

class emp_1(BaseModel):
    emp_id : StrictInt
    emp_name : str
    dept : str



