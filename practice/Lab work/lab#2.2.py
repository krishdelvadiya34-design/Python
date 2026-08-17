#question: 1

num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
num3=int(input("enter a number3:"))

if num1>num2:
    if num1>num3:
        print(f"num1 is max. number")
if num2>num1:
    if num2>num3:
        print(f"num2 is max. number")
if num3>num1:
    if num3>num2:
        print("num3 is max. number")

#question 2

a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))

if a<b:
    if a<c:
        print("a is minimum number")
if b<a:
    if b<c:
        print("b is miinimum number")
if c<a:
    if c<b:
        print("c is minimum number")

#question 3:

n1=int(input("enter a number1:"))
n2=int(input("enter a number2:"))
n3=int(input("enter a number3:"))
n4=int(input("enter a number4:"))

if n1>n2:
    if n1>n3:
        if n1>n4:
            print("n1 is maximum number")
else:
    if n2>n1:
        if n2>n3:
            if n2>n4:
                print("n2 is maximum number")
    if n3>n1:
        if n3>n2:
            if n3>n4:
                print("n3 is maximum number")
    if n4>n1:
        if n4>n2:
            if n4>n3:
                print("n4 is maximum number")


#question 4:

choice1=int(input("enter a number:"))
choice2=int(input("enter a number:"))

print("number 1 is for addition(+)")
print("number 2 is for substraction(-)")
print("number 3 is for multiplication(*)")
print("number 4 is for division(/)")

choice=int(input("enter your choice (+,-,*,/) :"))

match choice:
        case 1:
         k=choice1+choice2
         print(k)
        case 2:
         r=choice1-choice2
         print(r)
        case 3:
         i=choice1*choice2
         print("3")  
        case 4:
         s=choice1/choice2
         print("4")



#question 5:

print("=====welcome to fun food=====")

print("1. sandwich")
print("2. pizza")
print("3. dosha")

order=int(input("\nenter your choice food:"))

match order:
      case 1:
        print("\n===sandwich menu===")
        print("1. grilled sandwich")
        print("2. cheese sandwich")
        print("3. veg.sandwich")

        suborder=int(input("\nenter your choice sandwich:"))

        match suborder:
              case 1:
                print("you ordered grilled sandwich")
              case 2:
                print("you ordered cheese sandwich")
              case 3:
                print("you ordered veg. sandwich")
              case _:
                print("you ordered invalid choice")
      case 2:
        print("\n===pizza menu===")
        print("1. margrita pizza")
        print("2. double layer pizza")
        print("3. cheese burst pizza")

        suborder=int(input("\nenter your choice pizza:"))

        match suborder:
            case 1:
                print("you ordered margrita pizza")
            case 2:
                print("you ordered double layer pizza")
            case 3:
                print("you ordered cheese burst pizza")
            case _:
                print("you ordered invalid choice")           

      case 3:
        print("\n===dosha menu===")
        print("1. spring roll dosha")
        print("2. maysur dosha")
        print("3. fun food special dosha")

        suborder=int(input("\nenter your choice dosha:"))

        match suborder:
            case 1:
                print("you ordered spring roll dosha")
            case 2:
                print("you ordered maysur dosha")
            case 3:
                print("you ordered fun food special dosha")
            case _:
                print("you ordered invalid choice")

      case _:
        print("you ordered invalid choice")           


#question 6:

print("\n=====Telecom calling system=====")  
print("1. English")
print("2. Gujarati")
print("3. Hindi")

choice=int(input("enter your choice language:"))

match choice:
    case 1:
        print("\nyou selected English language")
        print("1. balance inquiry")
        print("2. Validity Check")
        print("3. data usage")

        subchoice=int(input("\nenter your problem:"))

        match subchoice:
          case 1:
           print("your current balance is ₹25,000")
          case 2:
           print("your service validity will expire in 20 days")
          case 3:
           print("your data usage is 1.23 gb of today")
          case _:
              print("invalid choice")
       
    case 2:
        print("\nyou selected gujarati language")
        print("1. balance inquiry")
        print("2. Validity Check")
        print("3. data usage")

        subchoice=int(input("\nenter your problem:"))

        match subchoice:
           case 1:
              print("tamaru balance ₹25,000 chhe")
           case 2:
              print("tamari service validity 20 divas ma samapt thay jase")
           case 3:
              print("tamaro ajno data vapras 1.23 gb chhe")
           case _:
              print("invalid choice")
       

    case 3:
        print("\nyou selected hindi language")
        print("1. balance inquiry")
        print("2. Validity Check")
        print("3. data usage")
          
        subchoice=int(input("\nenter your problem:"))

        match subchoice:
           case 1:
              print("apka balance ₹25,000 hai")
           case 2:
              print("apki service validity 20 dino me samapt ho jaye gi")
           case 3:
              print("apka ajka data usage 1.23 gb hai")
           case _:
              print("invalid choice")

    case _:
      print("invalid choice")