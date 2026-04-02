#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 2)

    def age(self) -> None:
        self._age = self._age + 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False
    
    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._bloomed == False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")
        
    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    print("=== Tree")
    print("=== Vegetable")
