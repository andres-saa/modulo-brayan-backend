from pydantic import BaseModel
from typing import Optional

class Produc_photo_schema_post(BaseModel):
    # id: Optional[int]
    image_url: str
    product_id: int