import mysql.connector
from tabulate import tabulate
import os
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    auth_plugin="mysql_native_password",
    database="shop_database"
)


def clear_screen():
    input("Press Any Key to Continue...")
    os.system("cls")


def table_menu():
    os.system("cls")
    tableMenu = [
        ["MENU"],
        ["1. CREATE DATABASE"],
        ["2. INSERT DATA TO DATABASE"],
        ["3. READ DATABASE"],
        ["4. UPDATE DATABASE"],
        ["5. DELETE DATA"],
        ["6. DELETE DATABASE"],
        ["7. EXIT"]
    ]
    print(tabulate(tableMenu, headers="firstrow", tablefmt="psql"))


def create_db():
    try:
        sql = """CREATE TABLE customers 
        (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name VARCHAR(255), 
            address VARCHAR(255),
            no_hp VARCHAR(255),
            email VARCHAR(255),
            purchase_date DATETIME
        )"""
        my_cursor.execute(sql)
    except Exception as ex:
        print(ex)


def read_db():
    sql = "SELECT * FROM customers"

    try:
        my_cursor.execute(sql)
        res = my_cursor.fetchall()

        header = ["ID", "NAME", "ADDRESS", "NO HP", "EMAIL", "PURCHASE DATE"]
        print(tabulate(res, headers=header, tablefmt="psql"))
    except Exception as ex:
        print(ex)


def update_db():
    read_db()
    print("Enter ID of Data that you want to update")
    ID = int(input("ID: "))

    name = input("Name: ")
    address = input("Address: ")
    no_hp = input("Phone Number: ")
    email = input("Email: ")
    purchase_date = datetime.datetime.now()

    # Update name
    sql = """
    UPDATE customers SET name = %s, 
    address = %s, no_hp = %s, 
    email = %s, purchase_date = %s 
    WHERE id = %s"""
    val = (name, address, no_hp, email, purchase_date, ID)
    try:
        my_cursor.execute(sql, val)
        mydb.commit()
    except Exception as ex:
        print(ex)


def delete_db():
    read_db()
    print("Enter ID of Data that you want to update")
    ID = int(input("ID: "))

    sql = "DELETE FROM customers WHERE id = %s"
    val = (ID,)
    try:
        my_cursor.execute(sql, val)
        mydb.commit()
    except Exception as ex:
        print(ex)


def insert_db():
    print("INSERT NEW DATA")
    name = input("Name: ")
    address = input("Address: ")
    no_hp = input("Phone Number: ")
    email = input("Email: ")
    purchase_date = datetime.datetime.now()

    sql = "INSERT INTO customers (name, address, no_hp, email, purchase_date) VALUES (%s, %s, %s, %s, %s)"
    val = (name, address, no_hp, email, purchase_date)

    try:
        my_cursor.execute(sql, val)
        mydb.commit()
        print(my_cursor.rowcount, "was inserted")
    except Exception as ex:
        print(ex)


def delete_all_db():
    sql = "DROP TABLE IF EXISTS customers"

    try:
        my_cursor.execute(sql)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    my_cursor = mydb.cursor()
    while True:
        table_menu()
        num = int(input("choice (1/2/3/4/5/6/7): "))

        if num == 1:
            create_db()
            clear_screen()
        elif num == 2:
            insert_db()
            clear_screen()
        elif num == 3:
            read_db()
            clear_screen()
        elif num == 4:
            update_db()
            clear_screen()
        elif num == 5:
            delete_db()
            clear_screen()
        elif num == 6:
            delete_all_db()
            clear_screen()
        elif num == 7:
            break
        else:
            print("Error Input")
            clear_screen()
            continue

    my_cursor.close()

    
