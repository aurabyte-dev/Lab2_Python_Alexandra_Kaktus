"""
Base class for geometric shapes.

"""
from utils import validate_number

class Shape:

    # Initialize shape with x and y center coordinates.
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self): 
        # Get the x-coordinate
        return self._x
    
    @x.setter
    def x(self, value): 
        # Validate before setting x
        self._x = validate_number(value, "x")

    
    @property
    def y(self):
        return self._y # Get the y-coordinate
    
    @y.setter 
    def y(self, value):
        # Validate before setting y
        self._y = validate_number(value, "y")
    
    def translate(self, dx, dy):
        # Move the shape by dx and dy
        dx = validate_number(dx, "dx")
        dy = validate_number(dy, "dy")

        self._x += dx
        self._y += dy

    def __eq__(self, other):
        # Check if two shapes are equal (have the same area)
        if not isinstance(other, Shape):
            return False
        return self.area == other.area

    def __lt__(self, other):
        # Check if this shapes area is smaller than the other
        return self.area < other.area
    
    def __le__(self, other):
        # Check if this shape is smaller than or equal to another
        return self.area <= other.area
    
    def __gt__(self, other):
        # Check if this shapes is larger than another
        return self.area > other.area
    
    def __ge__(self, other):
        # Check if this shape is larger than or equal to another
        return self.area >= other.area
