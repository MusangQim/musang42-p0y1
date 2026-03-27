#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


    def show(self) -> None:
        print(self.name)


    def grow(self) -> None:
        self.height = height + 0.8


    def age(self) -> None:
        self.age = age + 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    for days in range(7):
        print(f"=== Day: {days} ===")
        print(f"{rose.show}: {rose.grow}cm, {rose.age} days old")
    print("Growth this week: 6cm")
