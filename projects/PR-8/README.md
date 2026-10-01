# PR-8 🔢 NumPy Analyzer

🚀 A beginner-friendly, menu-driven NumPy project built with Python.

This project combines the NumPy concepts I have learned into one interactive program.
It allows users to create arrays and perform different operations such as indexing, slicing, mathematical operations, searching, sorting, filtering, combining, splitting, and statistical calculations.

✨ Features

#

Feature

Description

🟢 1

📦 Create Arrays

Create 1D and 2D NumPy arrays

🟢 2

🔍 Indexing

Access elements using indexes

🟢 3

✂️ Slicing

Slice 1D and 2D arrays

🟢 4

➕ Mathematics

Addition, subtraction, multiplication and division

🟢 5

🔗 Combine

Combine arrays using np.concatenate()

🟢 6

✂️ Split

Split arrays using np.split()

🟢 7

🔎 Search

Search values using np.where()

🟢 8

📊 Sort

Sort array values using np.sort()

🟢 9

🎯 Filter

Filter greater, lesser, even and odd values

🟢 10

📈 Statistics

Sum, mean, median, standard deviation and variance

🧠 NumPy Concepts Used

This project practices the following NumPy concepts:

np.array()
np.reshape()
np.concatenate()
np.split()
np.where()
np.sort()
np.sum()
np.mean()
np.median()
np.std()
np.var()

It also uses:

🔢 1D arrays

🔢 2D arrays

📍 Array indexing

✂️ Array slicing

🎯 Boolean masking

🔄 map()

📝 split()

🛡️ Exception handling

🔁 while loops

🔀 if-elif-else

🧩 Functions

🏗️ Basic OOP with a class

🖥️ Main Menu

When the program starts, it provides an interactive menu:

=====Welcome to the NumPy Analyzer=====

Choose an option:
        1. Create a Numpy Array
        2. Perform Mathematical Operations
        3. Combine or Split Arrays
        4. Search, Sort, or Filter Arrays
        5. Compute Aggregates and Statistics
        6. Exit

📦 1. Create a NumPy Array

The program currently supports:

🔹 1D Array

The user enters elements separated by spaces.

Example:

Enter elements for the array (sepreated by space): 10 20 30 40 50

Result:

[10 20 30 40 50]

🔹 2D Array

The user enters the number of rows, columns and elements.

Example:

Enter how many row you want to create: 2
Enter how many column you want to create: 3

Enter 6 elements to create Array: 10 20 30 40 50 60

Result:

[[10 20 30]
 [40 50 60]]

🚧 3D Array

3D array creation is currently not implemented.

Sorry ! ,This feature is not available

📍 2. Indexing & ✂️ Slicing

🔍 Indexing

For a 1D array:

array_data[i]

For a 2D array:

array_data[in_row, in_column]

✂️ Slicing

For a 1D array:

array_data[start:end]

For a 2D array:

array_data[row_start:row_end, column_start:column_end]

The program also handles invalid indexes using IndexError.

➕ 3. Mathematical Operations

The program supports:

➕ Addition

array_data + add_data

➖ Subtraction

array_data - sub_data

✖️ Multiplication

array_data * mul_data

➗ Division

array_data / div_data

The second array is created using the same dimensions as the original array.

🔗 4. Combine & ✂️ Split

🔗 Combine Arrays

The project uses:

np.concatenate((array_data, com_data))

This combines the arrays vertically for the current 2D-array workflow.

✂️ Split Array

The project uses:

np.split(array_data, parts)

If the array cannot be divided equally into the requested number of parts, the program handles the ValueError.

🔎 5. Search, Sort & Filter

🔎 Search

For searching values, the project uses:

np.where(array_data == value)

For a 2D array:

rows, columns = np.where(array_data == value)

This gives the positions where the value occurs.

📊 Sort

The project uses:

np.sort(array_data)

🎯 Filter

Greater than

array_data[array_data > value]

Less than

array_data[array_data < value]

Even numbers

array_data[array_data % 2 == 0]

Odd numbers

array_data[array_data % 2 != 0]

📈 6. Aggregate & Statistical Operations

The project calculates:

Operation

NumPy Function

➕ Sum

np.sum()

📊 Mean

np.mean()

📍 Median

np.median()

📉 Standard Deviation

np.std()

📈 Variance

np.var()

Example:

mean = np.mean(array_data)

🛡️ Error Handling

The project uses try-except blocks to handle some invalid operations.

Currently used exceptions include:

ValueError
IndexError

For example, an invalid array shape or an invalid split operation can raise ValueError.

Invalid array indexes are handled using IndexError.

🗂️ Project Structure

📁 NumPy Analyzer
│
├── 🐍 numpy_analyzer.py
│
└── 📄 README.md

⚙️ Requirements

You need:

🐍 Python

🔢 NumPy

Install NumPy using:

pip install numpy

▶️ How to Run

1️⃣ Clone or download the project

Place the Python file on your computer.

2️⃣ Install NumPy

pip install numpy

3️⃣ Run the program

python numpy_analyzer.py

🎯 Project Goal

The main goal of this project is to practice NumPy by combining multiple concepts into a single interactive command-line application.

Instead of practicing every NumPy concept separately, this project brings them together into one analyzer.

🚀 Future Improvements

Some features that can be added in future versions:

🔢 Add complete 3D array support

🛡️ Improve input validation

➗ Handle division by zero

🔄 Add more reshaping operations

🔁 Add transpose functionality

📈 Add maximum and minimum operations

🏆 Add argmax() and argmin()

🧩 Improve OOP structure

🎨 Improve the command-line interface

💾 Add options to save/load arrays

👨‍💻 Author

Krish Delvadiya

🎓 B.C.A. Student
🐍 Python Learner
🔢 NumPy Learner
📊 Exploring Data Science & AI/ML

⭐ Project Status

Status: 🟢 Active Learning Project

This project is being developed while learning Python and NumPy, so new features and improvements may be added over time.

💙 Thanks for checking out my project!

If you found this project useful, feel free to ⭐ the repository. 