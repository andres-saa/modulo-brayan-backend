from pydantic import BaseModel
from typing import Optional


class category_schema_post(BaseModel):
    # id: Optional[int]
    category_name: str
