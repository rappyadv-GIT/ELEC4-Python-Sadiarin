# Name: [RALPH DAINUEL SADIARIN] | Section: [IV-BSIT-B]
# Activity: P2 - Custom Module student_utils | Date: [11/24/26]

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def determine_status(grades, passing_average=75):
    return "PASSED" if grades and calculate_average(grades) >= passing_average else "FAILED"

def highest_grade(grades):
    return max(grades) if grades else None

def lowest_grade(grades):
    return min(grades) if grades else None
