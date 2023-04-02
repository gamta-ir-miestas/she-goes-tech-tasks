# Write a Python program that reads a CSV file 
# containing student grades and writes a new CSV file 
# with the grades sorted by student name.

import csv

data = []

with open("student_grades.csv", "r") as f:
    csvlines = csv.reader(f, delimiter=',', quotechar='|')
    for row in csvlines:
        data.append(row)

data.pop(0)

# concatenating name and surname in case there are 2 people with the same name
student_names = []
for name in data:
    student_names.append(name[0] + " " + name[1])

sorted_names = sorted(student_names)

lst = []
for name in sorted_names:
    lst.append(name.split())

final = []
for name in lst:
    for student in data:
        if name[0] == student[0]:
            final.append(student)

with open("students_sorted.csv", "w", newline='') as f:
    csvlines = csv.writer(f, delimiter=',')
    csvlines.writerow(['Name', 'Surname', 'Grade 1', 'Grade 2', "Grade 3", "Grade 4", "Grade 5"])
    for student in final:
        csvlines.writerow(student)