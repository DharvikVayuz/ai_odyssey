"""
Lesson 2.1 - Getting Input from the User
==========================================
What we already know: we can store Riya's marks in variables, and we know
that every value has a type.

The problem: right now, Riya's marks are typed directly into the code.
    math_marks = 80
If we want to record a DIFFERENT student's marks, we would have to open
the code and edit it every single time. That's not how a real program
should work - the person using it should be able to type their own marks
in while the program is running.

New concept: input() pauses the program and waits for the user to type
something and press Enter. Whatever they type comes back as a string.
"""

# input() always shows the message we give it, then waits for the user.
student_name = input("Enter the student's name: ")

# input() ALWAYS returns a string - even if the user types "80".
# So if we want to do maths with it later, we must convert it to a
# number using int() (whole numbers) or float() (decimal numbers).
math_marks = int(input("Enter Math marks: "))
science_marks = int(input("Enter Science marks: "))
english_marks = int(input("Enter English marks: "))

print("\n--- Recorded ---")
print("Student:", student_name)
print("Math:", math_marks)
print("Science:", science_marks)
print("English:", english_marks)

# --------------------------------------------------------------------
# Why the int() matters: try removing int() from one of the lines above
# and run the program. Python will store the marks as text, and later
# lessons that do maths on them (like adding marks together) will
# either crash or behave strangely (Python would "glue" numbers
# together as text instead of adding them).
# --------------------------------------------------------------------
