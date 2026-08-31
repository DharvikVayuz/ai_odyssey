"""
Lesson 5.2 - More on Parameters
==================================
What we already know: calculate_average(marks) takes one parameter and
returns one value.

New concept: a function can take MORE than one parameter, and a
parameter can have a DEFAULT VALUE - a value it uses automatically if
the caller doesn't provide one. Let's turn our pass/fail and grading
logic from Lesson 3 into reusable functions too.
"""


def calculate_average(marks):
    """Return the average of a list of marks."""
    total = 0
    for mark in marks:
        total = total + mark
    return total / len(marks)


def check_pass_fail(average, passing_marks=40):
    """Return 'Pass' or 'Fail' based on the average.

    passing_marks has a DEFAULT of 40, so most of the time we can call
    this with just the average. But if one school uses a different
    passing mark, we can still override it.
    """
    if average >= passing_marks:
        return "Pass"
    else:
        return "Fail"


def get_grade(average):
    """Return a letter grade based on the average - same rules as Lesson 3."""
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    elif average > 50:
        return "C"
    else:
        return "Fail"


# ---------- Using the functions together ----------
riya_marks = [80, 75, 90]
riya_average = calculate_average(riya_marks)

# Default passing_marks (40) is used automatically here:
riya_result = check_pass_fail(riya_average)
riya_grade = get_grade(riya_average)

print(f"Riya's average: {riya_average}")
print(f"Riya's result: {riya_result}")
print(f"Riya's grade: {riya_grade}")

# ---------- Overriding a default parameter ----------
# Some schools set the passing mark at 50 instead of 40. Because
# passing_marks has a default, we only need to mention it when it's
# actually different from the default.
strict_result = check_pass_fail(riya_average, passing_marks=50)
print(f"\nWith a stricter passing mark of 50: {strict_result}")

# ---------- Putting it all together for several students ----------
# Two lists, kept lined up by position: student_names[0] goes with
# all_marks[0], student_names[1] with all_marks[1], and so on.
# (Lesson 6 introduces a tidier way to pair a name with its marks -
# a dictionary - but plain lists already get the job done.)
student_names = ["Riya", "Aman", "Zoya"]
all_marks = [
    [80, 75, 90],
    [60, 55, 70],
    [30, 25, 45],
]

print("\n--- Class report ---")
for i in range(len(student_names)):
    name = student_names[i]
    marks = all_marks[i]
    average = calculate_average(marks)
    result = check_pass_fail(average)
    grade = get_grade(average)
    print(f"{name}: average={average:.2f}, result={result}, grade={grade}")

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Call check_pass_fail() for a student with a low average, and
#    confirm it correctly returns "Fail".
# 2. Add a new student to BOTH student_names and all_marks (same
#    position in each list) and re-run.
# 3. Write a function called count_passed(marks) that takes a list of
#    marks and returns how many individual subjects were >= 40.
# --------------------------------------------------------------------
