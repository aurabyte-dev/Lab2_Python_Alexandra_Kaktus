"""
Base class for 2D geometric shapes.
"""

class Shape:

    # 1. Initialize shape with x and y center coordinates.
    def __init__(self, x=0, y=0):

    @property
    def x(self): # Get the x-coordinate
        return self._x
    
    @x.setter
    def x(self, value): 
    # Validate before setting x
        if not isinstance
