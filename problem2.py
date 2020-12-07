"""
Name: problem2.py

Purpose: A program that computes the number of fried chicken shared with students and Mr.Fabroa

Author: Huang.K

Date created: 7/12/2020
"""

print("\no-o-o[Chicken Leftovers Calculator]o-o-o")

# Input the amount of students and the amount of chicken bought
number_of_students = float(input("\nEnter number of students: "))
fried_chicken = int(input("Enter amount of fried chicken bought: "))

# Compute the amount of fried chicken for each students 
# and how much fried chicken Mr.Fabroa gets
chicken_per_student = fried_chicken / number_of_students
leftovers_for_fabroa = fried_chicken % number_of_students

# Output the amount of chicken per student and leftovers for Mr.Fabroa
print("\n", chicken_per_student, "pieces of fried chicken per student.")
print("\n", leftovers_for_fabroa, "pieces of fried chicken leftovers for Mr. Fabroa!")