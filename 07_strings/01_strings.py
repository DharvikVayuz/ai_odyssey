"""
Lesson 7.1 - Strings
=======================
What we already know: we've been using text (strings) since Lesson 1 -
student names, subject names, dictionary keys - and we've printed them
using commas inside print(), like: print("Name:", riya["name"])

The problem: print("Name:", riya["name"]) is fine for quick debugging,
but it's clunky for a real report line. We want something that reads
like "Riya scored 81.67 average - Grade: B", built by mixing text and
numbers smoothly, not just comma-separated pieces.

New concept: f-strings (formatted strings) let us build one clean
string by dropping variables directly inside { } braces, and lets us
control exactly how numbers are displayed (like rounding to 2 decimals).
"""

name = "Riya"
marks = [80, 75, 90]
average = sum(marks) / len(marks)

# ---------- f-strings: the modern way to build a message ----------
# Put an "f" right before the opening quote, then use { } to drop any
# variable (or even a small expression) directly into the text.
report_line = f"{name} scored {average} average"
print(report_line)

# We can control number formatting inside the { } with a colon.
# ":.2f" means "as a float, with exactly 2 digits after the decimal."
report_line = f"{name} scored {average:.2f} average"
print(report_line)

# ---------- Useful string methods ----------
print("\n--- String methods ---")
print(name.upper())     # ALL CAPS
print(name.lower())     # all lowercase
print("  hindi  ".strip())   # removes leading/trailing spaces -> "hindi"
print(len(name))        # length works on strings too, not just lists!

# ---------- Combining strings (concatenation) ----------
greeting = "Hello, " + name + "!"     # + joins strings end to end
print("\n" + greeting)

# f-strings usually read more clearly than + for anything with more
# than one variable - compare:
greeting_fstring = f"Hello, {name}!"
print(greeting_fstring)

# ---------- Building the kind of report line we actually want ----------
attendance_percent = 92
is_eligible = attendance_percent >= 75

if is_eligible:
    status = "Eligible"
else:
    status = "Not Eligible"

formatted_report = f"{name} {attendance_percent}% attendance, {status}"
print("\n" + formatted_report)

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Build an f-string report line that includes name, average
#    (rounded to 1 decimal with :.1f), and a Pass/Fail result.
# 2. Use .upper() to print the student's name in capital letters as a
#    "banner" before the report line.
# 3. Try len() on a sentence, not just a name - what does it count?
# --------------------------------------------------------------------
