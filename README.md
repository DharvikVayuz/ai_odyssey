# AI Odyssey - Python Basics

A beginner-friendly, hands-on Python course - built around one running
example that grows a little bigger in every lesson, until it becomes a
real, working program.

## What this repository is

This is the companion code repository for the **"Python Basics and
Concepts"** class. It turns the concepts covered in class - variables,
loops, conditions, and functions - into a full, structured curriculum you
can teach from live, and that you (or your students) can come back to
later as a reference.

## Who it is for

Kids and absolute beginners who are writing Python for the first time. No
prior programming experience is assumed. Every file is meant to be read
top to bottom, run, and experimented with.

## How the lessons are structured

Every lesson builds on **one story**: a student named Riya and her exam
marks. Instead of a new, unrelated example every time, each lesson takes
the *exact same program* from the previous lesson and improves it using
one new concept - so it always feels like "we already know this, we're
just making it better," never "here's a completely new example."

```text
01_variables_and_data_types   ->  Store Riya's name and marks
02_input_and_operators        ->  Let the USER type the marks in; calculate total/average
03_conditions                 ->  Decide Pass/Fail and a letter grade
04_loops                      ->  Handle any number of subjects, not just 3
05_functions                  ->  Package the calculations so they can be reused
06_lists_and_collections      ->  Model a whole student, and many students, properly
07_strings                    ->  Turn the results into a clean, readable report
08_mini_project                ->  Combine everything into "Student Marks Manager"
```

Each new concept exists to solve a real problem the previous lesson ran
into - for example, doing `math_marks + science_marks + english_marks` by
hand is fine for 3 subjects, but becomes painful at 10. That's exactly why
Lesson 4 introduces lists and loops. Every lesson's README explains that
"why" explicitly.

## How to install Python

See [`setup_guide.md`](setup_guide.md) for full, step-by-step instructions
(installing Python, installing an editor, and verifying it all works).

## How to create and activate the virtual environment

```bash
# Create it once, from inside this folder:
python -m venv .venv

# Activate it (do this every time you start a new terminal session):
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# When you're done for the day:
deactivate
```

This course doesn't need any external packages (see
[`requirements.txt`](requirements.txt) for why), but setting up the virtual
environment is still good practice - it's exactly what you'd do before
`pip install`-ing anything in a future project.

## How to run a lesson

Every `.py` file can be run directly. From the root of this repository:

```bash
python 01_variables_and_data_types/01_variables.py
python 01_variables_and_data_types/02_data_types.py
python 02_input_and_operators/01_input.py
python 02_input_and_operators/02_operators.py
python 03_conditions/01_if_else.py
python 04_loops/01_for_loop.py
python 04_loops/02_while_loop.py
python 05_functions/01_basic_functions.py
python 05_functions/02_parameters.py
python 06_lists_and_collections/01_lists.py
python 06_lists_and_collections/02_tuples.py
python 06_lists_and_collections/03_dictionaries.py
python 07_strings/01_strings.py
python 08_mini_project/main.py
```

Some files use `input()` and will pause to ask you a question in the
terminal - just type your answer and press Enter.

## The learning progression

```text
Variables and Data Types
        |
Input and Operators
        |
Conditions (if / elif / else)
        |
Loops (for / while)
        |
Functions
        |
Lists, Tuples, and Dictionaries
        |
Strings (f-strings and formatting)
        |
Mini Project: Student Marks Manager
```

## The final mini-project

**Student Marks Manager** ([`08_mini_project/main.py`](08_mini_project/main.py))
lets you enter any number of students, collects their marks for three
subjects, and prints a full class report - total, average, grade, and
pass/fail for each student - plus the class topper. Every function inside
it is something you built, piece by piece, in an earlier lesson. See the
[mini project README](08_mini_project/README.md) for the full breakdown of
which lesson each part came from.

## Exercises

[`exercises/exercises.md`](exercises/exercises.md) has beginner,
intermediate, and challenge exercises following the same story, plus a
bonus set taken directly from the live class. Try each one yourself before
checking [`exercises/solutions/`](exercises/solutions/).

## A note on scope

This repository focuses entirely on Python basics: variables, data types,
input, operators, conditions, loops, functions, collections, and strings.
The class this course is based on also covers *why Python is used for
AI/ML* and introduces libraries like NumPy, Pandas, Matplotlib,
Scikit-learn, and TensorFlow/PyTorch - those are intentionally **not**
included here, since they need external packages and solid basics first.
This repository is that solid foundation.
