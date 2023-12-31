#!/usr/bin/python3
"""
It defines the Base classes for the entire AIRBNB Consol project
A module for all classes, it is a parent class.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """
    Base for all the classes in the entire project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__(self): prints the class name, id, and creates dictionary
        representations of the input values
        __save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
        __init__(self, *args, **kwargs)
        __repr__(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: uuid4, dates when class was created/updated
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return class name, id, and the dictionary
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """
        Instance method to:
        - update current datetime
        - invoke save() function &
        - save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
