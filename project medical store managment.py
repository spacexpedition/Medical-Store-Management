# ALL IMPORT STATEMENTS #
from datetime import datetime as t
import mysql.connector as sql
connect = sql.Connect(
    host='localhost',
    user='root',
    password='Q1w2e3r4t5y6u7@',
    database='medical_store_record')
if connect.is_connected:
    print("successfully connected")
cursor = connect.cursor()
a = t.now()
# EXIT FUCNTION #


def exit1():

    print("     THANK YOU      ")
    print(a)
    print("SYSTEM CLOSED")
    exit()
# LOGIN MENU#


def menu1():
    print(" YOUR WELLWISHER MEDICAL STORE ")
    print(a)
    print("1. Login")
    print("2. Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        login()
    elif select == 2:
        exit1()
    else:
        print("Invalid value")
    menu1()
# LOGIN FUNCTION#


def login():
    print(a)
    username = input("Enter your User name")
    password = input("Enter your password")
    check = f"select User_Name from account_details where User_Name ='{username}' and password = '{password}';"
    cursor.execute(check)
    if not cursor.fetchone():
        print("Login Failed")
    else:
        print("Login successfull")
        mainmenu()
# MAINMENU #


def mainmenu():
    print(a)
    print("1. Customer Account")
    print("2. Medicine Management")
    print("3.Customer Bill")
    print("4.Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        customer_account()
    elif select == 2:
        medicine_management()
    elif select == 3:
        customer_bill()
    elif select == 4:
        menu1()
    else:
        print("Invalid Choice. Enter 1-4")
# CUSTOMER ACCOUNT#


def customer_account():
    print(a)
    print("1.New Account")
    print("2.Existing Account")
    print("3.Exit")
    select = int(input("Enter your choice"))
    if select == 1:
        new_account()
    elif select == 2:
        existing_account()
    elif select == 3:
        mainmenu()
    else:
        print("Invalid Choice")
# CREATE CUSTOMER NEW ACCOUNT #


def new_account():
    print(a)
    account_number = int(input("enter your acct_number:"))
    patient_name = input("enter your name:")
    age = int(input("enter your age:"))
    address = input("enter your address:")
    phone_number = int(input("enter your number:"))
    balance_amount = float(input("enter your amount:"))
    x = "insert into customers_details values(" + str(
    account_number) + ",'" + patient_name + "'," + str(age) + ",'" + address + "'," + str(
    phone_number) + "," + str(balance_amount) + ")"
    print(x)
    cursor.execute(x)
    connect.commit()
    print("Customer Account Created Successful")
    I = ("select*from customers_details")
    cursor.execute(I)
    J = cursor.fetchall()
    for row in J:
        print(row)
        print("\n")
    customer_account()
# CHECK EXISTING ACCOUNT IF NOT CREATE NEW ACCOUNT#


def existing_account():
    print(a)
    number = input("Enter your phone number")
    g = f" select phone_number from customers_details where phone_number = '{number}'; "
    cursor.execute(g)
    if not cursor.fetchall():
        print("Account Does not exist")
        print("create new account")
        print("1.Wanna create new account")
        print("2. Exit")
        option = input("Enter your choice")
        if option == 1:
            new_account()
        elif option == 2:
            customer_account()
    else:
        print("your account exists")
        K = ("select*from customers_details")
        cursor.execute(K)
        L = cursor.fetchall()
        for row in L:
            print(row)
            print("\n")
        customer_account()

# MEDICINE DETAILS#


def medicine_management():
    print(a)
    print("1.Add new medicines")
    print("2.Check in stock medicines")
    print("3.exit")
    select = int(input("Enter your choice"))
    if select == 1:
        new_medicines()
    elif select == 2:
        stock_medicine()
    elif select == 3:
        mainmenu()
    else:
        print("Inavlid Input")
        medicine_management()
# ADD NEW MEDICINES IN STOCK #


def new_medicines():
    print(a)
    add_new_medicine = int(input("Enter number of new medicines to add"))
    for d in range(add_new_medicine):
        medicine_name = input("Enter name of medicine")
        medicine_code = int(input("Enter code of medicine"))
        cgst = float(input("Enter cgst of medicine"))
        sgst = float(input("Enter sgst of medicine"))
        quantity = int(input("Enter quantity of medicine"))
        cost_per_each = float(input("Enter per cost per each medicine"))
        e = "insert into medicine_details value('{}',{},{},{},{},{})".format(medicine_name,
                                                    medicine_code, cgst, sgst, quantity, cost_per_each)
        cursor.execute(e)
        connect.commit()
        print("Medicines Added in Stock")
        M = ("select*from medicine_details")
        cursor.execute(M)
        N = cursor.fetchall()
        for row in N:
            print(row)
            print("\n")
        medicine_management()
# CHECK MEDICINES IN STOCK #


def stock_medicine():
    print(a)
    code = int(input("Enter medcine code"))
    h = f" select * from medicine_details where medicine_code = '{code}' "
    cursor.execute(h)
    if not cursor.fetchall():
        print("Out of Stock")
        medicine_management()
    else:
        print("In Stock")
        O = ("select*from medicine_details")
        cursor.execute(O)
        P = cursor.fetchall()
        for row in P:
            print(row)
            print("\n")
    medicine_management()
# BILL GENERATION#


def customer_bill():
    print(a)
    patient_name = input("enter the patient_name :")
    no = int(input('enter the number of medicine:'))
    print('customer name:', patient_name)
    for i in range(no):
        medicine = input('enter medicine name')
        check1 = f"select*from medicine_details where medicine_name ='{medicine}' "
        cursor.execute(check1)
        data = cursor.fetchall()
        for row in data:
            print('medicine code of', medicine, ':', row[1])
            print('cgst of', medicine, ':', row[2])
            print('sgst of', medicine, ':', row[3])
            print('cost_per_each of', medicine, ':', row[5])
            connect.commit()
            account = input("Enter your Account Number")
            f = f"select balance_amount from customers_details where account_number ='{account}'"
            cursor.execute(f)
            data1 = cursor.fetchall()
            data1 = list(data1[0])
            print(data1)
            connect.commit()
            print("rows affected:", cursor.rowcount)
            connect.commit()
            quantity = int(input("Enter the quantity:"))
            total_amount=row[5]*quantity
            print("total_amount of", medicine, ':', total_amount)
            discount = int(input("Enter discount on total amount"))
            dobc = total_amount*discount/100
            v_sql_insert = " insert into patient_bill (medicine_name, medicine_code, cgst, sgst, cost_per_item, " \
                           "quantity, " \
                           "discount_on_balance_amount, total_amount)values ('{}', {}, {}, {}, {}, {}, {}, '{}' )".format\
                 (medicine, row[1], row[2], row[3], row[4], quantity, dobc, total_amount)
            cursor.execute(v_sql_insert)
            connect.commit()
            print("Bill Generated")
            Q = ("select*from patient_bill")
            cursor.execute(Q)
            R = cursor.fetchall()
            for row in R:
                print(row)
                print("\n")
            mainmenu()
# CREATING TABLES IN DATABASE #


cursor.execute('create table if not exists account_details('
                'User_Name varchar(30) primary key,'
                'password varchar(30) unique)')
print(a)
print("1.New user(signup)")
print("2.Exisiting User(signin)")
Action = int(input("Enter your Action"))
# ADDING NEW USER #
if Action == 1:
    Add_user = int(input("Enter the number of new users to Add "))
    for b in range(Add_user):
        User_Name = str(input("Enter your preffered User Name"))
        Password = str(input("Enter your password"))
        A = "insert into account_details values('{}','{}')".format(User_Name, Password)
        cursor.execute(A)
        connect.commit()
        print("Users Added Successfully")
        S = ("select*from account_details")
        cursor.execute(S)
        T = cursor.fetchall()
        for row in T:
            print(row)
            print("\n")
else:
    print("WELCOME USER")
# CUSTOMER DETAILS TABLES #
cursor.execute('create table if not exists customers_details('
                'account_number int primary key,'
                'patient_name varchar(30),'
                'age int,address varchar(50),'
                'phone_number bigint(11),balance_amount float)')
# MEDICINE DETAILS TABLE #
cursor.execute('create table if not exists medicine_details('
               'medicine_name varchar(30),'
               'medicine_code int,'
               'cgst float,sgst float,'
               'total_quantity float,'
               'cost_per_each float)')
# PATIENT BILL TABLE #
cursor.execute('create table if not exists Patient_bill('
               'medicine_name varchar(30),'
               'medicine_code int ,cgst float,'
               'sgst float,cost_per_item float,'
               'quantity int,'
               'discount_on_balance_amount int,'
               'total_amount float)')
print('table created')
print(a)
menu1()
