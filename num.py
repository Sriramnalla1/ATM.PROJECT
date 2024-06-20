username = 'Sriram'
password = 'Ram7221'

c_name = input("Enter your name:")
c_pass = str(input("Enter your password:"))

if username == c_name and password == c_pass:
    print('''
        1. Deposite
        2. withdraw
        3. Ministatement
        4. Exit
        ''')
    amount = 10000
    option = int(input("Select your option:"))
    if option == 1:
        dep = int(input("Enter your amount:"))
        amount = amount + dep
        print("Total amount",amount)
    elif option == 2:
        withd = int(input("Enter your amount:"))
        amount = amount - withd
        print("Total amount",amount)
    elif option == 3:
        print("======ATM=====")
        print("Username",username)
        print("Amount",amount)
        print("Thanks for visit")
        print("==============")
    elif option == 4:
        exit()

else:
    print("Please enter correct login")
            