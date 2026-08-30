# GWA Calculator - Calculate Grade Weighted Average

import re

# Lists to store subject information
subject_list = []
grade_list = []
subject_unit_list = []
weighted_grades = []
total_units = 0
total_grade = 0

# Add a new subject with its grade and units
def Add_Subject(subject, grade, units):
    subject_list.append(subject)
    grade_list.append(grade)
    subject_unit_list.append(units)
    return

# Remove a subject by its index
def Remove_Subject(index):
    subject_list.pop(index)
    grade_list.pop(index)
    subject_unit_list.pop(index)

# Calculate the sum of all grades
def calculate_total_grade():
    global total_grade
    count = len(grade_list)
    for i in range(count):  # Fixed: changed count() to range(count)
        total_grade += grade_list[i]
    return

# Calculate the sum of all units
def calculate_total_units():
    global total_units
    count = len(subject_unit_list)
    for i in range(count):  # Fixed: changed count to range(count)
        total_units += subject_unit_list[i]
    return

# Calculate weighted grade (GWA) by dividing total units by total grades
def calculate_weighted_grade():
    weighted_grades =  total_units / total_grade
    return weighted_grades

# Retry the main system
def try_again():
    return main_system()

# Main menu system for user interaction
def main_system():
    while True:
        choice = int(input("""
(1)Add Subject
(2)Remove Subject
(3)Show All Subject Details
(4)Calculate GWA
(5)Retry
(6)Exit
Choice: """))
        if choice == 1:
            subject = input("Input Subject: ")
            grade = float(input("Input Grade: "))
            unit = int(input("Input Units: "))
            Add_Subject(subject, grade, unit)
            
        elif choice == 2:
            # Display all subjects with their index for removal
            count = 0
            for i in subject_list:
                print(f"""

Count\t\tSubject\t\tGrade\t\tUnits
{count}\t\t{subject_list[count]}\t\t{grade_list[count]}\t\t{subject_unit_list[count]}
""")
                count += 1
                
            index = int(input("Count of Subject to Remove: "))
            Remove_Subject(index)
        elif choice == 3:
            # Display all subjects with their grades and units
            count = 0
            for i in subject_list:
                print(f"""

Subject\t\tGrade\t\tUnits
{subject_list[count]}\t\t{grade_list[count]}\t\t{subject_unit_list[count]}
""")
                count += 1
                 
        elif choice == 4:
            # Calculate and display GWA
            calculate_total_grade()
            calculate_total_units()
            GWA = calculate_weighted_grade()
            print(f"""
Total Grade: {total_grade}
Total Units: {total_units}
GWA: {GWA}
""")            
            
        elif choice == 5:
            main_system()
            
        elif choice == 6:
            return 0
        else:
            print("Invalid Choice")
            main_system()

# Calls Main system for it to run
main_system()
