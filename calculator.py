a=int(input("enter a"))
b=int(input("enter b"))
c=input("enter operator")
match c:
    case '+':
        print("a+b:",a+b)
    case '-':
        print("a-b:",a-b)
    case '*':
        print("a*b:",a*b)
    case '/':
        print("a/b:",a/b)
    case '//':
        print("a//b:",a//b)
    case  '%':
        print("a%b:",a%b)
    case _:
        print("wrong operator")
