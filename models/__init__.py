#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine import db_storage, file_storage


if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()
storage.reload()
