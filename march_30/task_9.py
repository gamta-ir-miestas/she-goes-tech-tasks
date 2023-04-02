# Write a Python program that reads a CSV file 
# containing student grades, calculates their average 
# score, and writes the average to a new file.

import csv

data = []

with open("student_grades.csv", "r") as f:
    csvlines = csv.reader(f, delimiter=',', quotechar='|')
    for row in csvlines:
        data.append(row)

data.pop(0)

with open("student_averages.csv", "w", newline='') as f:
    csvlines = csv.writer(f, delimiter=',')
    csvlines.writerow(['Name', 'Surname', 'Average'])
    for student in data:
        num1, num2, num3, num4, num5 = int(student[2]), int(student[3]), int(student[4]), int(student[5]), int(student[6])
        average = (num1 + num2 + num3 + num4 + num5) / 5
        csvlines.writerow([student[0], student[1], average])
