"""
Solution - Intermediate exercises (see exercises.md)
=======================================================
1. Find the highest mark, without max().
2. Count how many subjects were passed (>= 40).
3. Calculate the average, without sum().
"""

marks = [80, 75, 90, 35, 62]

# 1. Highest mark, found by hand with a loop.
highest = marks[0]     # start by assuming the first mark is the highest
for mark in marks:
    if mark > highest:
        highest = mark
print("Highest mark:", highest)

# 2. Count how many subjects were passed.
passed_count = 0
for mark in marks:
    if mark >= 40:
        passed_count = passed_count + 1
print("Subjects passed:", passed_count, "out of", len(marks))

# 3. Average, found by hand with a loop (no sum()).
total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)
print("Average:", average)
