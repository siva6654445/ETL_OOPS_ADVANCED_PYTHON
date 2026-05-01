from pyspark.sql.functions import *
from pyspark.sql.types import *

from pydantic import BaseModel

class employee_schema(BaseModel):
    name :str
    id : int
    depatment : str
    salary :float

obj = employee_schema(name='virat', id = 106, depatment='bat',salary= 7000)
print(obj)

obj1 = employee_schema(**{"name":"viat","id":"108","depatment":"bata","salary":"787878"})
print(obj1)  #'''above eventhough we passed differnt vales which is not valid data types it accepets and is called coherence'''

## strictint

from pydantic import StrictInt

class emp1(BaseModel):
    id :StrictInt
    name : str

obj2 = emp1(**{"id":'45',"name":"siva"})
print(obj2)
#in above case it failed due to the usage of strictint

