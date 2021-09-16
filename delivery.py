from itertools import permutations
from element import Element


class Delivery:
    drone = None
    destinations = []

    def __init__(self):
        matrix_file = open("matrix.txt")
        text_matrix = matrix_file.readlines()

        coordinate_line = text_matrix[0]
        rows = int(coordinate_line[0])
        columns = int(coordinate_line[2])

        text_matrix.pop(0)

        rows_counter = 0
        while rows_counter < rows:
            current_matrix_row = text_matrix[rows_counter].split(' ')

            column_counter = 0
            while column_counter < columns:
                current_element = current_matrix_row[column_counter].strip()
                self.__create_element(current_element, rows_counter, column_counter)

                column_counter += 1
            rows_counter += 1

        matrix_file.close()

    def __create_element(self, element_id: str, abscissa: int, ordered: int) -> None:
        if element_id != '0':
            if element_id == 'R':
                self.drone = Element(element_id, abscissa, ordered)
            else:
                destination = Element(element_id, abscissa, ordered)
                self.destinations.append(destination)

    def get_shortest_path(self):
        paths = permutations(self.destinations)

        shortest_path = None
        shortest_path_length = None

        for path in paths:
            current_delivery = Element('R', self.drone.abscissa, self.drone.ordered)
            path_length = 0

            for destination in path:
                path_length += current_delivery.get_distance(destination)
                current_delivery.update_position(destination)

            if shortest_path_length is None:
                shortest_path_length = path_length
            elif path_length < shortest_path_length:
                shortest_path_length = path_length
                shortest_path = path

        return shortest_path
