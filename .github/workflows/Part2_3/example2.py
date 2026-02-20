import numpy as np


def area_circ(r_in):
    """Calculate the area of a circle with given radius.

    :Input: The radius of the circle (float, >=0).
    :Returns: The area of the circle (float)."""
    if r_in < 0:
        raise ValueError("The radius must be >= 0.")
    circle = np.pi * r_in**2
    print(f"""The area of a circle with radius r = {r_in:3.2f}cm is A = {circle:4.2f}cm2.""")
    return circle


if __name__ == "__main__":
    _ = area_circ(5.0)
