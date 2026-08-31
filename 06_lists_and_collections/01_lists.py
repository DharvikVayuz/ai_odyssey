"""
Lesson 6.1 - Lists in Depth
==============================
What we already know: a list holds many values in order, and a for loop
can visit each one. We've used marks = [80, 75, 90] since Lesson 4.

New concept: lists can do a lot more than just get looped over - we can
look up one value by its position (indexing), grab a sub-section
(slicing), add to them, and use Python's built-in helper functions on
them. Let's use these to answer real questions about Riya's marks.
"""

marks = [80, 75, 90]
subjects = ["Math", "Science", "English"]

# ---------- Indexing: getting ONE value by its position ----------
# Python counts positions starting at 0, not 1.
print("First mark (index 0):", marks[0])
print("Second mark (index 1):", marks[1])
print("Last mark (index -1):", marks[-1])   # negative index counts from the end

# ---------- Slicing: getting a RANGE of values ----------
print("\nFirst two marks:", marks[0:2])   # up to (not including) index 2
print("All but the first mark:", marks[1:])

# ---------- Built-in functions that work on any list of numbers ----------
print("\n--- Quick stats on Riya's marks ---")
print("Number of subjects (len):", len(marks))
print("Total (sum):", sum(marks))
print("Highest mark (max):", max(marks))
print("Lowest mark (min):", min(marks))
print("Average:", sum(marks) / len(marks))

# ---------- Changing a list ----------
print("\n--- Changing the list ---")
marks.append(85)          # append() adds one value to the end
subjects.append("Hindi")
print("After adding a Hindi mark:", marks)
print("Subjects now:", subjects)

marks[0] = 88              # we can overwrite a value at a specific index
print("After correcting Math marks:", marks)

# ---------- Using max()/min() together with index() ----------
# index() finds the position of a value, which lets us find out WHICH
# subject had the highest mark - not just what the highest mark was.
highest_mark = max(marks)
position_of_highest = marks.index(highest_mark)
best_subject = subjects[position_of_highest]
print(f"\nBest subject: {best_subject} with {highest_mark} marks")

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Print the marks list sliced to show only the last two marks.
# 2. Use a loop (from Lesson 4) to count how many marks are >= 80.
# 3. Find and print the LOWEST-scoring subject, the same way we found
#    the best one above.
# --------------------------------------------------------------------
