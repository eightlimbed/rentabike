#!/usr/bin/python3
"""
Database engine.
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, category, city, bike, review, state, user


class DBStorage:
    """
    Handles long term storage of all class instances.
    """
    CNC = {
        'Category': category.Category,
        'City': city.City,
        'Bike': bike.Bike,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the database connection.
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('RENTABIKE_MYSQL_USER'),
                os.environ.get('RENTABIKE_MYSQL_PWD'),
                os.environ.get('RENTABIKE_MYSQL_HOST'),
                os.environ.get('RENTABIKE_MYSQL_DB')))
        if os.environ.get("RENTABIKE_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects.
        """
        obj_dict = {}
        if cls is not None:
            a_query = self.__session.query(DBStorage.CNC[cls])
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
            return obj_dict

        for c in DBStorage.CNC.values():
            a_query = self.__session.query(c)
            for obj in a_query:
                obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
                obj_dict[obj_ref] = obj
        return obj_dict

    def new(self, obj):
        """
        Adds objects to current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of current database session.
        """
        self.__session.commit()

    def rollback_session(self):
        """
        Rollsback a session in the event of an exception.
        """
        self.__session.rollback()

    def delete(self, obj=None):
        """
        Deletes an object from current database session if not None.
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def delete_all(self):
        """
        Deletes all stored objects (for testing purposes).
        """
        for c in DBStorage.CNC.values():
            a_query = self.__session.query(c)
            all_objs = [obj for obj in a_query]
            for obj in range(len(all_objs)):
                to_delete = all_objs.pop(0)
                to_delete.delete()
        self.save()

    def reload(self):
        """
        Creates all tables in database & session from engine.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
        Closes the current database session.
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieves one object based on class name and id.
        """
        if cls and id:
            fetch = "{}.{}".format(cls, id)
            all_obj = self.all(cls)
            return all_obj.get(fetch)
        return None

    def count(self, cls=None):
        """
        Returns the count of all objects in storage
        """
        return len(self.all(cls))
