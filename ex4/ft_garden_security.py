#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Plant created: {self.name}: {self.height}cm, {self.age} days old")

    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            print("Accepted")

    def get_height(self) -> float:
        return self.height

    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print("Accepted")

    def get_age(self) -> int:
        return self.age

if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    rose.set_height(25)
    print(rose.get_height())
    rose.set_age(30)
    print(rose.get_age())
