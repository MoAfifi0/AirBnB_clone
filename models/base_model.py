#!/usr/bin/python3
"""
A module that implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initialize the BaseModel class

        Attributes:
            id(string):unique identifier
            created_at(datetime): when the instance created
            updated_at(datetime): when the instance updated
        """
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        return a dict containing all keys/values of __dict__ of the instance
        """
        to_dect = dict({"__class__": type(self).__name__})
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = datetime.isoformat(value)
            to_dect[key] = value
        print(to_dect)
        print("----------")
        print(self.__dict__)
        return (to_dect)
