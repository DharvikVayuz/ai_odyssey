# Lesson 3: Conditions (if / elif / else)

## What you'll learn

- How `if` lets a program make a decision
- How `else` gives a fallback when the condition is `False`
- How `elif` (short for "else if") checks several conditions in order,
  and why the *order* you write them in matters
- How Python uses indentation (spaces) to know what's "inside" an `if`

## Why this matters

A calculator that only prints numbers isn't very interesting. The moment a
program can *react* differently depending on the data - "Pass" vs "Fail",
"A" vs "B" vs "C" - it starts to feel like a real tool. Every AI model you
will ever use eventually boils down to a decision like this too: spam or not
spam, cat or dog, pass or fail. `if/else` is the simplest possible version
of that same idea.

## What we already know

From [Lesson 2](../02_input_and_operators/README.md), we already calculated
`average` using arithmetic operators, and we already know that a comparison
like `average >= 40` produces a `True`/`False` answer. The problem: that
`True`/`False` value just sat there and didn't change what the program did.
Conditions fix that - they let the `True`/`False` answer actually control
what gets printed.

## New concept

`01_if_else.py` starts with a simple pass/fail check using the exact
`average` we already calculated, then upgrades it into a full grading
system (A/B/C/Fail) using `elif`. This mirrors the real classroom exercise
of grading students - and it's the same `if/elif/else` shape you'll use for
almost every decision a program ever makes.

## Try it yourself

1. Change `average` to a low number like `30` and re-run - does it correctly
   print "Fail"?
2. Add an `elif` for grade `"A+"` when `average > 95`, placed *above* the
   `"A"` check (think about why it has to go above, not below).
3. Add a separate `if` that checks a single subject (e.g. `math_marks`) and
   prints `"Needs improvement in Math"` if it's below 40.

## Challenge

1. Take marks for 5 subjects using `input()` (one at a time), calculate the
   average, and print a grade: `"A"` if average > 90, `"B"` if average > 75,
   `"C"` if average > 50, else `"Fail"` - using a chained `if/elif/else`
   (not five separate `if` statements).
2. Add a check: if the average is exactly `40` (the passing boundary),
   print a special message like `"Just made it!"` before the normal
   pass/fail message.
3. Using `and`/`or` inside a single `if` condition, print `"Needs a retest"`
   only when the average is below 40 **or** any individual subject is below
   30.
