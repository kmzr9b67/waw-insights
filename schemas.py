from pydantic import BaseModel


class InfoBase(BaseModel):
    id: int
    District: str
    Crimes: float
    Density: float
    Green_space: float

    class Config:
        orm_mode = True


