#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.bloom = bloom

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int) -> None:
        super().__init__(name, height, age)
        self.
