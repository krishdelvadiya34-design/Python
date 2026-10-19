import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

class Bookstore:

    def add_book(self,title,author,price,quantity):

        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

        data = pd.read_csv("Practice_test/inventory.csv")

        new_book = {
            "Title" : self.title,
            "Author" : self.author,
            "Genre" : "other",
            "Price" : self.price,
            "Quantity" : self.quantity
        }

        data.loc[len(data)] = new_book

        data.to_csv("Practice_test/inventory.csv",index=False)

        print("\nBook added successfully!")


    def update_inventory(self,title,quantity):
        
        data = pd.read_csv("Practice_test/inventory.csv")
        
        if title in data["Title"].values :

            data.loc[data["Title"] == title,"Quantity"] = quantity

            data.to_csv("Practice_test/inventory.csv",index=False)

            print("Stock updated successfully!")

        else:
            print("Book not found!")


    def record_sale(self,title,quantity):

        data = pd.read_csv("Practice_test/inventory.csv")
        sales = pd.read_csv("Practice_test/sales.csv")

        if title in data["Title"].values:

            if data.loc[data["Title"] == title, "Quantity"].values[0] >= quantity:

                price = data.loc[data["Title"] == title, "Price"].values[0]

                data.loc[data["Title"] == title, "Quantity"] -= quantity

                data.to_csv("Practice_test/inventory.csv", index=False)

                new_sale = {
                    "Date": pd.Timestamp.now().strftime("%Y-%m-%d"),
                    "Title": title,
                    "Quantity Sold": quantity,
                    "Total Revenue": price * quantity
                }

                sales.loc[len(sales)] = new_sale

                sales.to_csv("Practice_test/sales.csv", index=False)

                print("Sale recorded successfully!")

            else:
                print("Not enough stock available!")

        else:
            print("Book not found!")


    def generate_report(self):

        data = pd.read_csv("Practice_test/inventory.csv")
        sales = pd.read_csv("Practice_test/sales.csv")

        print("\n====Inventory Details====\n")

        print(data)

        total_book = data["Quantity"].sum()

        print(f"\nTotal book Quantity : {total_book}")

        print("\n====Sales Report====\n")

        print(sales)

        total_revenue = sales["Total_Revenue"].sum()

        print(f"\nTotal Revenue : {total_revenue}")


    def sales_analysis_computation(self):

        data = pd.read_csv("Practice_test/inventory.csv")
        sales = pd.read_csv("Practice_test/sales.csv")

        print("\n====Sales Analysis and Computation====")

        revenue = np.sum(sales["Total_Revenue"])

        print(f"\nTotal Revenue : {revenue}")

        avg_price = np.mean(data["Price"])

        print(f"\nAverage price of the book : {avg_price}")

        growth = sales["Total_Revenue"].pct_change() * 100

        print(f"\nRevenue Percentage Change : {growth}")

        book_sales = data.groupby("Title")["Price"].sum()

        best_book = book_sales.idxmax()

        max_value = book_sales.max()

        print(f"\nHighest selling book : {best_book}")

        print(f"Total Revenue          : {max_value}")


    def data_visualization(self):

        print("\n==Data Visualization==")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")
        print("4. Heatmap Chart")

        chart_choice = int(input("\nEnter your choice :"))

        data = pd.read_csv("Practice_test/inventory.csv")
        sales = pd.read_csv("Practice_test/sales.csv")

        if chart_choice==1:

            print("\n===Total Sales by Author===")

            merged = sales.merge(data, on="Title")

            plt.figure(figsize=(10, 6))
            sbn.barplot(data=merged,x="Author",y="Total_Revenue",color="teal",palette="Set2")

            plt.title("Total Sales by Author")
            plt.xticks(rotation=60, ha="right")
            plt.tight_layout()
            plt.show()

        elif chart_choice==2:

            print("\n===Monthly Sales Trends===")

            plt.figure(figsize=(10, 6))
            sbn.lineplot(data=sales,x="Date",y="Total_Revenue",palette="Set2")

            plt.title("Monthly sales")
            plt.xticks(rotation=70, ha="right")
            plt.tight_layout()
            plt.show()

        elif chart_choice==3:

            print("\n===Revenue share by book genre===")

            plt.figure(figsize=(10,6))
            plt.pie("Genre",labels="Price",colors="teal")

            plt.title("Revenue share by book genre")
            plt.tight_layout()
            plt.show()

        elif chart_choice==4:

            print("\n===Book Prices and Sales Volume Heatmap===")

            data = pd.merge(data, sales, on="Title")

            heatmap_data = data.pivot_table(
                index="Title",
                values=["Price", "Quantity Sold"],
                aggfunc="sum"
            )

            plt.figure(figsize=(10, 6))
            sbn.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".1f")

            plt.title("Book Prices and Sales Volume")
            plt.tight_layout()
            plt.show()

    def run_part(self):

        while True:
            print("\n====Book Inventory and Analytics system====")
            print("1. Add a new Book")
            print("2. Update Inventory")
            print("3. Sales Record")
            print("4. Bookstore Report")
            print("5. Sales Analysis")
            print("6. Data Visualization")
            print("7. Exit")

            choice = int(input("\nEnter your choice :"))

            if choice == 1:

                title = input("\nEnter book title :")
                author = input("Enter author :")
                price = float(input("Enter book price :"))
                quantity = int(input("Enter quantity :"))

                self.add_book(title, author, price, quantity)

            elif choice == 2:

                title = input("\nEnter book title to update stock :")
                quantity = int(input("Enter new quantity :"))

                self.update_inventory(title, quantity)

            elif choice == 3:

                title = input("\nEnter book title :")
                quantity = int(input("Enter quantity sold :"))

                self.record_sale(title, quantity)

            elif choice == 4:

                self.generate_report()

            elif choice == 5:

                self.sales_analysis_computation()

            elif choice == 6:

                self.data_visualization()

            elif choice==7:
                print("Thank you for using Book Inventory and Analytics system!")
                break

            else:
                print("\nInvalid choice!")

bookstore1 = Bookstore()
bookstore1.run_part()