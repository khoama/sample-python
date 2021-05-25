"""This module is a sample to validate lint and pre-commit configuration."""
import abc


class Polygon(metaclass=abc.ABCMeta):
    """A class to represent polygons"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and
                callable(subclass.area) and
                hasattr(subclass, 'perimeter') and
                callable(subclass.perimeter) and
                hasattr(subclass, 'volume') and
                callable(subclass.volume))

    @abc.abstractmethod
    def num_sides(self) -> int:
        """This method returns the number of sides of the polygon"""
        raise NotImplementedError
