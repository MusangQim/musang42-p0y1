#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height = round(self._height, 2)

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
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self._height = round(self._height + 2.1, 2)
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {int(self._nutritional_value)}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    for x in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
