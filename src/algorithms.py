import re
from abc import ABC, abstractmethod

from src.coordinate import Coordinate
from src.util import permutations


class FlyFoodRouting(ABC):

    @abstractmethod
    def get_shortest_path(self):
        pass


class BruteForce(FlyFoodRouting):

    __destinations = []
    __drone = None
    __shortest_path_cost = None
    __shortest_path_permutation = None

    def __init__(self, matrix: []) -> None:
        row_number = 0
        colum_number = 0

        for row in matrix:

            for column in row:
                if 'R' == column:
                    self.__drone = Coordinate(row_number, colum_number, column)
                elif re.match('[A-Z]', column):
                    self.__destinations.append(Coordinate(row_number, colum_number, column))

                colum_number += 1

            row_number += 1
            colum_number = 0

    def get_shortest_path(self):

        if self.__shortest_path_cost is None and self.__shortest_path_permutation is None:
            drone_origin = Coordinate(0, 0, 'origin')
            drone_origin.goto(self.__drone)

            for permutation in permutations(self.__destinations.copy()):

                current_cost = 0
                for destination in permutation:
                    current_cost += self.__drone.goto(destination)

                current_cost += self.__drone.goto(drone_origin)

                if self.__shortest_path_cost is None or current_cost < self.__shortest_path_cost:
                    self.__shortest_path_cost = current_cost
                    self.__shortest_path_permutation = permutation

        print(f'Shortest path: {"-".join(map(str,self.__shortest_path_permutation))}\n'
              f'Cost: {self.__shortest_path_cost}')
