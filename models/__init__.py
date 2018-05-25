#!/usr/bin/python3
'''
This file is the initializer for the Models module. It imports all Models and
the storage engine and creates a 'global' dictionary of all models. Upon each
initialization the `storage.reload()` method gets called which will read the
contents from storage and populate `FileStorage.__objects` with the deserialized
version of all objects.
'''

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.bike import Bike
from models.state import State
from models.city import City
from models.category import Category
from models.review import Review
import os


'''
CNC = { Class Name (string) : Class Type }
'''

if os.environ.get('RENTABIKE_TYPE_STORAGE') == 'db':
    from models.engine import db_storage
    CNC = db_storage.DBStorage.CNC
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    CNC = file_storage.FileStorage.CNC
    storage = file_storage.FileStorage()

storage.reload()
