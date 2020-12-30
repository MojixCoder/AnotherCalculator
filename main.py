

#Get Numbers !

num_flag = False


while not(num_flag):
    num1 = input('Enter First Number: ')
    if not(num1.isnumeric()):
        print("Enter a Valid Number Please! \n")
        continue
    num2 = input('Enter Second Number: ')
    if not(num2.isnumeric()):
        print("Enter a Valid Number Please! \n")
        continue
    num_flag = True



#Get Operator

operator_flag = False

while not(operator_flag):
    operator = input("Operator: + - * / \nEnter Your Operator: ")

    if operator not in ['+', '-', '*', '/']:
        print("Enter a Valid Operator Please !")
        continue
    
    operator_flag = True

num1 = float(num1)
num2 = float(num2)

result = None

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    if num2 == 0:
        result = "Devision By Zero!"
    else:
        result = num1 / num2

print(f"Result={result}\n")
