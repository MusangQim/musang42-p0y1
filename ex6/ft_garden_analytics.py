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
        self._height = round(self._height + 1.5, 2)
        self._stats._grow_count += 1

    def age(self) -> None:
        self._age += 1
        self._stats.age_count += 1

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

class Seed(Flower):
    def __init__(self, name: str, height: float, 
                 age: int, color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print(" === Check year-old")
    print(f"Is 30 days more than a year? "
          f"-> {Plant.ageofplant(30)}")
    print(f"Is 400 days more than a year? "
          f"-> {Plant.ageofplant(400)}")
    
    print()
    print("=== Flower")
    
    print()
    print("=== Tree")
    
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    
    print()
    print("=== Anonymous")
    unknown = Plant.info_anonymous()
    unknown.show()
