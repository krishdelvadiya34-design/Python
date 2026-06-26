data_li = []

# creating array
def input_data():
    global data_li
    data_li = [int(i) for i in input("Enter elements separated by space: ").split()]
    print("\nData entered successfully.")


# Data summary using built-in functions
def data_summary(data_li):
    print("\nData Summary:")
    print("- Total of Elements:", len(data_li))
    print("- Minimum Value:", min(data_li))
    print("- Maximum Value:", max(data_li))
    print("- Sum of Values:", sum(data_li))
    print("- Average Value:", sum(data_li) / len(data_li))

# factorial
def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print(factorial)

# threshold
def threshold_data(data_li, threshold):
    condition = lambda x: x >= threshold
    return [x for x in data_li if condition(x)]

# sorting:ascending
def sorting():
    global data_li
    sorted_list = sorted(data_li)
    print(sorted_list)

# sorting:descending
def reverse():
    global data_li
    sorted_list = sorted(data_li, reverse=True)
    print(sorted_list)

# return multiple value
def multiple_value(data_li):
    min_value = min(data_li)
    max_value = max(data_li)
    sum_value = sum(data_li)
    average_value = sum(data_li) / len(data_li)

    return min_value, max_value, sum_value, average_value


print("\nWelcome to the Data Analyzer and Transformer Program!")

while True:
    print('''\nMain Menu:
    1. Input Data
    2. Display Data Summary (Built-in Functions)
    3. Calculate Factorial (Recursion)
    4. Filter Data by Threshold (Lambda Function)
    5. Sort Data
    6. Display Dataset Statistics (Return Multiple Values)
    7. Exit Program''')

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        data_summary(data_li)

    elif choice == 3:
        n = int(input("\nEnter a number to calculate factorial: "))
        fact(n)

    elif choice == 4:
        threshold = int(input("\nEnter a number for threshold: "))
        result = threshold_data(data_li, threshold)
        print(result)

    elif choice == 5:
        print("1. Ascending")
        print("2. Descending")

        num = int(input("\nEnter your choice: "))

        if num == 1:
            sorting()
        elif num == 2:
            reverse()

    elif choice == 6:
        min_value, max_value, sum_value, average_value = multiple_value(data_li)

        print(f'''\nDataset Statistics:
- Maximum Value: {max_value}
- Minimum Value: {min_value}
- Sum of all Values: {sum_value}
- Average Value: {average_value}
''')

    elif choice == 7:
        print("\nThank you!")
        break

    else:
        print("\nInvalid choice!")