from typing import Any, NewType


NonNegativeInt = NewType("NonNegativeInt", int)


def validate_int(value: Any) -> int:
    if not isinstance(value, int):
        raise TypeError(f"{value} is not int")
    return value


def validate_non_negative_int(value: Any) -> NonNegativeInt:
    value = validate_int(value)
    if value < 0:
        raise ValueError(f"{value} is negative")
    return value
