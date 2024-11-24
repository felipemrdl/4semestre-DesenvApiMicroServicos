from pydantic import BaseModel
from typing import Any

class ResponseObject(BaseModel):
  status: bool
  detalhes: str
  dados: Any