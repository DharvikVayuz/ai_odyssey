"""
Lesson 4.1 - The for Loop
===========================
What we already know: Riya has three subjects, stored in three separate
variables, and we calculate her total by adding them one by one:
    total = math_marks + science_marks + english_marks

The problem: that line works fine for 3 subjects. But what if Riya had
10 subjects? We would need 10 separate variables, and a total line with
9 plus signs. What if a school wants this for EVERY student, with a
different number of subjects each time? Typing every variable by name
does not scale.

New concept: a LIST holds many values in one single box, in order. A
for loop then lets us visit every value in that list, one at a time,
without writing a separate line for each one.
"""

student_name = "Riya"

# Instead of three separate variables, all three marks now live inside
# ONE list. The square brackets [ ] and commas are how Python writes a
# list. Order matters: this is still Math, then Science, then English.
marks = [80, 75, 90]

print(f"{student_name}'s marks list:", marks)

# A for loop visits each value in "marks", one at a time, and calls it
# "mark" for the duration of that one visit (you could name it anything).
print("\n--- Printing every mark ---")
for mark in marks:
    print(mark)

# Now let's recreate the total we calculated before - but with a loop
# this time, so it would work identically even if "marks" had 10 values.
total = 0            # start an "accumulator" at 0 - our running total
for mark in marks:
    total = total + mark   # add each mark onto the running total

average = total / len(marks)   # len() tells us how many items are in the list

print("\n--- Totals, calculated with a loop instead of by hand ---")
print("Total:", total)
print("Average:", average)

# --------------------------------------------------------------------
# Why this matters: notice that this code did not need to change AT ALL
# if we added a 4th, 5th, or 10th mark to the "marks" list - len(marks)
# and the loop automatically adjust. That's the whole point of loops:
# write the logic once, let it work for any amount of data.
# --------------------------------------------------------------------

# for + range(): sometimes we want to repeat something a fixed number
# of times, without looping over a list at all.
print("\n--- Using range() to repeat something 5 times ---")
for i in range(5):
    print("Repetition number:", i)   # range(5) counts 0, 1, 2, 3, 4

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Add a 4th mark to the "marks" list and re-run - check that total
#    and average update correctly with no other code changes.
# 2. Use a for loop to print each mark ALONGSIDE whether it's a pass
#    (>= 40) or fail, using what you learned about if/else.
# 3. Use range() to print the numbers 1 to 10 (hint: range(1, 11)).
# --------------------------------------------------------------------
