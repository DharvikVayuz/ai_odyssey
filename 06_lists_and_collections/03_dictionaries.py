"""
Lesson 6.3 - Dictionaries
============================
What we already know: a list keeps values in order, and we access them
by POSITION (marks[0]). A tuple bundles a couple of fixed values
together.

The problem: describing one whole student ("Riya", her marks, maybe her
attendance) using separate variables or lists is clunky - we've been
carrying student_name and marks around as two unrelated things this
whole course. What we really want is ONE box that holds everything
about Riya, labelled clearly.

New concept: a DICTIONARY stores values by NAME (called a "key")
instead of by position. { } curly braces, with "key": value pairs.
"""

# One student, described as a single dictionary. Compare this to
# juggling student_name + marks as two separate variables - everything
# about Riya now lives in one place.
riya = {
    "name": "Riya",
    "marks": [80, 75, 90],
    "attendance_percent": 92,
}

# Instead of an index number, we look things up by key name.
print("Name:", riya["name"])
print("Marks:", riya["marks"])
print("Attendance:", riya["attendance_percent"])

# We can still use everything we know about lists on the value stored
# inside the dictionary - riya["marks"] is a perfectly normal list.
average = sum(riya["marks"]) / len(riya["marks"])
print("Average:", average)

# Dictionaries can be updated by key, and new keys can be added later.
riya["is_passing"] = average >= 40
print("\nAfter adding is_passing:", riya)

# ---------- Many students: a list of dictionaries ----------
# This is exactly the shape we need for a real class report - each
# student is one dictionary, and all the students together are one list.
students = [
    {"name": "Riya", "marks": [80, 75, 90]},
    {"name": "Aman", "marks": [60, 55, 70]},
    {"name": "Zoya", "marks": [95, 88, 92]},
]

print("\n--- Class report ---")
for student in students:
    student_average = sum(student["marks"]) / len(student["marks"])
    print(f"{student['name']}: average = {student_average:.2f}")

# ---------- Finding the topper across all students ----------
topper_name = ""
topper_average = 0

for student in students:
    student_average = sum(student["marks"]) / len(student["marks"])
    if student_average > topper_average:
        topper_average = student_average
        topper_name = student["name"]

print(f"\nTopper: {topper_name} with an average of {topper_average:.2f}")

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Add "attendance_percent" to each student dictionary in "students".
# 2. Add a 4th student to the "students" list and re-run the class
#    report - it should include them automatically.
# 3. Loop through "students" and print only the students whose average
#    is below 40 (using the if/else skills from Lesson 3).
# --------------------------------------------------------------------
