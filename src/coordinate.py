from __future__ import annotations


class Coordinate:

    def __init__(self, x: int, y: int, description: str) -> None:
        self.__abscissa = x
        self.__ordinate = y
        self.__description = description

    def goto(self, coordinate: Coordinate) -> int:
        distance = self.__distance(coordinate)

        self.__abscissa = coordinate.__abscissa
        self.__ordinate = coordinate.__ordinate

        return distance

    def __distance(self, coordinate: Coordinate) -> int:
        return abs(self.__abscissa - coordinate.__abscissa) + abs(self.__ordinate - coordinate.__ordinate)

    def __repr__(self) -> str:
        return self.__description
