# Name: [RALPH DAINUEL SADIARIN] | Section: [IV-BSIT-B]
# Activity: P2 - Custom Module student_utils | Date: [11/24/26]

import student_utils
from datetime import datetime
from student_utils import calculate_average, determine_status

def read_grades():
    grades = []
    while True:
        value = input("Enter grade 0-100 (Q to finish): ").strip()
        if value.lower() == "q":
            if grades:
                return grades
            print("Enter at least one grade.")
            continue
        try:
            grade = float(value)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    grades = read_grades()
    print("\nSTUDENT REPORT")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # from student_utils import ... style:
    print(f"Average: {calculate_average(grades):.2f}")
    print("Status:", determine_status(grades))
    # import student_utils style:
    print("Highest:", student_utils.highest_grade(grades))
    print("Lowest:", student_utils.lowest_grade(grades))

if __name__ == "__main__":
    main()
