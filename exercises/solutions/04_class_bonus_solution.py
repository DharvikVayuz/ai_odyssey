"""
Solution - Bonus exercises straight from class (see exercises.md)
=====================================================================
1. 5 students, formatted report lines with f-strings in a loop.
2. Right-angled triangle of stars using nested loops.
3. Marks for 5 subjects via input(), chained if/elif/else for a grade.
4. grade_report(name, marks_list) function.

Run this file and it will walk through all four, one after another.
"""

# --------------------------------------------------------------------
# 1. Five students, each a dictionary; print a formatted report line
#    for each one using an f-string inside a loop.
# --------------------------------------------------------------------
print("=== Exercise 1: Five students report ===")

students = [
    {"name": "Riya", "attendance_percent": 82, "is_eligible": True},
    {"name": "Aman", "attendance_percent": 68, "is_eligible": False},
    {"name": "Zoya", "attendance_percent": 95, "is_eligible": True},
    {"name": "Karan", "attendance_percent": 74, "is_eligible": False},
    {"name": "Meera", "attendance_percent": 88, "is_eligible": True},
]

for student in students:
    if student["is_eligible"]:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print(f"{student['name']} {student['attendance_percent']}% attendance, {status}")

# --------------------------------------------------------------------
# 2. Right-angled triangle of stars using nested loops - rows equal to
#    the number of letters in a name.
# --------------------------------------------------------------------
print("\n=== Exercise 2: Star triangle ===")

name = "Riya"          # 4 letters -> 4 rows
row_count = len(name)

for row in range(1, row_count + 1):   # outer loop: which row we're on
    line = ""
    for star in range(row):            # inner loop: how many stars this row
        line = line + "*"
    print(line)

# --------------------------------------------------------------------
# 3. Marks for 5 subjects via input(), then a chained if/elif/else
#    grade based on the average.
# --------------------------------------------------------------------
print("\n=== Exercise 3: Grade from 5 subjects (enter marks below) ===")

subject_marks = []
for subject_number in range(1, 6):
    mark = int(input(f"Enter marks for subject {subject_number}: "))
    subject_marks.append(mark)

subject_average = sum(subject_marks) / len(subject_marks)

if subject_average > 90:
    grade = "A"
elif subject_average > 75:
    grade = "B"
elif subject_average > 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Average: {subject_average:.2f} -> Grade: {grade}")


# --------------------------------------------------------------------
# 4. grade_report(name, marks_list) function, called for 3 students.
# --------------------------------------------------------------------
print("\n=== Exercise 4: grade_report() function ===")


def grade_report(student_name, marks_list):
    """Return a formatted 'name scored X average - Grade: Y' string."""
    average = sum(marks_list) / len(marks_list)

    if average > 90:
        grade = "A"
    elif average > 75:
        grade = "B"
    elif average > 50:
        grade = "C"
    else:
        grade = "Fail"

    return f"{student_name} scored {average:.1f} average - Grade: {grade}"


print(grade_report("Riya", [80, 75, 90]))
print(grade_report("Aman", [60, 55, 70]))
print(grade_report("Zoya", [95, 88, 92]))
