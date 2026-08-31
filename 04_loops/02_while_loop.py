"""
Lesson 4.2 - The while Loop
==============================
What we already know: a for loop visits every value in a list, or
repeats a fixed number of times with range().

The problem: sometimes we don't know in advance how many times we need
to repeat something. For example: "keep asking the teacher for marks
until they type 'done'." A for loop needs a known list or a known
count up front - it can't wait for a signal like that.

New concept: a while loop keeps repeating AS LONG AS a condition stays
True. It checks the condition before every repeat, and stops the
moment the condition becomes False.
"""

# ---------- while loop with a counter ----------
# Let's collect marks for a fixed number of subjects, but this time
# using a while loop driven by a counter we control ourselves.
marks = []              # start with an empty list - we'll fill it as we go
subject_count = 3
current_subject = 1     # counts 1, 2, 3, ...

print("Enter marks for 3 subjects:")
while current_subject <= subject_count:
    mark = int(input(f"  Subject {current_subject} marks: "))
    marks.append(mark)          # append() adds one value to the end of a list
    current_subject = current_subject + 1   # move the counter forward

print("\nAll marks collected:", marks)
print("Total:", sum(marks))     # sum() adds up every value in a list

# --------------------------------------------------------------------
# Why the counter update matters: if we forgot the line
# "current_subject = current_subject + 1", the condition
# "current_subject <= subject_count" would NEVER become False, and the
# loop would run forever (an "infinite loop"). Every while loop needs
# something inside it that eventually makes the condition False.
# --------------------------------------------------------------------

# ---------- while loop driven by a "stop word" ----------
# This is the situation a for loop genuinely cannot handle well: we
# don't know ahead of time how many subjects there will be. We keep
# going until the user themselves signals they're finished.
print("\nEnter marks one at a time. Type 'done' when finished.")
more_marks = []
mark_input = input("  Marks (or 'done'): ")

while mark_input != "done":
    more_marks.append(int(mark_input))
    mark_input = input("  Marks (or 'done'): ")

print("\nMarks entered:", more_marks)
if more_marks:   # an empty list is treated as False - a handy Python shortcut
    print("Average:", sum(more_marks) / len(more_marks))
else:
    print("No marks were entered.")

# --------------------------------------------------------------------
# TRY IT YOURSELF:
# 1. Change subject_count to 5 and re-run the first while loop.
# 2. In the "stop word" loop, use "stop" instead of "done" as the
#    signal to finish.
# 3. Add a check: if the user types a mark above 100, print
#    "That's not a valid mark!" and ask again (this needs an if
#    inside the while loop).
# --------------------------------------------------------------------
