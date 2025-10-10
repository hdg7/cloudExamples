from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str
        
class BatchInput(BaseModel):
    texts: List[str]

class Feedback(BaseModel):
    text: str
    predicted: str
    true_label: str
                                
