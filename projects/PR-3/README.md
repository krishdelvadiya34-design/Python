# Student Data Organizer

## Overview

Student Data Organizer is a Python-based console application that helps manage student records efficiently. The program allows users to add, view, update, and delete student information through a simple menu-driven interface.

This project demonstrates the use of Python data structures such as lists, dictionaries, and sets, along with loops, conditional statements, and user input handling.

---

## Features

### 1. Add Student

Users can add a new student by providing:

* Name
* Age
* Grade
* Date of Birth
* Subjects (comma-separated)

Each student is automatically assigned a unique ID.

### 2. Display All Students

View all stored student records, including:

* Student ID
* Name
* Age
* Grade
* Date of Birth
* Subjects

### 3. Delete Student

Remove a student record using the student's unique ID.

### 4. Update Student Information

Modify the details of an existing student by entering their ID.

### 5. Display Subjects Offered

Shows a combined list of all subjects chosen by students.

### 6. Exit Program

Safely closes the application.

---

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Sets
* Loops (`while`, `for`)
* Conditional Statements (`if-elif-else`)

---

## Data Structure Used

Each student is stored as a dictionary:

```python
{
    "Id": 101,
    "Name": "John",
    "Age": 18,
    "Grade": "A",
    "Date of Birth": "2008-05-12",
    "Subject": {"Math", "Science", "English"}
}
```

All student records are stored inside a list:

```python
students = []
```

---

## How to Run

1. Install Python 3 on your system.
2. Save the program as:

```bash
student_data_organizer.py
```

3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python student_data_organizer.py
```

---

## Sample Menu

```text
Welcome to Student Data Organizer!

Select an option:

1. Add student
2. Display all student
3. Delete student
4. Update student information
5. Display subjects offered
6. Exit
```

---

## Learning Objectives

This project helps beginners learn:

* Python fundamentals
* Menu-driven programming
* Lists, dictionaries, and sets
* Data management techniques
* User input handling
* CRUD operations (Create, Read, Update, Delete)

---

## Future Improvements

* Save data to a file (JSON/CSV)
* Search students by name
* Sort students by age or grade
* Add input validation
* Create a graphical user interface (GUI)
* Store data in a database

---

## Author

**Krish Delvadiya**

AI & ML | Data Science Student

Currently learning Python and building beginner-friendly projects to strengthen programming skills.
