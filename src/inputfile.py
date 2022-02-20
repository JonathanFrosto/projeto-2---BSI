import re

from src.exceptions import LayoutError
from src.util import strip_words


class InputFileReader:

    __matrix = []

    def __init__(self, file: str) -> None:
        with open(file) as matriz_file:
            self.__process_header_line(matriz_file.readline())
            self.__process_matrix_body(matriz_file)

    def __process_header_line(self, header_line: str) -> None:
        if not re.match('[0-9] [0-9]', header_line):
            raise LayoutError('Header line missing or in wrong layout')

        self.__rows, self.__columns = map(int, header_line.split())

    def __process_matrix_body(self, matriz_file) -> None:
        row_number = 0

        while row_number < self.__rows:
            current_row = strip_words(matriz_file.readline().split())

            if not len(current_row) == self.__columns:
                raise LayoutError(f'Current row {current_row} '
                                  f'do not match header line columns size of {self.__columns}')

            self.__matrix.append(current_row)
            row_number += 1

    def get_matrix(self) -> []:
        return self.__matrix
