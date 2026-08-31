# Lesson 5: Functions

## What you'll learn

- What a function is, and why `def` creates one
- Parameters vs. arguments
- `return` (sending a value back out) vs. just `print()`-ing inside a
  function
- Default parameter values, and when to override them
- Calling the same function repeatedly for different data

## Why this matters

Every library function you'll ever use - `load_data()`, `model.fit()`,
`model.predict()` - is just someone else's well-written function. Learning
to write your own is the first step to understanding what those calls are
actually doing underneath.

## What we already know

In [Lesson 4](../04_loops/README.md) we wrote a 4-line loop to calculate an
average, and in [Lesson 3](../03_conditions/README.md) we wrote `if/elif`
logic for pass/fail and grades. The problem: every time we want an average
or a grade for a *new* student, we'd have to copy-paste those same lines
again. If we ever found a bug in the calculation, we'd have to fix it in
every copy. Functions solve this - write the logic once, reuse it by name.

## New concept

- `01_basic_functions.py`: wraps the averaging loop from Lesson 4 into
  `calculate_average(marks)`, then reuses it for three different students
  with zero copy-pasting.
- `02_parameters.py`: turns the pass/fail and grading logic from Lesson 3
  into `check_pass_fail(average, passing_marks=40)` (showing a default
  parameter) and `get_grade(average)`, then runs a small class report by
  calling all three functions together.

## Try it yourself

In `01_basic_functions.py`:
1. Call `calculate_average()` with a brand-new list of your own marks.
2. Write `calculate_total(marks)` that returns the sum of a marks list.
3. Print a message like `"Riya's total is 245 and her average is 81.67"`
   using both functions together.

In `02_parameters.py`:
1. Call `check_pass_fail()` for a student with a low average and confirm it
   returns `"Fail"`.
2. Add a new student to both `student_names` and `all_marks` and re-run.
3. Write `count_passed(marks)` that returns how many subjects scored `>= 40`.

## Challenge

Write a function `grade_report(name, marks_list)` that takes a student's
name and a list of marks, calculates the average *inside* the function, and
returns a formatted string like `"Riya scored 78.4 average - Grade: B"`.
Call it for 3 different students and print each result.
