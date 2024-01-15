#!/usr/bin/python3
"""
The BaseModel class defines all common attributes/methods for other classes.
"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """Defines all common attributes/methods for other classes.

    Attributes:
    id: unique id for each instance.
    created_at: date of creation.
    updated_at: date of last instance update.
    """

    def __init__(self, *args, **kwargs):
        """Inits BaseModel with id, creation and update dates."""
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
    
    def __str__(self):
        """Prints [<class name>] (<self.id>) <self.__dict__>"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
    
    def save(self):
        """Updates the updated_at with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        for k, v in self.__dict__.items():
            if k == 'created_at':
                my_dict[k] = self.created_at.isoformat()
            elif k == 'updated_at':
                my_dict[k] = self.updated_at.isoformat()
            else:
                my_dict[k] = v
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
