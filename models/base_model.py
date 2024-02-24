#!/usr/bin/python3
'''Creates a class that defines all common attributes/methods for
other classes'''

import uuid
from datetime import datetime


class BaseModel:
    '''Class that defines all common attributes/methods
        for other classes
    '''
    def __init__(self):
        '''Initialize BaseModel instance'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''Return a string representation of the object'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)

    def save(self):
        '''Updates the public instance attribute updated_at with the
        current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containig all key/values of __dict__'''
