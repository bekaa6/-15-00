def main():
    with open("cars.txt", "r", encoding="utf-8") as file:
        prices = []
        print("Автосалондағы көліктер:")
        print("-" * 35)
        for line in file:
            line = line.strip()
            if not line:
                continue
            model, price_str = line.split(",")
            model = model.strip()
            price_str = price_str.strip()
            try:
                price = int(price_str)
            except ValueError:
                print(f"Қате баға: {model} → '{price_str}'")
                continue
            print(f"{model:<20} {price} тг")
            prices.append(price)
    if prices:
        avg = sum(prices) / len(prices)
        print("-" * 35)
        print(f"Орташа баға: {avg:,.0f} тг")
    else:
        print("Дұрыс баға табылмады.")

if __name__ == "__main__":
    main()