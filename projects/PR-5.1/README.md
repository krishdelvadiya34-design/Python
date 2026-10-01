# 👨‍💼 Employee Management System (Python OOP)

A simple **Employee Management System** built using **Python Object-Oriented Programming (OOP)** concepts. This project demonstrates **Inheritance, Method Overriding, Constructors, Lists of Objects, and Menu-Driven Programming**.

---

## 📌 Features

- ➕ Add Employee
- 👔 Add Manager
- 💻 Add Developer
- 📋 Display Employee Details
- 📋 Display Manager Details
- 📋 Display Developer Details
- 🧬 Uses Inheritance
- 🔁 Method Overriding
- 🧱 Object-Oriented Design
- 📂 Stores multiple objects using Python Lists

---

## 🛠️ Concepts Used

- Classes & Objects
- Constructors (`__init__`)
- Inheritance
- `super()`
- Method Overriding
- Lists
- Loops
- Conditional Statements
- User Input
- Menu-Driven Program

---

## 📁 Project Structure

```
Employee-Management-System/
│
├── employee_management.py
└── README.md
```

---

## 🏗️ Class Diagram

```
                Employee
               /        \
              /          \
         Manager      Developer
```

### Employee

**Attributes**
- Name
- Age
- Salary

**Methods**
- `showinfo()`

---

### Manager

Inherits from **Employee**

**Additional Attribute**
- Department

Overrides:
- `showinfo()`

---

### Developer

Inherits from **Employee**

**Additional Attribute**
- Programming Language

Overrides:
- `showinfo()`

---

## ▶️ Menu

```
Choose an option:

1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit
```

---

## 💻 Example Output

```
Choose an option:

1. Create Employee
2. Create Manager
3. Create Developer
4. Show Details
5. Exit

Choose an option : 1

Enter Employee name : Krish
Enter Employee's age : 18
Enter Employee's salary : 25000

Employee is added successfully!
```

Display Details

```
Enter 1/2/3 to show Emp/Mana/Dev => 1

Name : Krish
Age : 18
Salary : 25000
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/Employee-Management-System.git
```

### Go to Project Folder

```bash
cd Employee-Management-System
```

### Run

```bash
python employee_management.py
```

---

## 📚 Learning Objectives

This project helps beginners understand:

- Creating classes
- Creating objects
- Inheritance
- Method overriding
- Using `super()`
- Menu-driven programs
- Managing multiple objects
- Python OOP best practices

---

## 🔮 Future Improvements

- ✅ Delete Employee
- ✅ Update Employee Details
- ✅ Search by Name or ID
- ✅ Employee ID Generation
- ✅ File Handling (Save Data)
- ✅ JSON Database
- ✅ SQLite Database
- ✅ Exception Handling
- ✅ Login System
- ✅ GUI using Tkinter
- ✅ Web Version using Flask/Django

---

## 🧑‍💻 Author

**Krish Delvadiya**

🌱 Learning:
- Python
- Object-Oriented Programming
- Data Structures
- AI & Machine Learning
- Data Science

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.

Happy Coding! 🚀