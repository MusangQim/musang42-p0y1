#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
    
    def bloom(self) -> None:


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
