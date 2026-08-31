"""
Lesson 1.1 - Variables
=======================
Our story: Riya just gave her school exams. We want a Python program that
can remember her name and her marks in three subjects, so we can work
with them later.

A VARIABLE is like a labelled box. You put a value inside the box, and
you write a name on the box so you can find it again later.
"""

# We store the student's name in a variable.
# Think of "student_name" as a box with the word "student_name" written
# on it, and "Riya" is what we placed inside the box.
student_name = "Riya"

# Each of these is its own box, holding one number - the marks Riya
# scored in that subject.
math_marks = 80
science_marks = 75
english_marks = 90

# Once a value is stored in a variable, we can use the variable's name
# instead of retyping the value. Python will look inside the box for us.
print("Student name:", student_name)
print("Math marks:", math_marks)
print("Science marks:", science_marks)
print("English marks:", english_marks)

# Variables can also change what they hold - that is why they are called
# "variable" (able to vary). Let's say Riya's English paper gets re-checked
# and her marks go up.
english_marks = 92
print("\nAfter re-checking, English marks:", english_marks)

# --------------------------------------------------------------------
# TRY IT YOURSELF (see the README in this folder for the full list):
# 1. Change student_name to your own name.
# 2. Change the three marks to any numbers you like.
# 3. Run this file again and see the new output.
# --------------------------------------------------------------------
