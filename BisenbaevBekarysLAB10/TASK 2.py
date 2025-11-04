def main():
    filename = "cars.txt"
    model = input("Көлік моделін енгізіңіз: ")
    price = input("Бағасын (тек сан) енгізіңіз: ")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{model}, {price}\n")
    print("Көлік қосылды!")
    print("\nАвтосалондағы барлық көліктер:")
    print("-" * 45)
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())
    print("-" * 45)

if __name__ == "__main__":
    main()