# Mini Project: Student Marks Manager

## What this is

The final program of the course - it doesn't introduce anything new. Every
piece of `main.py` is something you already built, lesson by lesson. This
is the payoff for following the story from Lesson 1 to Lesson 7.

## What you'll learn (by reusing what you already know)

- Nothing new syntactically - the goal here is seeing how *all seven
  lessons combine* into one real, working program
- How to organize a bigger program into small functions, each with one job
- How to structure an interactive program around a `main()` function that
  calls the smaller pieces in order

## Why this matters

Real programs are never just one lesson's worth of code - they're dozens of
small, well-named pieces (functions) working together. This project is
intentionally small enough to read top to bottom in a few minutes, while
still showing that structure.

## What we already know (and where each piece came from)

| Piece of `main.py` | Came from |
|---|---|
| `calculate_total()`, `calculate_average()` | [Lesson 5](../05_functions/README.md) |
| `get_grade()`, `check_pass_fail()` | [Lesson 3](../03_conditions/README.md) turned into functions |
| `collect_student()` using `input()` | [Lesson 2](../02_input_and_operators/README.md) |
| Student stored as `{"name": ..., "marks": [...]}` | [Lesson 6](../06_lists_and_collections/README.md) |
| Looping over `students`, and over `SUBJECTS` | [Lesson 4](../04_loops/README.md) |
| `build_report_line()` using f-strings | [Lesson 7](../07_strings/README.md) |

## How to run it

```bash
python 08_mini_project/main.py
```

It will ask how many students you want to enter, then ask for each
student's name and marks in Math, Science, and English. At the end it
prints a full class report and announces the topper.

## Try it yourself

1. Add a 4th subject to the `SUBJECTS` list at the top of the file - notice
   that `collect_student()`, `calculate_total()`, and every other function
   still work correctly without any other changes.
2. Change `PASSING_MARKS` from `40` to `35` and see how the Pass/Fail
   results change.
3. Add a function `count_passed_students(students)` that loops through the
   class and returns how many students overall got a `"Pass"` result.

## Challenge (take it further)

1. Add an `attendance_percent` question to `collect_student()`, and print
   `"Not Eligible for exam"` instead of a grade for any student below 75%
   attendance.
2. Sort the class report so it prints highest average first (hint: look up
   Python's `sorted()` function and its `key` parameter).
3. This mirrors the real end-of-course project from class: pick any small
   beginner dataset (for example from kaggle.com/datasets), load a few rows
   by hand into a list of dictionaries the same way we did here, and reuse
   `get_grade()`-style functions to label each row.
