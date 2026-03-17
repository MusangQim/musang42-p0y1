class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def main():
    print("=== Garden Plant Registry===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    print(p1.name, ":", p1.height, "cm", p1.age, "days old")
    print(p2.name, ":", p2.height, "cm", p2.age, "days old")
    print(p3.name, ":", p3.height, "cm", p3.age, "days old")

if __name__ == "__main__":
    main()
