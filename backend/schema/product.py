from pydantic import BaseModel
from typing import Optional

class Product_schema_post(BaseModel):
    # id:Optional[int]
    product_name:str
    product_description:str
    product_purchase_price:int
    product_selling_price:int
    


