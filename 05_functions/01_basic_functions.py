"""
Lesson 5.1 - Functions
=========================
What we already know: with a for loop, we can calculate the total and
average of any list of marks:
    total = 0
    for mark in marks:
        total = total + mark
    average = total / len(marks)

The problem: that's 4 lines of code. If we want the average for Riya,
AND for another student, AND for a whole class, we'd have to copy-paste
those same 4 lines every single time. And if we ever find a mistake in
the calculation, we'd have to fix it in every single copy.

New concept: a FUNCTION packages a set of steps under one name, so we
can reuse it any time just by calling that name - without rewriting the
steps.
"""


def calculate_average(marks):
    """Return the average of a list of marks."""
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


# Now the 4 lines of calculation logic exist in exactly ONE place. Every
# time we need an average, we just "call" the function by writing its
# name followed by parentheses, with the list we want inside them.
riya_marks = [80, 75, 90]
riya_average = calculate_average(riya_marks)
print("Riya's average:", riya_average)

# Because the logic lives inside the function, reusing it for a
# different student is now a single line - no copy-pasting needed.
aman_marks = [60, 55, 70]
aman_average = calculate_average(aman_marks)
print("Aman's average:", aman_average)

zoya_marks = [95, 88, 92]
zoya_average = calculate_average(zoya_marks)
print("Zoya's average:", zoya_average)

# --------------------------------------------------------------------
# Vocabulary:
# - "marks" (inside the parentheses in the def line) is called a
#   PARAMETER - a placeholder name for whatever list gets passed in.
# - "riya_marks" (what we actually passed in when calling the function)
#   is called an ARGUMENT.
# - "return" sends a value back out of the function, so we can store
#   it in a variable (like riya_average) or use it right away.
# --------------------------------------------------------------------

# A function can also just DO something without returning a value -
# that's fine too, as long as it has one clear job.
def print_report_line(name, average):
    """Print one formatted line for a student's report."""
    print(f"{name}: average = {average}")


print_report_line("Riya", riya_average)
print_report_line("Aman", aman_average)
print_report_line("Zoya", zoya_average)

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Call calculate_average() with a brand-new list of your own marks.
# 2. Write a function calculate_total(marks) that returns the sum of a
#    marks list (you can use Python's built-in sum() inside it).
# 3. Combine both: print a message like "Riya's total is 245 and her
#    average is 81.67" using calculate_total() and calculate_average().
# --------------------------------------------------------------------
