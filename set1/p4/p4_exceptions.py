# Name: [RALPH DAINUEL SADIARIN] | Section: [IV-BSIT-B]
# Activity: P4 - Safe Menu Program | Date: [11/25/26]

def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        result = first / second
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Division operation finished.")

def read_file():
    filename = input("File name to open: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except PermissionError:
        print("You do not have permission to read that file.")
    else:
        print("\n--- FILE CONTENTS ---")
        print(contents if contents else "(The file is empty.)")
    finally:
        print("File operation finished.")

def main():
    while True:
        print("\nSAFE MENU")
        print("1. Divide two numbers")
        print("2. Open and display a text file")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            read_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu selection. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
