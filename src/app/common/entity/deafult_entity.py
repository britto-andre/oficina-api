from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field

PyObjectId = Annotated[str, BeforeValidator(str)]

class DefaultEntity (BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    
    excluded: bool = Field(default=None)
    created_time: datetime = Field(default=None)
    # created_user: str = Field(default=None)
    
    version: int = Field(default=None)

    def model_post_init(self, *args, **kwargs):
        if self.excluded == None: self.excluded = False
        if self.created_time == None: self.created_time = datetime.now()
        if self.version == None: self.version = 0