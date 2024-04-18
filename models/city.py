#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ City class definition """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state_id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialization method for City class"""
        super().__init__(*args, **kwargs)
