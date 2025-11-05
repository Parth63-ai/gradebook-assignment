"""
---------------------------------------------------------
Title      : GradeBook Analyzer
Course     : Programming for Problem Solving using Python
Student    : Kumar Partha
Date       : 05-11-2025
Description: A CLI program to analyze and report student grades.
---------------------------------------------------------
"""
import csv
import statistics

#---------- Task 1: Setup----------

def welcome_message():
    print("Welcome to the GradeBook Analyzer")
    print("This program analyzes student grades from a CSV file.")
    print("1. Enter the student data manually")
    print("2. Upload a CSV file")
    print("3. Exit")
    print("Choose an option (1-3): ", end='')

#---------- Task 2:Data Entry ----------

def manual_data_entry():
    marks = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score
    return marks



def upload_csv_file():
    marks = {}
    file_path = input("Enter the path to the CSV file: ").strip()
    with open(file_path, mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            score = float(row[1])
            marks[name] = score
    return marks

#---------- Task 3:Statistical Functions ----------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)


def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())


def find_max_score(marks_dict):
    return max(marks_dict.values())


def find_min_score(marks_dict):
    return min(marks_dict.values())

#---------- Task 4: Grade assignment and distribution ----------

def assign_grades(marks_dict):
    grades = {}
    for name,score in marks_dict.items():
        if score >=90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    distribution = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        distribution[grade] += 1
    return distribution

#---------- Task 5: Pass/Fail filter ----------

def filter_pass_fail(marks_dict):
    pass_students = {name for name, score in marks_dict.items() if score>= 50}
    fail_students = {name for name, score in marks_dict.items() if score< 50}
    return pass_students, fail_students

#---------- Task 6: Display Results ----------

def display_results(marks_dict,grades):
    print("\nName\tscore\tgrade")
    for name,score in marks_dict.items():
        print(f"{name:<10}{score:<10}{grades[name]}")

def show_statistics(marks_dict):
    print("\n --- Analysis Summary ---")
    print(f"Average Marks: {calculate_average(marks_dict)}")
    print(f"Median Marks : {calculate_median(marks_dict)}")
    print(f"Highest Score: {find_max_score(marks_dict)}")
    print(f"Lowest Score : {find_min_score(marks_dict)}")


def show_grade_distribution(distribution):
    print("\n --- Grade Distribution ---")
    for grade, count in distribution.items():
        print(f"{grade}: {count} student(s)")

def show_pass_fail(passed, failed):
    print("\n Passed Students:", len(passed))
    print(", ".join(passed))
    print(" Failed Students:", len(failed))
    print(", ".join(failed))

#---------- Main Program Loop ----------
def main():
    while True:
        welcome_message()
        choice = input()
        if choice == '1':
            marks_dict = manual_data_entry()
        elif choice == '2':
            marks_dict = upload_csv_file()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        # Perform calculations
        grades = assign_grades(marks_dict)
        distribution = grade_distribution(grades)
        passed, failed = filter_pass_fail(marks_dict)

        # Display results
        display_results(marks_dict, grades)
        show_statistics(marks_dict)
        show_grade_distribution(distribution)
        show_pass_fail(passed, failed)

        again = input("\n Do you want to check again? (yes/no): ").lower()
        if again == 'yes':
            continue
        else:
            print("Exiting the program. Goodbye!")
            break

        # End of main loop
if __name__ == "__main__":
    main()