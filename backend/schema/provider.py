from pydantic import BaseModel
from typing import Optional


class provider_schema_post(BaseModel):
    # id: Optional[int]
    provider_name: str
    provider_address: str
    provider_contact: str
    provider_nit: str 