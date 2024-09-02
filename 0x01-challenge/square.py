#!/usr/bin/python3

class Square:
    """Class representing a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    def area_of_my_square(self):
        """Calculate the area of the square."""
        return self.size * self.size

    def perimeter_of_my_square(self):
        """Calculate the perimeter of the square."""
        return self.size * 4

    def __str__(self):
        """Return a string representation of the square."""
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    # Create a square with size 12
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
