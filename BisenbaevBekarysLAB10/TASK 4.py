class LowScoreError(Exception):
    pass

def main():
    filename = "students.txt"

    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Name cannot be empty!")

    while True:
        try:
            grade = int(input("Enter student grade: ").strip())
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100!")
                continue

            if grade < 50:
                raise LowScoreError("Score too low! Student failed.")

            break

        except ValueError:
            print("Please enter a valid number!")
        except LowScoreError as e:
            print(f"Custom Exception: {e}")
            print("Grade rejected.")
            return

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{name}, {grade}\n")
        print("Grade accepted. Record added successfully!")

        print("\nUpdated file contents:")
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("File not found! Creating new file...")
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{name}, {grade}\n")
        print("Grade accepted. Record added successfully!")
        print("\nUpdated file contents:")
        print(f"{name}, {grade}")

if __name__ == "__main__":
    main()