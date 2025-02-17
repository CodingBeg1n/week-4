'''

For this assignment please do the following:

- Read in the student_grades.csv file

- calculate the average grade for the class

- for each student record calculate the difference between the student's grade and the average grade

- write the output to a new file called student_grade_differences.csv

'''
import csv

with open('student_grades.csv','r') as f:

    # collect all lines from the file
    lines = f.readlines()
    if len(lines) > 0:
        grades = []
        for line in lines[1:]:
            row = line.split(',')
            grades.append(float(row[3].replace('\n','')))
        avg = sum(grades) / len(grades)
        
        differences = []

        for line in lines[1:]:
            row = line.split(',')
            grade = float(row[3].replace('\n', ''))
            difference = grade - avg
            differences.append([row[0], grade, difference])

with open('grade_differences','w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['StudendID', 'Grade', 'Difference'])
    writer.writerows(differences)
