# Lesson 6: Lists, Tuples, and Dictionaries

## What you'll learn

- Indexing (`marks[0]`) and slicing (`marks[0:2]`) on lists
- List built-ins: `len()`, `sum()`, `max()`, `min()`, `.append()`, `.index()`
- Tuples: fixed, unchangeable groups of values like `("Math", 80)`
- Dictionaries: looking up a value by name (`"key"`) instead of position
- A list of dictionaries - the shape almost every real dataset takes

## Why this matters

Real data is rarely just one flat list of numbers. A student has a name
*and* marks *and* attendance. A dataset has many students. Dictionaries and
lists-of-dictionaries are how Python (and, later, tools like Pandas) model
that kind of structured, real-world information.

## What we already know

Since [Lesson 4](../04_loops/README.md), `marks` has been a simple list. In
[Lesson 5](../05_functions/README.md) we kept a student's name and marks in
two *separate* lists (`student_names` and `all_marks`) that only made sense
if they stayed lined up by position - fragile, and easy to get wrong. This
lesson fixes that two ways: tuples bundle a couple of fixed values
together so they can't drift apart, and dictionaries let us describe one
whole student - name, marks, attendance, anything - as a single, clearly
labelled unit.

## New concept

- `01_lists.py`: goes deeper on lists we've been using since Lesson 4 -
  indexing, slicing, `.append()`, and finding the best-scoring subject with
  `max()` + `.index()`.
- `02_tuples.py`: pairs each subject with its mark as an unchangeable
  `("Math", 80)` tuple, replacing the two-separate-lists approach from
  Lesson 5.
- `03_dictionaries.py`: models one student as `{"name": ..., "marks": ...}`,
  then builds a list of student dictionaries and finds the class topper -
  this is the exact data shape the mini-project will use.

## Try it yourself

In `01_lists.py`: slice the last two marks; count marks `>= 80` with a
loop; find the lowest-scoring subject.

In `02_tuples.py`: add a 4th `(subject, mark)` tuple; print subjects scoring
below 80; try (and read the error from) changing a tuple's value directly.

In `03_dictionaries.py`: add `"attendance_percent"` to each student; add a
4th student; print only students averaging below 40.

## Challenge

Create variables for 5 students' `student_name`, `attendance_percent`, and
`is_eligible` (using a list of dictionaries), then print a formatted report
line for each student in a loop - e.g. `"Riya 82% attendance, Eligible"`.
(This uses f-strings, covered next in [Lesson 7](../07_strings/README.md) -
come back to this challenge after that lesson if you want the exact format.)
