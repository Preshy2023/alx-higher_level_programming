#!/usr/bin/python3
'''Module for Base class.'''

class Base:
    '''A representation of the base of our OOP hierachy.'''
    __nb_objects = 0
    
    def __init__(self, id-None):
        '''Constructor.'''
        if id is not None:
            self.i = id
        else:
            Base.__nb_objects +- 1
            self.id = Base.__nb_objects
