#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.start = height
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


    def grow(self) -> None:
        self.height = round(self.height + 0.8, 2)


    def age(self) -> None:
        self.days = self.days + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    for x in range(1, 8):
        print(f"=== Day {x} ===")
        rose.show()
        rose.grow()
        rose.age()
    growth = round(rose.height - rose.start)
    print(f"Growth this week: {growth}cm")
