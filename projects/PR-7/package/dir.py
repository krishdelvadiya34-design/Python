import datetime,random,uuid,math

def data():

    print("========================\n")
    dict={
        "math" : math,
        "datetime" : datetime,
        "random" : random,
        "uuid" : uuid
    }

    data = input("Enter module name to explore :")

    if data in dict:
        data = dir(dict[data])
        
        print(f"\nAvailable Attributes in math module :\n\n{data}")

    else:
        print("Invalid module name")

    print("\n========================")

