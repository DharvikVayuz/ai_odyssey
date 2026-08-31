# Lesson 4: Loops (for and while)

## What you'll learn

- What a **list** is (`marks = [80, 75, 90]`) and why it beats one variable
  per value
- How a `for` loop visits every item in a list automatically
- How `for i in range(n)` repeats something a fixed number of times
- How a `while` loop repeats *as long as* a condition stays `True`
- Why every `while` loop needs something inside it that can eventually make
  the condition `False` (or it never stops)

## Why this matters

Training an AI model means repeating the same calculation across thousands
or millions of data points - nobody writes that by hand, one line per data
point. Loops (or their faster cousins, like NumPy's vectorized operations)
are what make that possible. Even outside AI, "do this for every student /
every row / every photo" is one of the most common patterns in programming.

## What we already know

We calculated Riya's `total` in [Lesson 2](../02_input_and_operators/README.md)
with `math_marks + science_marks + english_marks`. That's fine for 3
subjects, but imagine 10 subjects - that line would need 10 variable names
and 9 plus signs, and every new student would mean rewriting it. This lesson
solves exactly that problem: put the marks in **one list**, then loop over
it. The total logic no longer cares how many marks there are.

## New concept

- `01_for_loop.py`: turns Riya's three separate mark variables into a
  single `marks` list, then recalculates the same `total`/`average` from
  Lesson 2 - but with a `for` loop this time, so it would work unchanged
  even with 10 or 100 marks.
- `02_while_loop.py`: uses a `while` loop for two situations a `for` loop
  can't handle as naturally - repeating a known number of times using a
  manually-controlled counter, and repeating an *unknown* number of times
  until the user types a stop signal.

## Try it yourself

In `01_for_loop.py`:
1. Add a 4th mark to the `marks` list and re-run - `total` and `average`
   should update with no other code changes.
2. Print each mark alongside whether it's a pass (`>= 40`) or fail, using
   an `if/else` inside the loop.
3. Use `range()` to print the numbers 1 to 10.

In `02_while_loop.py`:
1. Change `subject_count` to 5 and re-run.
2. Use `"stop"` instead of `"done"` as the finish signal.
3. Add a check inside the loop: if a mark is above 100, print
   `"That's not a valid mark!"`.

## Challenge

1. Print a right-angled triangle pattern of stars using **nested loops**
   (a loop inside a loop), where the number of rows equals the number of
   letters in your name. For example, a 5-letter name prints 5 rows: 1
   star, then 2 stars, then 3, up to 5.
2. Using the `marks` list, write a loop that counts how many subjects
   scored `>= 40` (a "subjects passed" counter).
3. Using the `marks` list, write a loop that finds the *highest* mark
   without using Python's built-in `max()` - keep a variable
   `highest_so_far` and update it inside the loop whenever you see a bigger
   mark.
