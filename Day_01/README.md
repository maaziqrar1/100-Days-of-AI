# 🐍 Day 1: Python Fundamentals & Ubuntu Setup

### 📌 Journey Overview
This repository tracks my **100 Days of AI** journey. Today was focused on configuring my **HP ProBook 640 G2** environment and mastering core Python syntax.

---

### 🛠️ Technical Hurdles & Solutions

#### 1. Python Syntax: Reserved Keywords
* **Issue**: Encountered a `SyntaxError` when trying to assign a value to `break`.
* **Solution**: Learned that words like `break`, `class`, and `if` are reserved by Python and cannot be used as variable names.

#### 2. Ubuntu System Fixes
* **Issue**: `apt` updates were blocked by a missing `cdrom` Release file.
* **Solution**: Edited `/etc/apt/sources.list` to disable the CD-ROM entry, allowing for a clean Python installation.

#### 3. Display Configuration (X11)
* **Issue**: Encountered a `BadValue` error when trying to force 1080p resolution on a Dell monitor.
* **Solution**: Used `cvt` to calculate a safe $74.50\text{ MHz}$ pixel clock and added the new mode via `xrandr`.

---

### 💻 Concepts Practiced
* **f-strings**: Used `f"{variable}"` for fast, readable string formatting.
* **Binary Conversion**: Leveraged `format(num, 'b')` to represent integers in binary.
* **Dynamic Arrays**: Practiced using Python **Lists** to store heterogeneous data types.

---

### 📂 Day 1 File Index
* `variables.py`: Proper naming and keyword avoidance.
* `number_formating.py`: Binary and f-string exercises.
* `lists.py`: List manipulation and dynamic array properties.
* `sys_check.py`: Verification of the Ubuntu Python environment.

---
*Follow my progress as I dive into NumPy and Linear Algebra for AI next!*
