"""
Lesson 1.2 - Data Types
========================
What we already know: we can store Riya's name and marks in variables.

New concept: every value in Python has a TYPE - it tells Python (and us)
what *kind* of value is inside the box. Using the right type matters,
because Python treats numbers and text differently.
"""

student_name = "Riya"
math_marks = 80
science_marks = 75
english_marks = 90

# str  -> text ("string" of characters), always written in quotes
# int  -> a whole number, no decimal point
# float -> a number that has a decimal point
# bool -> only two possible values: True or False

# Python's built-in type() function tells us the type of any value.
print("student_name is a:", type(student_name))
print("math_marks is a:", type(math_marks))

# A float shows up when a number has a decimal point.
average_marks = 81.5
print("average_marks is a:", type(average_marks))

# A bool is a yes/no, true/false value. Here we ask Python a question,
# and it hands back True or False - that answer IS the bool.
is_passing = math_marks >= 40
print("is_passing is a:", type(is_passing))
print("Is Riya passing in Math?", is_passing)

# --------------------------------------------------------------------
# Why this matters: input() (next lesson) always gives us a string, even
# if the user types a number. If we try to do maths on a string, Python
# will refuse. So we need to be able to recognise types, and convert
# between them on purpose using int(), float(), and str().
# --------------------------------------------------------------------
marks_as_text = "80"          # this looks like a number, but it's a string
print("\nmarks_as_text is a:", type(marks_as_text))

marks_as_number = int(marks_as_text)   # int() converts text -> whole number
print("marks_as_number is a:", type(marks_as_number))
print("marks_as_number + 5 =", marks_as_number + 5)

# str() does the opposite - it turns a number into text, useful when
# joining a number into a sentence.
marks_message = "Math marks: " + str(math_marks)
print(marks_message)

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Print the type() of science_marks and english_marks.
# 2. Create a new bool variable called is_topper that checks if
#    math_marks >= 90, and print it.
# 3. Convert "75" (a string) into a number and add 10 to it.
# --------------------------------------------------------------------
