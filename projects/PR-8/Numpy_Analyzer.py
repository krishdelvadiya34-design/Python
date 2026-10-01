import numpy as np

def array_x():

    global row,column,array_data
    
    print("\nSelect the type of Array to create :")
    print("\t1. 1D Array")
    print("\t2. 2D Array")
    print("\t3. 3D Array")
    
    arr_choice = int(input("\nEnter your choice :"))
    
    if arr_choice==1:
    
        element = input("\nEnter elements for the array (sepreted by space) :")
        row = 1
        column = len(element.split())
        array_data = np.array(list(map(int,element.split())))
        print(f"\n1D Array : {array_data}")
    
    elif arr_choice==2:
    
        try:
    
            row = int(input("\nEnter how many row you want to create : "))
            column = int(input("Enter how many column you want to create : "))
            data = input(f"\n\tEnter {row*column} elements to create Array (sepreted by space) : ")
    
            array_data = np.array(list(map(int,data.split()))).reshape(row,column)
    
        except ValueError:

            print(f"\nError : you have to give {row*column} elements")
    
        else:

            print(f"\n2D Array created successfully :\n{array_data}")
    
    elif arr_choice==3:

        print("Sorry ! ,This feature is not available")  
                
    else:
        print("\nInvaild choice!")

def array_op():

    while True:

        global row,column,array_data

        print("\nChoose an Operations:")
        print("\t1. Indexing")
        print("\t2. Slicing")
        print("\t3. Go Back")

        op_choice= int(input("\nEnter your choice :"))

        if op_choice==1:

            if array_data.ndim == 1:

                try:

                    i = int(input("\nEnter the index :"))

                    in_result1 = array_data[i]

                except IndexError:

                    print("\nPlease enter a valid Index !")

                else:

                    print(f"\nYour index Element : {in_result1}")

            else:

                try:

                    in_row = int(input("\nEnter the row index :"))
                    in_column = int(input("Enter the column index :"))

                    in_result2 = array_data[in_row,in_column]

                except IndexError:

                    print("\nPlease enter a valid Index !")

                else:

                    print(f"\nYour index Element : {in_result2}")

        elif op_choice==2:

            if array_data.ndim==1:

                try:

                    sl_index1 = int(input("\nEnter the starting index :"))

                    sl_index2 = int(input("Enter the ending index :"))

                    sl_result1 = array_data[sl_index1:sl_index2]

                except IndexError:
                
                    print("\nPlease enter a valid Index !")

                else:

                    print(f"\nSliced Array :\n{sl_result1}") 

            else:

                try:

                    sl_row1,sl_row2 = map(int,input("\nEnter the row range (start:end) :").split(":"))

                    sl_column1,sl_column2 = map(int,input("Enter the column range (start:end) :").split(":"))

                    sl_result2 = array_data[sl_row1:sl_row2,sl_column1:sl_column2]

                except IndexError:
                
                    print("\nPlease enter a valid Index !")
                
                else:

                    print(f"\nSliced Array :\n{sl_result2}") 

        elif op_choice==3:
            print("\nBack to Main Menu !")
            break

        else:
            print("\nInvaild Choice !")


def mathematics():

    global row,column,array_data

    print("\nChoose a Mathematical operation :")
    print("\t1. Addition")
    print("\t2. Substraction")
    print("\t3. Multiplication")
    print("\t4. Division")

    math_choice = int(input("\nEnter your choice :"))

    if math_choice==1:

        try:

            add_array = input(f"\nEnter the same-size array elements ({row*column} elements separated by space) : ")

            add_data = np.array(list(map(int,add_array.split()))).reshape(row,column)

            add_result = array_data + add_data

        except ValueError:
        
            print(f"\nError : Array size should be {row}x{column} ")

        else:

            print(f"\nOriginal Array :\n{array_data}")

            print(f"\nSecond Array :\n{add_data}")

            print(f"\nResult of Addition :\n{add_result}")

    elif math_choice==2:

        try:
            sub_array = input(f"\nEnter the same-size array elements ({row*column} elements separated by space) : ")

            sub_data = np.array(list(map(int,sub_array.split()))).reshape(row,column)

            sub_result = array_data - sub_data

        except ValueError:
                
            print(f"\nError : Array size should be {row}x{column} ")

        else:

            print(f"\nOriginal Array :\n{array_data}")

            print(f"\nSecond Array :\n{sub_data}")

            print(f"\nResult of Substraction :\n{sub_result}")

    elif math_choice==3:

        try:

            mul_array = input(f"\nEnter the same-size array elements ({row*column} elements separated by space) :")

            mul_data = np.array(list(map(int,mul_array.split()))).reshape(row,column)

            sub_result = array_data * mul_data

        except ValueError:
                
            print(f"\nError : Array size should be {row}x{column} ")
        
        else:
            print(f"\nOriginal Array :\n{array_data}")

            print(f"\nSecond Array :\n{mul_data}")

            print(f"\nResult of Multiplication :\n{sub_result}")

    elif math_choice==4:

        try:

            div_array = input(f"\nEnter the same-size array elements ({row*column} elements separated by space) : ")

            div_data = np.array(list(map(int,div_array.split()))).reshape(row,column)

            div_result = array_data / div_data

        except ValueError:
                        
            print(f"\nError : Array size should be {row}x{column} ")

        else:

            print(f"\nOriginal Array :\n{array_data}")

            print(f"\nSecond Array :\n{div_data}")

            print(f"\nResult of Division :\n{div_result}")

    else:
        print("\nInvaild choice!")


def combine_split():

    while True:

        global row,column,array_data

        print("\nChoose an option :")
        print("\t1. Combine Arrays")
        print("\t2. Split Array")
        print("\t3. Go Back")

        sub_choice = int(input("\nEnter your choice :"))

        if sub_choice==1:

            try:

                com_array = input(f"\nEnter the elements of another array to combine ({row*column} elements separated by space) : ")

                com_data = np.array(list(map(int,com_array.split()))).reshape(row,column)

                com_result = np.concatenate((array_data,com_data))

            except ValueError:
                    
                print(f"\nError : Array size should be {row}x{column} ")

            else:

                print(f"\nOriginal Array :\n{array_data}")

                print(f"\nSecond Array :\n{com_data}")

                print(f"\nCombined Array (Vertical Stack) :\n{com_result}")

        elif sub_choice==2:

            try:
            
                parts = int(input("\nEnter many parts do you want to split into? : "))

                sp_result = np.split(array_data,parts)

            except ValueError:

                print("\nArray can not divide properly")

            print(f"\nResult of Split :\n{sp_result}")

        elif sub_choice==3:
            print("\nBack to Main Menu !")
            break

        else:
            print("\nInvalid choice!")


def ssf():

    global row,column,array_data

    print("\nChoose an option:")
    print("\t1. Search a value")
    print("\t2. Sort the array")
    print("\t3. Filter values")

    ssf_choice=int(input("\nEnter your choice :"))

    if ssf_choice==1:

        if array_data.ndim==1:

            value = int(input("\nEnter the value that you want to search :"))

            result = np.where(array_data == value)

            if value in array_data:
                print(f"\nthe value {value} is at {result[0]}")

            else:
                print(f"\nthe value {value} is not in the array")

        else:

            value2 = int(input("\nEnter the value that you want to search :"))

            rows,columns = np.where(array_data==value2)

            if value2 in array_data:
                print(f"\nthe value {value2} is at {rows} row and {columns} column")

            else:
                print(f"\nthe value {value2} is not in the array")


    elif ssf_choice==2:

        print(f"\nOriginal Array:\n{array_data}")

        data = np.sort(array_data)

        print(f"\nSorted Array :\n{data}\n(Sorting Applied row-wise)")

    elif ssf_choice==3:

        print("\nChoose an Option:")
        print("\t1.Greater than (>)")
        print("\t2.Less than (<)")
        print("\t3.Even Numbers")
        print("\t4.Odd Numbers")

        f_choice=int(input("\nEnter your choice :"))

        if f_choice==1:

            g_value = int(input("\nEnter a value to get greater values :"))

            g_result = array_data[array_data > g_value]

            print(f"\nGreater Values : {g_result}")

        elif f_choice==2:

            l_value = int(input("\nEnter a value to get lesser values :"))

            l_result = array_data[array_data < l_value]

            print(f"\nLesser Values : {l_result}")

        elif f_choice==3:

            e_result = array_data[array_data%2==0]

            print(f"\nEven values : {e_result}")

        elif f_choice==4:
            
            o_result = array_data[array_data%2!=0]

            print(f"\nEven values : {o_result}")

        else:
            print("\nInvaild Choice !")

    else:
        print("\nInvaild Choice !")

def agg_st():

    global array_data

    print("\nChoose an aggregate/statistical operation:")
    print("\t1. Sum")
    print("\t2. Mean")
    print("\t3. Median")
    print("\t4. Standard Deviation")
    print("\t5. Variance")

    agg_st_choice = int(input("\nEnter your choice :"))

    if agg_st_choice==1:

        sum = np.sum(array_data)

        print(f"\nSum : {sum}")

    elif agg_st_choice==2:

        mean = np.mean(array_data)

        print(f"\nMean : {mean}")

    elif agg_st_choice==3:

        median = np.median(array_data)

        print(f"\nMedian : {median}")

    elif agg_st_choice==4:

        std = np.std(array_data)

        print(f"\nStandard Deviation : {std}")

    elif agg_st_choice==5:

        var = np.var(array_data)

        print(f"\nVariance : {var}")

    else:
        print("\nInvaild Choice !")



class DataAnalytics:

    def data(self):

        while True:

            print('''\n=====Welcome to the NumPy Analyzer=====

            Choose an option:
                    1. Create a Numpy Array
                    2. Perform Mathematical Operations
                    3. Combine or Split Arrays
                    4. Search, Sort, or Filter Arrays
                    5. Compute Aggregates and Statistics
                    6. Exit''')

            choice = int(input("\nEnter your choice :"))

            if choice==1:

                array_x()

                if array_data is None:
                    print("\nPlease create an array first !")

                else:
                    array_op()

            elif choice==2:

                if array_data is None:
                    print("\nPlease create an array first !")
                
                else:
                    mathematics()

            elif choice==3:

                if array_data is None:
                    print("\nPlease create an array first !")
                
                else:
                    combine_split()

            elif choice==4:

                if array_data is None:
                    print("\nPlease create an array first !")
                
                else:
                    ssf()

            elif choice==5:

                if array_data is None:
                    print("\nPlease create an array first !")
                
                else:
                    agg_st()

            elif choice==6:
                print("\nThank you for using NumPy Analyzer !")
                break

            else:
                print("\nInvaild choice !")


f_data = DataAnalytics()
f_data.data()