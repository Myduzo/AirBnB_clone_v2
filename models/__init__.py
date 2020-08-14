#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
from models.engine import file_storage
from models.engine import db_storage


if os.environ['HBNB_TYPE_STORAGE'] == "db":
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()
storage.reload()
