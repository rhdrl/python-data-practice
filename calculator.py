print("Hello! My name is 계산기.")  
num1=float(input("첫 번째 수를 입력하세요: "))
operation=input("연산자를 입력하세요 (+, -, *, /): ")
num2=float(input("두 번째 수를 입력하세요: "))

if operation == "+":
    result = num1 + num2
    print(f"결과: {result:.2f}")
elif operation == "-":
    result = num1 - num2
    print(f"결과: {result:.2f}")
elif operation == "*":
    result = num1 * num2
    print(f"결과: {result:.2f}")
elif operation == "/":
    result = num1 / num2
    if num2 == 0:
            print("0으로 나눌 수 없습니다.")
    else:
            result = num1 / num2
            print(f"결과: {result:.2f}")
else:
        print("잘못된 연산자입니다. 올바른 연산자 (+, -, *, /)를 입력하세요.")


