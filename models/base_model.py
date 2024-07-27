#!/usr/bin/python3
"""Modules for the base model."""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class of the base model."""

    def __init__(self, *args, **kwargs):
        """Class constructor."""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for i, j in kwargs.items():
                while i != "__class__":
                    if i == "created_at":
                        self.created_at = datetime.fromisoformat(j)
                    elif i == "updated_at":
                        self.updated_at = datetime.fromisoformat(j)
                    else:
                        setattr(self, i, j)

    def __str__(self):
        """Return string representation."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save updates of upadates_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation."""
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
