# Name: [RALPH DAINUEL SADIARIN] | Section: [IV-BSIT-B]
# Activity: P1 - Student Grade Calculator | Date: [11/24/26]

def accept_grades():
    """Collect one or more valid grades from the user."""
    grades = []
    while True:
        raw = input("Enter a grade from 0 to 100 (or Q to finish): ").strip()
        if raw.lower() == "q":
            if grades:
                return grades
            print("Enter at least one grade before finishing.")
            continue
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Invalid input. Enter a number or Q.")

def compute_average(grades):
    return sum(grades) / len(grades) if grades else 0

def get_highest(grades):
    return max(grades) if grades else None

def get_lowest(grades):
    return min(grades) if grades else None

def get_status(grades, passing_average=75):
    return "PASSED" if grades and compute_average(grades) >= passing_average else "FAILED"

def show_results(grades):
    if not grades:
        print("No grades have been entered.")
        return
    print("\n--- GRADE REPORT ---")
    print(f"Grades: {', '.join(f'{g:g}' for g in grades)}")
    print(f"Average: {compute_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print(f"Status: {get_status(grades)}")

def main():
    grades = []
    while True:
        print("\nSTUDENT GRADE CALCULATOR")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            grades = accept_grades()
        elif choice == "2":
            show_results(grades)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

# A local variable is created inside a function and can only be used there.
# For example, the variable grade inside accept_grades is local to that function.
# The variable grades inside main is also local to main, even though it is passed
# to other functions as an argument. A global variable is defined outside all
# functions and can be accessed throughout the module; this program avoids globals.
