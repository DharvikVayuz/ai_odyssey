"""
Lesson 2.2 - Operators
========================
What we already know: we can store marks in variables, either typed
directly into the code or entered by the user with input().

New concept: OPERATORS are the symbols Python uses to do maths and to
compare values - +, -, *, /, and more. Let's use them to finally
calculate something useful from Riya's marks: her total and her average.
"""

student_name = "Riya"
math_marks = 80
science_marks = 75
english_marks = 90

# ---------- Arithmetic operators (maths) ----------
total = math_marks + science_marks + english_marks     # + adds
average = total / 3                                    # / divides (always gives a float)

print(f"{student_name}'s total marks:", total)
print(f"{student_name}'s average marks:", average)

# A few more arithmetic operators, shown on small examples:
print("\n--- Other arithmetic operators ---")
print("7 - 2 =", 7 - 2)     # subtraction
print("7 * 2 =", 7 * 2)     # multiplication
print("7 / 2 =", 7 / 2)     # division -> always a float, e.g. 3.5
print("7 // 2 =", 7 // 2)   # floor division -> whole number only, e.g. 3
print("7 % 2 =", 7 % 2)     # modulus -> the REMAINDER after dividing, e.g. 1
print("7 ** 2 =", 7 ** 2)   # exponent -> 7 to the power of 2

# ---------- Comparison operators (asking a true/false question) ----------
# These don't calculate a new number - they compare two values and give
# back a bool (True or False). We will use these heavily in the next
# lesson (Conditions) to make decisions like pass/fail.
print("\n--- Comparison operators ---")
print("average >= 40 ?", average >= 40)   # greater than or equal to
print("average == 100 ?", average == 100)  # equal to (note: == not =)
print("average != 100 ?", average != 100)  # not equal to
print("math_marks > science_marks ?", math_marks > science_marks)

# ---------- Logical operators (combining true/false questions) ----------
# and / or / not let us combine multiple comparisons into one decision.
print("\n--- Logical operators ---")
passed_math = math_marks >= 40
passed_science = science_marks >= 40
print("Passed both Math and Science?", passed_math and passed_science)
print("Passed at least one of Math or Science?", passed_math or passed_science)
print("Did NOT pass Math?", not passed_math)

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Add a fourth subject's marks and include it in the total/average.
# 2. Use % to check if the total is an even or odd number
#    (hint: total % 2 == 0 means even).
# 3. Combine three comparisons with "and" to check if all three
#    subjects individually scored above 40.
# --------------------------------------------------------------------
