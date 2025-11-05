"""
Test file for Sphere class to test functionalities.

"""
from pytest import raises
from sphere import Sphere
import math

# 1. Test creating a sphere
def test_sphere_creation():
    s = Sphere(x=2, y=3, z=5, radius=10)
    assert s.x == 2 and s.y ==3 and s.z == 5 and s.radius == 10

# 2. Calculate surface area 
def test_surface_area():
    s = Sphere(radius=3)
    # by using abs(absolute value) it checks if the values are “close enough”.
    assert abs(s.surface_area - 4 * math.pi * 3**2) < 0.0001

# 3. Calculate volume 
def test_volume():
    s = Sphere(radius=3)
    assert abs(s.volume - (4/3) * math.pi * 3**3) < 0.0001

# 4. Check if sphere is unit sphere
def test_is_unit_sphere():
    s1 = Sphere(x=0, y=0, z=0, radius=1)
    assert s1.is_unit_sphere() is True

    s2 = Sphere(x=1, y=0, z=2, radius = 3)
    assert s2.is_unit_sphere() is False

# 5. Moving the circle
def test_translate():
    s = Sphere(x=0, y=0, z=0, radius=9)
    s.translate(10, 12, 14)
    assert s.x == 10 and s.y == 12 and s.z == 14

# 6. Compairing two different sphere
def test_comparison():
    s1 = Sphere(radius=1)
    s2 = Sphere(radius=5)
    assert s1 < s2

# 7. Error handling
def test_type_error(): # -> TypeError
    with raises(TypeError):
        Sphere(radius="eight")

def test_value_error(): # -> ValueError
    with raises(ValueError):
        Sphere(radius=-2)
