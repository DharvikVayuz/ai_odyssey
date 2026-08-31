"""
Lesson 3.1 - Conditions (if / elif / else)
=============================================
What we already know: we can calculate Riya's total and average, and we
know comparison operators (like >=) give us a True/False answer.

The problem: knowing that "average >= 40" is True doesn't DO anything by
itself - it just sits there as a fact. We want the program to actually
react to that fact: print "Passed" or print "Failed".

New concept: if / else lets the program choose which lines of code to
run, based on whether a condition is True or False.
"""

student_name = "Riya"
math_marks = 80
science_marks = 75
english_marks = 90

total = math_marks + science_marks + english_marks
average = total / 3

# ---------- Simple if / else ----------
print(f"{student_name}'s average: {average}")

if average >= 40:
    print(f"{student_name} passed!")
else:
    print(f"{student_name} failed.")

# Notice the indentation (the spaces before print()) - Python uses
# indentation to know which lines belong INSIDE the if, and which lines
# come after it. This is different from many other languages.

# ---------- Levelling up: if / elif / else for a grade ----------
# A plain pass/fail is fine, but real report cards use grades. elif
# means "else, if this next condition is true" - Python checks each
# condition top to bottom and stops at the first one that matches.
print()  # blank line for readability

if average > 90:
    grade = "A"
elif average > 75:
    grade = "B"
elif average > 50:
    grade = "C"
else:
    grade = "Fail"

print(f"{student_name}'s grade: {grade}")

# --------------------------------------------------------------------
# Why the ORDER of elif matters: Python checks top to bottom and stops
# at the first True condition. If we had written "average > 50" BEFORE
# "average > 90", then a student with average = 95 would incorrectly
# get grade "C", because 95 > 50 is already True and Python would never
# even look at the ">90" check. Always order elif from most specific
# (highest) to least specific (lowest) when the ranges overlap like this.
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Change average to a low number like 30 and re-run - does it
#    correctly print "Fail"?
# 2. Add an elif for grade "A+" when average > 95, above the "A" check.
# 3. Add a separate if that checks a single subject (e.g. math_marks)
#    and prints "Needs improvement in Math" if it's below 40.
# --------------------------------------------------------------------
