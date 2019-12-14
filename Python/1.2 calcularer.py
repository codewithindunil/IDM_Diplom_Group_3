print('-----WELCOME-----')
firstValue=eval(input('Enter First Value : '))
secValue=eval(input('Enter Second Value : '))
print('+ or - or * or / ')
operator=input('Enter Your Operator : ')


if operator == '+':
    print('Result is : ',firstValue+secValue)
elif operator == '-':
    print('Result is : ',firstValue-secValue)
elif operator == '*':
    print('Result is : ',firstValue*secValue)
elif operator == '/':
    print('Result is : ',firstValue/secValue)
