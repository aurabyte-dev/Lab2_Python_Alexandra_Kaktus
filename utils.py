"""
Function for validating that value is a number.

"""

def validate_number(value, name):
    if not isinstance(value,(int, float)):
        raise TypeError(f"{name} must be a number, not {type(value)}")
    return float(value)


"""
Function for validating that a value is a positive number.

"""

def validate_positive_number(value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be anumber, not {type(value)}")
    if value <= 0 =:
        raise ValueError(f"{name} must be positive")
    return float(value)
