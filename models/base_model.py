#!/usr/bin/python3
"""Gather data for each model."""
import uuid
import datetime


class BaseModel:
    """Class of project."""
    def __init__(self):
        """Class constructor."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at attribute."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Converts input into dictionary."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary
