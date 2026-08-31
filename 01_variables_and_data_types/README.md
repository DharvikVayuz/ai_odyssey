# Lesson 1: Variables and Data Types

## What you'll learn

- What a variable is, and how to create one
- How to store a name, a number, and other values in Python
- The four data types we use constantly: `str`, `int`, `float`, `bool`
- How to check a value's type with `type()`
- How to convert between types with `int()`, `float()`, and `str()`

## Why this matters

Every program - including every AI/ML program - starts the same way: put some
information somewhere the computer can find it again. A variable is that
"somewhere." Before a computer can calculate an average, sort a list, or
predict anything, the numbers have to live in variables first.

## What we already know

Nothing yet - this is lesson 1! We're starting our running example here:
**Riya's exam marks.** Every lesson from now on reuses this same student and
the same three subjects (Math, Science, English), and slowly builds a bigger
program around them.

## New concept

- **Variables** (`01_variables.py`): naming a box so Python can remember a
  value for us, and reusing that name later instead of retyping the value.
- **Data types** (`02_data_types.py`): every value has a *kind* - text
  (`str`), whole numbers (`int`), decimal numbers (`float`), or true/false
  (`bool`). Python needs to know the kind so it knows what operations make
  sense (you can add two `int`s, but not an `int` and random text).

## Try it yourself

Open `01_variables.py` and:
1. Change `student_name` to your own name.
2. Change the three marks to any numbers you like.
3. Run the file again (see the root [README](../README.md) for how to run a
   lesson) and check the new output.

Open `02_data_types.py` and:
1. Print the `type()` of `science_marks` and `english_marks`.
2. Create a new `bool` variable `is_topper` that checks `math_marks >= 90`.
3. Convert the string `"75"` into a number and add `10` to it.

## Challenge

1. Create a variable `attendance_percent` and give it a decimal value like
   `92.5`. What type is it?
2. Create a variable `class_section = "8B"`. Is it a `str` or an `int`? Why
   might that surprise someone who only looks at the value?
3. Without running the code, guess what `type("80" + "5")` would print.
   Then run it and see if you were right. (Hint: it's not `85`!)
