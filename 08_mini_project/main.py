"""
Mini Project - Student Marks Manager
=======================================
This is where every lesson comes together into one real program.

What we already know, and where it came from:
  - Lesson 1 (Variables & Data Types): student names and marks live in
    variables with the right type (str, int, float, bool).
  - Lesson 2 (Input & Operators):      input() collects data from the
    user; +, /, and comparisons calculate totals and averages.
  - Lesson 3 (Conditions):             if/elif/else decides Pass/Fail
    and assigns a letter grade.
  - Lesson 4 (Loops):                  for loops repeat work across
    every subject, and across every student.
  - Lesson 5 (Functions):              the average/grade/pass-fail
    logic is packaged into reusable functions, written ONCE.
  - Lesson 6 (Lists & Dictionaries):   each student is a dictionary
    {"name": ..., "marks": [...]}, and all students live in one list.
  - Lesson 7 (Strings):                f-strings build the final,
    nicely formatted report.

The program: Student Marks Manager
  1. Ask how many students to record.
  2. For each student, ask for their name and marks in 3 subjects.
  3. Store everything as a list of dictionaries.
  4. Calculate each student's total, average, grade, and pass/fail.
  5. Print a full report using f-strings.
  6. Find and announce the topper of the class.
"""

SUBJECTS = ["Math", "Science", "English"]
PASSING_MARKS = 40


def calculate_total(marks):
    """Return the sum of a list of marks. (Lesson 5 + Lesson 6)"""
    total = 0
    for mark in marks:
        total = total + mark
    return total


def calculate_average(marks):
    """Return the average of a list of marks. (Lesson 5)"""
    return calculate_total(marks) / len(marks)


def get_grade(average):
    """Return a letter grade for an average. (Lesson 3, as a function)"""
    if average > 90:
        return "A"
    elif average > 75:
        return "B"
    elif average > 50:
        return "C"
    else:
        return "Fail"


def check_pass_fail(average, passing_marks=PASSING_MARKS):
    """Return 'Pass' or 'Fail' based on the average. (Lesson 3 + 5)"""
    if average >= passing_marks:
        return "Pass"
    else:
        return "Fail"


def collect_student():
    """Ask the user for one student's name and marks, and return it as
    a dictionary - the same shape we built in Lesson 6."""
    name = input("\nEnter student name: ")

    marks = []
    for subject in SUBJECTS:
        mark = int(input(f"  Enter {subject} marks: "))
        marks.append(mark)

    return {"name": name, "marks": marks}


def build_report_line(student):
    """Turn one student dictionary into a formatted report line.
    (Lesson 7 - f-strings)"""
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    result = check_pass_fail(average)

    return (
        f"{student['name']}: total={total}, "
        f"average={average:.2f}, grade={grade}, result={result}"
    )


def find_topper(students):
    """Return the student dictionary with the highest average.
    (Lesson 4 loop + Lesson 6 list of dictionaries)"""
    topper = None
    topper_average = -1

    for student in students:
        average = calculate_average(student["marks"])
        if average > topper_average:
            topper_average = average
            topper = student

    return topper, topper_average


def main():
    print("=== Student Marks Manager ===")
    print(f"Subjects recorded for every student: {', '.join(SUBJECTS)}")

    student_count = int(input("\nHow many students do you want to enter? "))

    students = []
    for student_number in range(student_count):
        students.append(collect_student())

    print("\n--- Class Report ---")
    for student in students:
        print(build_report_line(student))

    topper, topper_average = find_topper(students)
    print(f"\nTopper: {topper['name']} with an average of {topper_average:.2f}")


# Run the program.
main()
