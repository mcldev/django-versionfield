from .constants import DEFAULT_NUMBER_BITS
from .utils import convert_version_string_to_int, convert_version_int_to_string


class Version(object):
    def __init__(self, string, number_bits=DEFAULT_NUMBER_BITS):
        """
        Take in a verison string e.g. '3.0.1'
        Store it as a converted int
        """
        self.number_bits = number_bits
        self.internal_integer = convert_version_string_to_int(string, number_bits)

    def __str__(self):
        return str(convert_version_int_to_string(
                   self.internal_integer, self.number_bits))

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.internal_integer

    def __eq__(self, other):
        if not other:
            return False  # we are obviously a valid Version, but 'other' isn't
        if other == Ellipsis:
            return False # For pydantic use
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return int(self) == int(other)

    def __hash__(self):
        return int(self)

    def __lt__(self, other):
        if not other:
            return False
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return int(self) < int(other)

    def __le__(self, other):
        if not other:
            return False
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return int(self) <= int(other)

    def __gt__(self, other):
        if not other:
            return False
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return int(self) > int(other)

    def __ge__(self, other):
        if not other:
            return False
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return int(self) >= int(other)

    # Added Add + and Subtract - so 1.0.1 + 2.0.1 = 3.0.2 etc. Subtracting is max of 0.0.0
    def __add__(self, other):
        if not other:
            return self
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return Version(convert_version_int_to_string(int(self) + int(other), self.number_bits), self.number_bits)


    def __sub__(self, other):
        if not other:
            return self
        if isinstance(other, str):
            other = Version(other, self.number_bits)
        return Version(convert_version_int_to_string(max(int(self) - int(other), 0), self.number_bits), self.number_bits)
