"""
Solution - Challenge exercises (see exercises.md)
====================================================
1. Store multiple students as a list of dictionaries.
2. Calculate each student's average.
3. Determine who scored the highest.
"""


def calculate_average(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


# 1. Multiple students, each one a dictionary with a name and marks list.
students = [
    {"name": "Riya", "marks": [80, 75, 90]},
    {"name": "Aman", "marks": [60, 55, 70]},
    {"name": "Zoya", "marks": [95, 88, 92]},
    {"name": "Karan", "marks": [45, 39, 50]},
]

# 2. Each student's average, printed as we go.
topper_name = ""
topper_average = -1

for student in students:
    average = calculate_average(student["marks"])
    print(f"{student['name']}: average = {average:.2f}")

    # 3. Keep track of whoever has the highest average so far.
    if average > topper_average:
        topper_average = average
        topper_name = student["name"]

print(f"\nTopper: {topper_name} with an average of {topper_average:.2f}")
