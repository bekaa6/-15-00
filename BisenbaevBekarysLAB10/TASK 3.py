def main():
    filename = "cars.txt"

    while True:
        model = input("Көлік моделін енгізіңіз: ").strip()
        if model:
            break
        print("Модель бос болмауы керек!")

    while True:
        price_input = input("Бағасын (тек сан, теңге) енгізіңіз: ").strip()
        if not price_input:
            print("Баға бос болмауы керек!")
            continue
        try:
            price = int(price_input)
            if price < 1000000:
                print("Баға кемінде 1 000 000 теңге болуы керек!")
                continue
            break
        except ValueError:
            print("Қате! Тек сан енгізіңіз.")

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{model}, {price}\n")
        print("Көлік сәтті қосылды!")

        print("\nАвтосалондағы барлық көліктер:")
        print("-" * 50)
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if lines:
                for line in lines:
                    print(line.strip())
            else:
                print("(салон бос)")
        print("-" * 50)

    except FileNotFoundError:
        print("Файл табылмады! Жаңасын жасап жатырмын...")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{model}, {price}\n")
        print("Көлік сәтті қосылды!")
        print("\nАвтосалондағы барлық көліктер:")
        print("-" * 50)
        print(f"{model}, {price}")
        print("-" * 50)

    except Exception as e:
        print(f"Күтпеген қате: {e}")

    finally:
        print("Бағдарлама аяқталды.")

if __name__ == "__main__":
    main()