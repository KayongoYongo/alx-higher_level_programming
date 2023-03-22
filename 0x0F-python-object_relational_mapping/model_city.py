#!/usr/bin/pythn3
"""Mapping python classes into columns"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Metadata
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """Class that defines each city
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
