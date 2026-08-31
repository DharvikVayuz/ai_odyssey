# Lesson 2: Input and Operators

## What you'll learn

- How to use `input()` to get information from the person running the
  program, instead of hardcoding it
- Why `input()` always gives you text (a `str`), and how to convert it to a
  number with `int()`/`float()`
- Arithmetic operators: `+ - * / // % **`
- Comparison operators: `> < >= <= == !=`
- Logical operators: `and`, `or`, `not`

## Why this matters

A program that only ever works with one hardcoded student ("Riya") isn't
very useful. `input()` is what turns a script into something a real user can
actually interact with. And once we can collect numbers, operators are how
we turn them into something meaningful - like a total and an average.

## What we already know

From [Lesson 1](../01_variables_and_data_types/README.md), we know how to
store Riya's name and marks in variables, and we know Python cares about
*types*. Here's the problem that creates: right now, every new student means
opening the code and retyping their marks by hand. That's fragile and
doesn't scale - which is exactly why we need `input()`.

## New concept

- `01_input.py`: replace hardcoded marks with `input()`, and explicitly
  convert what the user types (always a string) into a number with `int()`.
- `02_operators.py`: use arithmetic operators to calculate Riya's `total`
  and `average`, then use comparison and logical operators to start asking
  true/false questions about her marks (setting up the very next lesson:
  Conditions).

## Try it yourself

Open `01_input.py`, run it, and enter your own name and marks.

Open `02_operators.py` and:
1. Add a fourth subject's marks and include it in the total/average.
2. Use `%` to check if the total is an even or odd number
   (`total % 2 == 0` means even).
3. Combine three comparisons with `and` to check if all three subjects
   individually scored above 40.

## Challenge

1. Rewrite `01_input.py` so it also asks for and stores `attendance_percent`
   as a `float`.
2. Using only what you've learned so far (variables + operators, no
   conditions yet), print `True` or `False` for "Did Riya score above 80 in
   every subject?" using two comparisons joined with `and`.
3. What happens if you divide by `0` (e.g. `total / 0`)? Try it and read the
   error message carefully - can you tell what Python is complaining about?
