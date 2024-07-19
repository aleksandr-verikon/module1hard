grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()

print(students)

grades_mean = []
for grade in grades:
    grades_mean.append(sum(grade) / len(grade))
print(grades_mean)
result_dict = {}
for student, grade_mean in zip(students, grades_mean):
    result_dict[student] = grade_mean

print(result_dict)


