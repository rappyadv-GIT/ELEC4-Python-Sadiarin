# Name: [RALPH DAINUEL SADIARIN] | Section: [IV-BSIT-B]
# Activity: P3 - Student Record Manager | Date: [11/25/26]

students = []  # List preserves the student names for display.
student_keys = set()  # Set provides fast, case-insensitive duplicate checking.

def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    key = name.casefold()
    if key in student_keys:
        print("That student is already in the records.")
    else:
        students.append(name)
        student_keys.add(key)
        print(f"Added: {name}")

def remove_student():
    name = input("Name to remove: ").strip()
    key = name.casefold()
    for existing in students:
        if existing.casefold() == key:
            students.remove(existing)
            student_keys.remove(key)
            print(f"Removed: {existing}")
            return
    print("Student not found.")

def search_student():
    query = input("Enter all or part of a name: ").strip().casefold()
    matches = [name for name in students if query in name.casefold()]
    if matches:
        print("Matches:")
        for name in sorted(matches, key=str.casefold):
            print("-", name)
    else:
        print("No matching student found.")

def display_students():
    print(f"\nStudents ({len(students)} total)")
    if not students:
        print("No student records yet.")
        return
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")

def main():
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("1. Add  2. Remove  3. Search  4. Display all  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

# A list is ordered and can contain repeated values; it is useful when the
# program needs to keep and display the student names. A set stores unique
# values and is useful for checking whether a name has already been added.
# This program uses a list for the records and a set of case-folded names
# to prevent duplicates such as Juan Cruz and juan cruz.
