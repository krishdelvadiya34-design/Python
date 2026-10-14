# PR-9 📊 Sales Data Analyzer

A menu-driven, command-line Python program to load a CSV dataset, explore it, clean it, run statistics, and create charts. 🐍

---

## ✨ Features

| # | Menu Option | What it does |
|---|-------------|--------------|
| 1 | 📂 Load Dataset | Reads a CSV file into a pandas DataFrame |
| 2 | 🔍 Explore Data | First/last 5 rows, column names, data types, basic info |
| 3 | 🛠️ DataFrame Operations | Search a column, sort, filter, aggregate |
| 4 | 🧹 Handle Missing Data | Show, fill (mean / custom value), or drop missing values |
| 5 | 📈 Descriptive Statistics | Std, variance, quantile, describe |
| 6 | 🎨 Data Visualization | Bar, line, scatter, pie, histogram, stack plot |
| 7 | 💾 Save Visualization | Saves the last chart as an image (e.g. `chart.png`) |
| 8 | 👋 Exit | Closes the program |

---

## 📦 Requirements

- 🐍 Python 3.8 or higher
- 🐼 pandas
- 📉 matplotlib
- 🌊 seaborn

Install everything with:

```bash
pip install pandas matplotlib seaborn
```

---

## ▶️ How to Run

```bash
python sales_data_analyzer.py
```

Then type the number of the option you want and press **Enter**.

---

## 🧭 Usage Guide

### 1️⃣ Load Dataset 📂
Enter the path of your CSV file, for example `sales.csv` or `C:/data/sales.csv`.
> ⚠️ Always load a dataset first, before using options 2 to 6.

### 2️⃣ Explore Data 🔍
1. First 5 rows
2. Last 5 rows
3. Column names
4. Data types
5. Basic info

### 3️⃣ DataFrame Operations 🛠️
1. **Search for a column** 🔎: shows the data of one column
2. **Sort values** ↕️: sorts the data by a column
3. **Filter** 🎯: less than a value, greater than a value, or between a range
4. **Aggregate** ➕: sum, mean, or count of a column

### 4️⃣ Handle Missing Data 🧹
1. Show rows with missing values
2. Fill missing values with the mean (numerical columns only)
3. Drop rows with missing values
4. Replace missing values with a specific number

### 5️⃣ Descriptive Statistics 📈
1. Standard deviation
2. Variance
3. Quantile (enter a value between 0 and 1, e.g. `0.25`)
4. Describe (summary of all numeric columns)

### 6️⃣ Data Visualization 🎨
| Chart | Input needed |
|-------|--------------|
| 📊 Bar Plot | x column, y column |
| 📉 Line Plot | x column, y column |
| ⚪ Scatter Plot | x column, y column |
| 🥧 Pie Chart | label column, value column |
| 📶 Histogram | one column |
| 🥞 Stack Plot | x column, several y columns separated by commas (e.g. `Quantity,Total_Sales`) |

### 7️⃣ Save Visualization 💾
Enter a file name with an extension, for example `linechart.png`.
> ⚠️ Draw a chart with option 6 first, then save it with option 7.
screenshot1
---

## 🛡️ Error Handling

The program catches common input mistakes and prints a friendly message instead of crashing:

- ❌ **ValueError**: the user typed text instead of a number, or used a non-numeric column for a numeric operation
- ❌ **IndexError**: the data or index requested is not available

---

## 📝 Example Session

### design :
![design](screenshot%20(1).png)

### Explore data :
![Explore_data](screenshot%20(2).png)

### data operations :
![data_operations](screenshot%20(3).png)

### handling missing value :
![missing_value](screenshot%20(4).png)

### statstical operations :
![statstical](screenshot%20(5).png)

### visualization :
![visualization](screenshot%20(6).png)

### save chart :
![save_chart](screenshot%20(7).png)

## 💡 Tips

- 🔤 Column names are **case-sensitive**: type them exactly as they appear in your CSV.
- 🔢 Use **numerical columns** for sum, mean, std, variance, quantile and most charts.
- 📁 Saved charts appear in the folder where you run the program.

---

## 📂 Project Structure

```text
📁 project-folder
 ├── 🐍 sales_data_analyzer.py
 ├── 📄 README.md
 └── 📊 your_dataset.csv
```

---

Made with ❤️ and Python 🐍