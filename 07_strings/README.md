# Lesson 7: Strings

## What you'll learn

- f-strings (`f"{name} scored {average:.2f}"`) - the clean way to mix text
  and variables
- Controlling how numbers are displayed (e.g. rounding to 2 decimal places)
- Common string methods: `.upper()`, `.lower()`, `.strip()`
- `+` to join strings, and why f-strings usually read better
- `len()` works on strings too, not just lists

## Why this matters

Every report, every printed result, every message a user sees is ultimately
a string. Learning to build one cleanly - instead of a messy pile of commas
inside `print()` - is what turns "debug output" into something that looks
like a real program.

## What we already know

We've used strings since [Lesson 1](../01_variables_and_data_types/README.md)
(`student_name = "Riya"`) and printed comma-separated pieces since day one -
`print("Name:", riya["name"])`. That gets clunky fast, especially once we
want a single, nicely formatted line like `"Riya scored 81.67 average"`.
f-strings are the fix.

## New concept

`01_strings.py` takes the `name`, `marks`, and `average` we've been working
with since Lesson 4, and builds the exact kind of report line the mini
project will need - combining an f-string, number formatting (`:.2f`), and
an `if/else` from Lesson 3 into one clean sentence.

## Try it yourself

1. Build an f-string report line that includes `name`, `average` (rounded
   to 1 decimal with `:.1f`), and a Pass/Fail result.
2. Use `.upper()` to print the student's name in capital letters as a
   "banner" before the report line.
3. Try `len()` on a full sentence, not just a name - what does it count?

## Challenge

Go back to the [Lesson 6 challenge](../06_lists_and_collections/README.md):
create 5 students (name, attendance, eligibility) and print a formatted
report line for each one in a loop, using an f-string - e.g.
`"Riya 82% attendance, Eligible"`.
