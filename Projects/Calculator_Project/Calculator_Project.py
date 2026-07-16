# the meno!
def display_menu():
    print('========WELCOME TO OUR PROGRAME=======')
    print('==This is the calculator application==')
    print('--------------------------------------')
    print('1. Addition')
    print('2. Multiplication')
    print('3. Subtruction')
    print('4. Devition')
    print('5. Exit!')
    print('--------------------------------------')


def add():
    n1 = int(input('First number : '))
    n2 = int(input('second number : '))
    sum = n1 + n2
    print(n1,'+',n2, '=', sum)
def mul():
    n1 = int(input('First number : '))
    n2 = int(input('second number : '))
    ml = n1 * n2
    print(n1,'*',n2, '=',ml)
def sub():
    n1 = int(input('First number : '))
    n2 = int(input('second number : '))
    sub = n1 - n2
    print(n1,'-',n2, '=',sub)
def dev():
    n1 = int(input('First number : '))
    n2 = int(input('second number : '))
    sub = n1 / n2
    print(n1,'/',n2, '=',sub)
    
    
    
    
def main():
    display_menu()
    while True:
        choice = int(input('Enter your choice : '))

        if choice == 1:
            add()
        elif choice == 2:
            mul()  
        elif choice == 3:
            sub() 
        elif choice == 4:
            dev()
        elif choice == 5:
            break
        else:
            print('sorry the number is invalid number')
            
main()