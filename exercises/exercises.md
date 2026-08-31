# Exercises

These build on the same Student Marks story as the lessons. Work through
them roughly in order - each tier assumes you've finished the matching
lesson. Solutions are in [`solutions/`](solutions/) - try each exercise
yourself first before peeking.

---

## Beginner (after Lesson 1 - Variables and Data Types)

1. Change the student's name to your own name.
2. Change the marks to any three numbers you like.
3. Add a fourth subject (a new variable, e.g. `hindi_marks`) and print it.

*(Solution: `solutions/01_beginner_solution.py`)*

## Intermediate (after Lesson 4 - Loops)

1. Using a `marks` list, calculate the **highest** mark without using
   Python's built-in `max()` - loop through and keep track by hand.
2. Count how many subjects were **passed** (marks `>= 40`).
3. Calculate the **average** of the marks list using a loop (no `sum()`).

*(Solution: `solutions/02_intermediate_solution.py`)*

## Challenge (after Lesson 6 - Lists, Tuples, and Dictionaries)

1. Store **multiple students** as a list of dictionaries, each with a name
   and a marks list.
2. Calculate **each student's average**.
3. Determine **who scored the highest** average in the class.

*(Solution: `solutions/03_challenge_solution.py`)*

---

## Bonus: straight from class

These four are the exact exercises given out during the live "Python
Basics" session - a nice way to check everything stuck.

1. Create variables for 5 students' `student_name`, `attendance_percent`,
   and `is_eligible` (using a list or a dictionary), then print a formatted
   report line for each student using an f-string in a loop - e.g.
   `"Riya 82% attendance, Eligible"`.
2. Print a right-angled triangle pattern of stars using **nested loops**,
   where the number of rows equals the number of letters in your name
   (e.g. a 5-letter name prints 5 rows: 1 star, 2 stars, up to 5 stars).
3. Take marks for 5 subjects as input (one at a time), calculate the
   average, and print a grade: `"A"` if average > 90, `"B"` if average > 75,
   `"C"` if average > 50, else `"Fail"` - using a chained `if/elif/else`.
4. Write a function `grade_report(name, marks_list)` that takes a student's
   name and a list of marks, calculates the average *inside* the function,
   and returns a formatted string like
   `"Riya scored 78.4 average - Grade: B"`. Call it for 3 different
   students.

*(Solution: `solutions/04_class_bonus_solution.py`)*
