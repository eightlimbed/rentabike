#!/usr/bin/python3
'''
This module contains the DBStorage class which holds all the attributes and
methods for a MySQL database storage engine.

    Attributes:
    -----------
    `__engine`: SQLAlchemy enginemaker
    `__session`: SQLAlchemy sessionmaker

    Methods:
    --------
    `all(self)`: Returns all objects in storage.
    `new(self, obj)`: Places a new object in the storage engine.
    `save(self)`: Saves an object to the database.
    `reload(self)`: Reloads all tables from the database and creates a session.
'''
import models
from models.city import City
from models.state import State
from models.category import Category
from models.base_model import Base
from models.user import User
from models.bike import Bike
from models.review import Review
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    '''
    DBStorage engine class. Contains the necessary attributes and methods
    required for a MySQL database engine using SQLAlchemy to map objects to
    database entries.
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        DBStorage instance constructor. Gets attribute values from environment
        variables.
        '''
        user = os.getenv('RENTABIKE_MYSQL_USER')
        password = os.getenv('RENTABIKE_MYSQL_PWD')
        host = os.getenv('RENTABIKE_MYSQL_HOST')
        database = os.getenv('RENTABIKE_MYSQL_DB')

        # Request a connection with the database once required
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)

        # Base gets some metadata when it is created (in models/base_model).
        # The metadata contains all the info we need to create the tables.
        Base.metadata.create_all(self.__engine)

        # If we are testing, we will drop all the tables.
        if os.getenv('RENTABIKE_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        # Start talking to the db
        Session = sessionmaker(bind=self.__engine)

        # Session is a SQLAlchemy class. self.__session is an instance.
        self.__session = Session()

    def all(self, cls=None):
        '''
        Queries all objects of a class in the database. If cls is None it
        will display all objects in the database.
        '''
        all_objects = {}
        if cls:
            instance = models.classes[cls.__name__]
            query = self.__session.query(instance).all()
            for obj in query:
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                all_objects[key] = obj
        else:
            db_list = [City, State, User, Category, Review, Bike]
            for cls in db_list:
                for obj in self.__session.query(cls).all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    all_objects[key] = obj
        return all_objects

    def new(self, obj):
        '''
        Adds an object to the current database session.
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commits an object to the current database session.
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes an object from the current database session.
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
        Reloads all tables in the database.
        '''
        user = os.getenv('RENTABIKE_MYSQL_USER')
        password = os.getenv('RENTABIKE_MYSQL_PWD')
        host = os.getenv('RENTABIKE_MYSQL_HOST')
        database = os.getenv('RENTABIKE_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, host, database),
                                      pool_pre_ping=True)
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        '''
        Ends the database session.
        '''
        self.__session.remove()
