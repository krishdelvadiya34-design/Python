# Pattern Generator and Number Analyzer

## Overview

Pattern Generator and Number Analyzer is a beginner-friendly Python console application that allows users to generate patterns and analyze a range of numbers through a menu-driven interface. The project demonstrates the use of loops, nested loops, conditional statements, user input, and Python's `match-case` structure.

---

## Features

### 1. Generate a Pattern

Users can choose between two pattern types:

#### Star (*) Pattern

Example (Rows = 5):

```text
*
**
***
****
*****
****
***
**
*
```

#### Number Pattern

Example (Rows = 5):

```text
1
22
333
4444
55555
```

---

### 2. Analyze a Range of Numbers

The program:

- Accepts a starting number and ending number.
- Determines whether each number is Even or Odd.
- Supports both ascending and descending ranges.
- Calculates the sum of all numbers within the range.

Example:

```text
Enter the start of the range: 1
Enter the end of the range: 5

1 is Odd
2 is Even
3 is Odd
4 is Even
5 is Odd

Sum of all numbers from 1 to 5 is: 15
```

---

### 3. Exit the Program

Allows users to safely terminate the application.

Example:

```text
Exiting the program. Goodbye!
```

---

## Concepts Used

- Python Variables
- User Input (`input()`)
- Type Conversion (`int()`)
- While Loop
- For Loop
- Nested Loops
- Conditional Statements (`if`, `elif`, `else`)
- Match-Case Statement
- Range Function
- Arithmetic Operations

---

## Program Flow

1. Display the main menu.
2. User selects an option.
3. If Pattern Generator is selected:
   - Choose Star Pattern or Number Pattern.
   - Enter the number of rows.
   - Display the selected pattern.
4. If Number Analyzer is selected:
   - Enter the start and end of the range.
   - Display whether each number is Even or Odd.
   - Calculate and display the total sum.
5. If Exit is selected:
   - End the program.

---

## Requirements

- Python 3.10 or higher

---

## How to Run

1. Save the Python code in a file named `pattern_generator.py`.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python pattern_generator.py
```

---

## Learning Objectives

This project helps beginners learn:

- Menu-driven programming
- Pattern printing using nested loops
- Number analysis with conditional statements
- Loop control and iteration
- Match-case implementation in Python
- Interactive console application development
- Problem-solving using Python

---

## Sample Menu

```text
Select an Option:

1. Generate a Pattern
2. Analyze a Range of Number
3. Exit
```

---

## Author

**Krish Delvadiya**

AI, Machine Learning & Data Science Student

Currently learning Python programming and building beginner-friendly projects to strengthen programming and problem-solving skills.

---

⭐ If you found this project useful, consider giving it a star on GitHub!