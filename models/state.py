#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if storage_type == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, *args, **kwargs):
        """Initialization method for State class"""
        super().__init__(*args, **kwargs)
