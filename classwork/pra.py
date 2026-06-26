# even_number=[i for i in range(1,101) if i%2==0]
# print(even_number)


# square=[i*i for i in range(11)]
# print(square)

# a=['apple','banana','orange']

# upper=[i.upper()for i in a ]
# print(upper)

# num=[i for i in range(1,11)]
# print(num)

# square=[i*i for i in range(1,11)]
# print(square)

# cube=[i**i for i in range(1,11)]
# print(cube)

# even=[i for i in range(1,21) if i%2==0]
# print(even)

# odd=[i for i in range(1,21) if i%2!=0]
# print(odd)

# number=[1,2,3,4,5]

# multiply=[i*2 for i in number]
# print(multiply)

# name=["krish","vedang","dhyey","bhavo"]

# upper=[name.upper() for name in name]
# print(upper)

# len_s=["krish","vedang","dhyey","bhavo"]

# length=[len(lens) for lens in len_s]
# print(length)

# divide=[i for i in range(1,51) if i%3==0]
# print(divide)

# evensquare=[i*i for i in range (1,21) if i%2==0]
# print(evensquare)

# numbers = [5, 12, 7, 18, 25, 3]
# greater=[i for i in numbers if i>10]
# print(greater)

# names = ["Krish", "Raj", "Amit", "Priya"]
# len=[i for i in names if len(i)>4]
# print(len)

# nums = [5, -2, 8, -1, 10, -7]
# negative=[i for i in nums if i>0]
# print(negative)

# text = "pythonprogramming"
# vowels=[i for i in text if i!="a" and i!="e" and i!="i" and i!="o" and i!="u"]
# print("".join(vowels))

# words = ["apple", "banana", "mango"]
# first=[word[0] for word in words ]
# print(first)

# nested = [[1, 2], [3, 4], [5, 6]]
# flattened=[i for row in nested for i in row]
# print(flattened)

# table=[5*i for i in range(1,11)]
# print(table)

# num=int(input("Enter table number :"))
# for i in range(1,11):
#   print(f"{num} x {i} = {num*i}")

# words = ["apple", "banana", "kiwi", "mango"]

# char=[word for word in words if len(word) > 5]
# print(char)

matrix=[12,43,34]

matrix.sort()
print(matrix)

add=lambda x,y : x*y
print(add(10,20))

num=[1,2,3,4,5,6]

n= list(filter(lambda x: x%2==0, num))
print(n)
