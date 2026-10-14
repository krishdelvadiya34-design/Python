import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

figure = None

def load_data():

    global dataframe

    try:

        file_name = input("\nEnter the path of dataset (CSV file) :")

        dataframe = pd.read_csv(file_name)

        print("\nDataset loaded successfully!") 

    except ValueError:

        print("\nInvalid file! Please enter a valid CSV file path.")


def explore_data():

    global dataframe

    print("\n== Explore Data ==")
    print("1. Display the first 5 rows")
    print("2. Display the last 5 rows")
    print("3. Display column names")
    print("4. Display data types")
    print("5. Display basic info")

    try:

        ed_choice = int(input("\nEnter your choice :"))

        if ed_choice==1:

            print("\nData of first five rows :") 
            data01 = dataframe.head()
            print()               
            print(data01)

        elif ed_choice==2:

            print("\nData of last five rows :") 
            data02 = dataframe.tail()
            print()
            print(data02)

        elif ed_choice==3:

            data03 = dataframe.columns.to_list()
            print("\n===Columns name===")

            for columns in data03:
                print(columns)

        elif ed_choice==4:

            data04 = dataframe.dtypes
            print(f"\nData Type :\n{data04}")

        elif ed_choice==5:

            print(f"\nData Info :\n")
            dataframe.info()

        else:

            print("\nInvaild choice!")

    except ValueError:

        print("\nInvalid input! Please enter a number only.")

    except IndexError:

        print("\nNo data available to display. Please check the dataset.")


def data_operations():

    print("\n== DataFrame Operations ==")
    print("1. Search for a column")
    print("2. Sort values")
    print("3. Filter for specific column")
    print("4. Aggregating functions")
    
    try:

        do_choice = int(input("\nEnter your choice :"))
        
        if do_choice==1:
        
            c_name = input("\nEnter a specific column name :")
            data05 = dataframe[c_name]
            print(f"\n{c_name}'s data :\n{data05}")
        
        elif do_choice==2:
        
            s_column = input("\nEnter column name to sort value :")
            data06 = dataframe.sort_values([s_column])
            print("\nResult of sorting :\n",data06)
        
        elif do_choice==3:
        
            print("\n==Filter Menu==")
            print("1. Less value")
            print("2. Greater value")
            print("3. Between a range (Ex :Total sales from 10000 to 20000)")
        
            f_column = input("\nEnter a column name that you want to filter :")
        
            f_choice = int(input("\nEnter your choice :"))
        
            if f_choice==1:
        
                l_value = int(input("\nEnter a value to print less values :"))
                data07 = dataframe[dataframe[f_column] < l_value]
                print(f"\nLess values from {l_value} :\n{data07}")
        
            elif f_choice==2:
        
                g_value = int(input("\nEnter a value to print greater values :"))
                data08 = dataframe[dataframe[f_column] > g_value]
                print(f"\nGreater values from {g_value} :\n{data08}")
                            
        
            elif f_choice==3:
        
                first_range = int(input("\nEnter minimum value :"))
                second_range = int(input("Enter maximum value :"))
        
                data09 = dataframe[(dataframe[f_column] > first_range) & (dataframe[f_column] < second_range)]
                print("\nResult :\n",data09)
        
            else:
        
                print("\nInvalid choice!")

        elif do_choice==4:

            print("\n==Aggregating Operations==")
            print("1. Sum")
            print("2. Mean")
            print("3. count")

            a_column = input("\nEnter a column name that you want to aggregate :")
            a_choice = int(input("\nEnter your choice :"))

            if a_choice==1:

                data10 = dataframe[a_column].sum()
                print("\nSum :",data10)

            elif a_choice==2:

                data11 = dataframe[a_column].mean()
                print("\nMean :",data11)

            elif a_choice==3:

                data12 = dataframe[a_column].count()
                print("\nCount :",data12)

            else:

                print("\nInvalid choice!")
               
        else:

            print("\nInvalild choice!")

    except ValueError:

        print("\nInvalid input! Please enter a valid number (or a numeric column for this operation).")

    except IndexError:

        print("\nIndex out of range! Please check the column or the data you entered.")


def clean_data():

    global dataframe

    print("\n== Handle Missing Data ==")
    print("1. Display rows with missing values")
    print("2. Fill missing values with mean")
    print("3. Drop rows with missing values")
    print("4. Replace missing values with a specific value")

    try:

        m_choice = int(input("\nEnter your choice :"))

        if m_choice==1:

            data08 = dataframe.isnull().sum()

            if data08.sum() == 0:
                print("\nNo missing value found in dataset")

            else:
                print(f"\nMissing values in each column :\n{data08}")
                data09 = dataframe[dataframe.isnull().any(axis=1)]
                print(f"\nRows with missing values :\n{data09}")

        elif m_choice==2:

            col_name = input("\nEnter column name to fill value with mean (enter only numerical columns) :")

            mean_col = dataframe[col_name].mean()

            dataframe[col_name] = dataframe[col_name].fillna(mean_col)

            print(f"\nMissing values of {col_name} filled with mean ({mean_col}) successfully!")

        elif m_choice==3:

            before_rows = len(dataframe)

            dataframe = dataframe.dropna()

            print(f"\n{before_rows - len(dataframe)} rows dropped successfully!")

        elif m_choice==4:

            col_name = input("\nEnter column name to replace missing values :")
            new_value = input("Enter a value to replace with :")

            new_value = float(new_value)

            dataframe[col_name] = dataframe[col_name].fillna(new_value)

            print(f"\nMissing values of {col_name} replaced with {new_value} successfully!")

        else:

            print("\nInvalid choice!")

    except ValueError:

        print("\nInvalid input! Please enter a valid number for the choice or the replacement value.")

    except IndexError:

        print("\nIndex out of range! Unable to handle missing data for the given input.")


def statstical_analysis():

    print("\n==Statistical Operations==")
    print("1. Standard Deviation (std)")
    print("2. Variance (var)")
    print("3. Quantile")
    print("4. Describe")

    try:

        s_choice = int(input("\nEnter your choice :"))

        if s_choice==1:

            std_column = input("\nEnter a column to find Standard Deviation :")
            data13 = dataframe[std_column].std()
            print(f"\nStandard Deviation :{data13}")

        elif s_choice==2:

            var_column = input("\nEnter a column to find Variance :")
            data14 = dataframe[var_column].var()
            print(f"\nVariance :\n{data14}")

        elif s_choice==3:

            qua_column = input("\nEnter a column to find Quantile :")
            qua_value = float(input("Enter a quantile between 0 and 1 (Ex: 0.25) :"))
            data15 = dataframe[qua_column].quantile(qua_value)
            print(f"\nQuantile of {qua_value} :\n{data15}")

        elif s_choice==4:

            data16 = dataframe.describe()
            print(f"\n==Result==\n{data16}")

        else:

            print("Invalid choice!")

    except ValueError:

        print("\nInvalid input! Please enter a number (quantile must be between 0 and 1) and use a numerical column.")

    except IndexError:

        print("\nIndex out of range! No data available for the statistical operation.")


def visualize_data():

    global figure

    print("\n== Data Visualization ==")
    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Histogram")
    print("6. Stack Plot")

    figure = plt.figure()

    try:

        v_choice = int(input("Enter your choice :"))

        if v_choice==1:

            x = input("\nEnter a column name for horizontal line (x) :")
            y = input("\nEnter a column name for vertical line (y) :")
            data17 = snb.barplot(data=dataframe,x=f"{x}",y=f"{y}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("==Bar chart==")
            figure = plt.gcf()
            plt.show()

        elif v_choice==2:

            x = input("\nEnter a column name for horizontal line (x) :")
            y = input("\nEnter a column name for vertical line (y) :")
            data17 = snb.lineplot(data=dataframe,x=f"{x}",y=f"{y}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("==Line chart==")
            figure = plt.gcf()
            plt.show()

        elif v_choice==3:

            x = input("\nEnter a column name for horizontal line (x) :")
            y = input("\nEnter a column name for vertical line (y) :")
            data17 = snb.scatterplot(data=dataframe,x=f"{x}",y=f"{y}")
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("==Scatter chart==")
            figure = plt.gcf()
            plt.show()

        elif v_choice==4:

            p_label = input("\nEnter a column name for labels (Ex: Category) :")
            p_value = input("\nEnter a column name for values (Ex: Total_Sales) :")

            data17 = dataframe.groupby(p_label)[p_value].sum()

            plt.pie(data17, labels=data17.index, autopct="%1.1f%%", startangle=90)
            plt.title("==Pie chart==")
            plt.axis("equal")

            figure = plt.gcf()
            plt.show()

        elif v_choice==5:

            x = input("\nEnter a column name for histogram (x) :")
            data18 = snb.histplot(data=dataframe,x=f"{x}",kde=True)
            plt.xlabel(x)
            plt.ylabel("Count")
            plt.title("==Hist chart==")
            figure = plt.gcf()
            plt.show()

        elif v_choice==6:
            x = input("\nEnter a column name for horizontal line (x) :")
            y = input("\nEnter column names to stack, separated by comma (Ex: Quantity,Total_Sales) :")

            y_list = [col.strip() for col in y.split(",")]
            data20 = dataframe.sort_values(x)

            data21 = []

            for col in y_list:
                data21.append(data20[col])

            plt.stackplot(data20[x], *data21, labels=y_list)
            plt.xlabel(x)
            plt.ylabel("Values")
            plt.title("==Stack chart==")
            plt.legend(loc="upper left")

            figure = plt.gcf()
            plt.show()

        else:

            print("Invalid choice!")

    except ValueError:

        print("\nInvalid input! Please enter a number for the choice and use columns with suitable (numerical) values.")

    except IndexError:

        print("\nIndex out of range! There is not enough data to draw this chart.")

def save_chart():
    
    print("\n== Save Visualization ==")

    try:

        name = input("\nEnter file name to save the plot (e.g.,linechart.png) :")
        figure.savefig(name)
        print(f"Visualization saved as {name} successfully!")

    except ValueError:

        print("\nInvalid file name or format! Please use a valid name like linechart.png")


                
class SaleDataAnalyzer:

    
    def __init__(self):

        self.dataframe = None

    def main_data(self):

        while True:

            print("\n===========Data Analysis & Visualization Program=============")
            print("Please select an option:")
            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("============================================================")

            try:

                choice = int(input("\nEnter your choice :"))

                if choice==1:

                    load_data()

                elif choice==2:

                    explore_data()

                elif choice==3:

                    data_operations()

                elif choice==4:

                    clean_data()

                elif choice==5:

                    statstical_analysis()

                elif choice==6:

                    visualize_data()

                elif choice==7:

                    save_chart()

                elif choice==8:

                    print("\nExiting the program. Goodbye!")
                    break

                else:

                    print("Invalid choice!")

            except ValueError:

                print("\nInvalid input! Please enter a number between 1 and 8.")

            except IndexError:

                print("\nIndex out of range! Please select a valid option.")

sale_analyzr = SaleDataAnalyzer()
sale_analyzr.main_data()