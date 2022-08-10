from pydantic import BaseModel


class AtoiInput(BaseModel):
    input_str: str
