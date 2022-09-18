first=input("Enter the first value");
second=input("enter the second value");
operator=input("Enter the operator(+,-,*,%)");
first=int(first)
second=int(second)
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="%":
    print(first%second)
elif operator=="/":
    print(first/second)
