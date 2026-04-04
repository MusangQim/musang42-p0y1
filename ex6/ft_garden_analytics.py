#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow,"
                  f" {self._age_count} age,"
                  f" {self._show_count} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def grow(self) -> None:
        self._height = round(self._height + 8.0, 2)
        self._stats._grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._stats._age_count += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        self._stats._show_count += 1

    @staticmethod
    def ageofplant(age: int) -> bool:
        return age > 365

    @classmethod
    def info_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)


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
        if not self._bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height}cm long and {self._trunk_diameter}cm wide.")
        self._stats._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 2)
        self._stats._grow_count += 1
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._stats._grow_count += 1 

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {int(self._nutritional_value)}")

class Seed(Flower):
    def __init__(self, name: str, height: float, 
                 age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 2)
        self._stats._grow_count += 1

    def age(self) -> None:
        self._age += 20
        self._stats._age_count += 1

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_stats(plant) -> None:
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print(" === Check year-old")
    print(f"Is 30 days more than a year? "
          f"-> {Plant.ageofplant(30)}")
    print(f"Is 400 days more than a year? "
          f"-> {Plant.ageofplant(400)}")
    
    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)


    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower._seeds = 42
    sunflower.show()
    display_stats(sunflower)
    
    print()
    print("=== Anonymous")
    unknown = Plant.info_anonymous()
    unknown.show()
    display_stats(unknown)
