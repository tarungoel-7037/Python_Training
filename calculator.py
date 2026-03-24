def main():
    operation = input('Enter the operation you want to perform ')
    try:
        a = int(input('Enter first number '))
        b = int(input('Enter second number '))
    except ValueError:
        print('Please enter valid numbers only')
        return

    if operation == '+':
        print(f'{a} {operation} {b} => {a+b}') 
    elif operation == '-':
        print(f'{a} {operation} {b} => {a-b}')
    elif operation == '*':
        print(f'{a} {operation} {b} => {a*b}')
    elif operation == '/':
        if b == 0:
            print('Can not divide by zero')
        else:
            print(f'{a} {operation} {b} => {a/b}') 
    else:
        print('Enter valid input')  
        
if __name__ == '__main__':
    main()


