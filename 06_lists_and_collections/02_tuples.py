"""
Lesson 6.2 - Tuples
======================
What we already know: lists hold many values, and can be changed after
they're created (we used .append() and overwrote marks[0] in the last
lesson).

The problem: in the last lesson we kept "subjects" and "marks" as two
SEPARATE lists that only made sense together because they lined up by
position (subjects[0] belongs with marks[0]). That's easy to break -
if someone appends to one list and forgets the other, they'd go out of
sync.

New concept: a TUPLE bundles a few related values into one single,
UNCHANGEABLE group. Pairing "Math" with 80 as one tuple (not two
separate list entries) means they can never accidentally drift apart.
"""

# A tuple looks like a list, but with ( ) instead of [ ].
subject_marks = [
    ("Math", 80),
    ("Science", 75),
    ("English", 90),
]

# Looping over a list of tuples lets us "unpack" each tuple straight
# into two named variables in the for line itself.
print("--- Riya's report ---")
for subject, mark in subject_marks:
    print(f"{subject}: {mark}")

# We can still use everything we learned about lists - indexing,
# looping, len() - because subject_marks is a list; it just happens to
# contain tuples instead of plain numbers.
first_pair = subject_marks[0]
print("\nFirst subject/mark pair:", first_pair)
print("Just the subject name:", first_pair[0])
print("Just the mark:", first_pair[1])

# ---------- Why "unchangeable" (immutable) matters ----------
# Trying to change a value inside a tuple raises an error - on purpose.
# Uncomment the line below to see it happen:
# first_pair[1] = 100   # TypeError: 'tuple' object does not support item assignment

# If Riya's Math marks genuinely need correcting, we don't edit the
# tuple - we replace the whole pair with a new one.
subject_marks[0] = ("Math", 88)
print("\nAfter correcting Math marks:", subject_marks[0])

# ---------- Finding the best subject, the tuple way ----------
best_subject, best_mark = "", 0
for subject, mark in subject_marks:
    if mark > best_mark:
        best_subject = subject
        best_mark = mark

print(f"\nBest subject: {best_subject} with {best_mark} marks")

# --------------------------------------------------------------------
# When to use a tuple vs a list:
# - Use a LIST when you'll be adding/removing/changing items over time
#   (like collecting marks one at a time with input()).
# - Use a TUPLE when a few values belong together as one fixed unit,
#   like a (subject, mark) pair, or a (x, y) coordinate.
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Add a 4th (subject, mark) tuple to subject_marks for "Hindi".
# 2. Loop over subject_marks and print only the subjects where the
#    mark is below 80.
# 3. Try uncommenting the line that changes first_pair[1] and read the
#    error message Python gives you.
# --------------------------------------------------------------------
