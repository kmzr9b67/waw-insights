from sqlalchemy import Column, String, Float
from app.database import *

class InfoWaw(Base):
    __tablename__ = "info"
    District = Column(String(50), primary_key=True)
    Crimes = Column(Float)
    Density = Column(Float)
    Green_space = Column(Float)




