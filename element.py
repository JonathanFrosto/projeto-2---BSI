from __future__ import annotations


class Element:
    def __init__(self, identification: str, x: int, y: int):
        self.id = identification
        self.abscissa = x
        self.ordered = y

    def get_distance(self, other_element: Element) -> int:
        return abs(self.abscissa - other_element.abscissa) + abs(self.ordered - other_element.ordered)

    def __str__(self) -> str:
        return self.id

    def update_position(self, element: Element) -> None:
        self.abscissa = element.abscissa
        self.ordered = element.ordered
