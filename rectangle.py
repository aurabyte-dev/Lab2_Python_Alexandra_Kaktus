
   
"""
A class representing a rectangle and it's position.

Attributes:
    - width (float): The with of the rectangle -> read-only
    - height (float): The height of the rectangle -> read only
    - area (float): The area of the rectangle -> read only 
    - x (float): The x-coordinate of the rectangles center 
    - y (float): The y-coordinate of the rectangles center
    - perimeter (float): The perimiter of the rectangle -> read-only

"""

from shape import Shape
from utils import validate_positive_number

class Rectangle(Shape): 

    # Initializing a rectangle
    def __init__(self, x=0, y=0, width=1, height=1): # with and height 1 because we need a positive number
        super().__init__(x, y)
        self.width = width
        self.height = height
    
    @property
    def width(self):
        # Getting the width
        return self._width
    
    @width.setter
    def width(self, value):
        # Validate and set the width
        self._width = validate_positive_number(value, "width")
    
    @property
    def height(self):
        # Getting the height
        return self._height
    
    @height.setter
    def height(self, value):
        # Validate and set the height
        self._height = validate_positive_number(value, "height")

    @property
    def area(self):
        # Calculate the area: width * height
        return self.width * self.height
    
    @property
    def perimeter(self):
        # Calculate the perimeter: 2 * (width + height)
        return 2 * (self.width + self.height)
    
    def is_square(self):
        # Check if the rectangle is a square (width == hight)
        return self.width == self.height
    
    def __str__(self):
        return f"This rectangle has it's center at ({self.x}, {self.y}), width {self.width} and height {self.height}"
    
    def __repr__(self):
        return f"Rectangle_coordinates(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
