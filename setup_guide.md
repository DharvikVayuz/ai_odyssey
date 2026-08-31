# Setup Guide

Follow this once before Lesson 1. It takes about 10 minutes.

## 1. Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/) and
   download the latest version for your operating system.
2. Run the installer.
   - **Windows only:** tick the box that says **"Add Python to PATH"**
     before clicking Install. This step is easy to miss and causes the
     most setup problems, so double-check it.
3. Verify it worked by opening a terminal and running:

   ```bash
   python --version
   ```

   You should see something like `Python 3.11.x`. If you see an error
   instead, Python either isn't installed or isn't on your PATH - reinstall
   and make sure to tick that checkbox.

   > On some Macs/Linux systems the command is `python3` instead of
   > `python`. If `python --version` doesn't work, try `python3 --version`.

## 2. Install an editor (recommended: VS Code)

1. Go to [code.visualstudio.com](https://code.visualstudio.com/), download
   it for your OS, and install it.
2. Open VS Code, click the Extensions icon on the left sidebar, search for
   **"Python"**, and install the official Microsoft extension.

## 3. Create a virtual environment

A virtual environment is a self-contained, private copy of Python just for
this project - it keeps this course's setup separate from anything else on
your computer.

From inside the `ai_odyssey` folder, run:

```bash
python -m venv .venv
```

This creates a `.venv` folder (you'll see it appear in the file explorer) -
that's your private Python environment.

## 4. Activate the virtual environment

You need to do this every time you start a new terminal session to work on
this course.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

When it's active, you'll see `(.venv)` appear at the start of your terminal
prompt.

## 5. Confirm everything works

```bash
python --version
```

Then try running the very first lesson:

```bash
python 01_variables_and_data_types/01_variables.py
```

If you see Riya's name and marks printed, you're fully set up.

## 6. Deactivate when you're done

```bash
deactivate
```

This returns your terminal to normal. You'll activate it again next time
you sit down to work through a lesson.

## About requirements.txt

This course intentionally uses **no external packages** - every lesson runs
on Python alone, so `requirements.txt` is empty (with a comment explaining
why). You still don't need to skip the virtual environment step - it's the
habit that matters, and it's exactly how you'd install packages later (with
`pip install -r requirements.txt`) if a future course needed any.
