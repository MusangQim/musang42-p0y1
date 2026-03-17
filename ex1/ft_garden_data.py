class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print(f"{p1.name}: {p1.height}cm, {p1.age} days old")
    print(f"{p2.name}: {p2.height}cm, {p2.age} days old")
    print(f"{p3.name}: {p3.height}cm, {p3.age} days old")


if __name__ == "__main__":
    main()
