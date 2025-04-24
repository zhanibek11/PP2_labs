import psycopg2
import csv
import re

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook_db",
    user="postgres",
    password="chessy228",
    port="5432"
)
cur = conn.cursor()

# Create table
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20)
        );
    """)
    conn.commit()

# Insert from csv
def insert_from_csv(filename):
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                cur.execute("SELECT phone FROM phonebook2 WHERE first_name = %s", (row[0],))
                user = cur.fetchone()
                if user:
                    cur.execute("UPDATE phonebook2 SET phone = %s WHERE first_name = %s", (row[1], row[0]))
                else:
                    cur.execute("INSERT INTO phonebook2 (first_name, phone) VALUES (%s, %s)", (row[0].strip(), row[1].strip()))
        conn.commit()
        print("Data inserted successfully")
    except FileNotFoundError:
        print("File not founded")

# Insert from console
def insert_from_console():
    name = input("Enter first name: ")
    phone = input("Enter phone: ")
    cur.execute("SELECT phone FROM phonebook2 WHERE first_name = %s", (name,))
    user = cur.fetchone()
    if user:
        cur.execute("UPDATE phonebook2 SET phone = %s WHERE first_name = %s", (phone, name))
    else:
        cur.execute("INSERT INTO phonebook2 (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

# Update datas
def update_data():
    enter = input("What you want to update: 'name' or 'phone'? ").strip().lower()
    if enter == "name":
        old_name = input("Enter current name: ")
        new_name = input("Enter new name: ")
        cur.execute("SELECT * FROM phonebook2 WHERE first_name = %s", (old_name,))
        user = cur.fetchone()
        if user:
            cur.execute("UPDATE phonebook2 SET first_name = %s WHERE first_name = %s", (new_name, old_name))
            conn.commit()
            print("Data is updated.")
        else:
            print("No such user found.")
    elif enter == "phone":
        name = input("Enter name to change phone: ")
        new_phone = input("Enter new phone: ")
        cur.execute("SELECT * FROM phonebook2 WHERE first_name = %s", (name,))
        user = cur.fetchone()
        if user:
            cur.execute("UPDATE phonebook2 SET phone = %s WHERE first_name = %s", (new_phone, name))
            conn.commit()
            print("phone updated.")
        else:
            print("No such user found.")
    else:
        print("Wrong choice.")

# Query with filters
def query_data():
    print("\nSelect request type:")
    print("1. Show all users")
    print("2. Search by name")
    print("3. Search by phone")

    choice = input("Your choise (1-3): ").strip()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook2")
    elif choice == "2":
        namee = input("Enter name to search: ")
        cur.execute("SELECT * FROM phonebook2 WHERE first_name ILIKE %s", (f'%{namee}%',))
    elif choice == "3":
        phonee = input("Enter a phone number to search: ")
        cur.execute("SELECT * FROM phonebook2 WHERE phone ILIKE %s", (f'%{phonee}%',))
    else:
        print("Wrong choice.")
        return

    rows = cur.fetchall()
    cnt = 0
    if rows:
        for row in rows:
            cnt += 1

    pages = (cnt // 5) + 1
    page = 0
    cnt = 0

    if rows:
        print("\nResults:")
        statement = True
        while statement:
            for row in rows:
                choise = input("\nSelect operation: prev or next: ")
                if choise == "prev" and page == 0 and pages > 0:
                    print("It is the first page")
                elif choise == "prev" and page > 0 and pages > 0:
                    page -= 1
                    cnt = 0
                    for row1 in rows:   
                        cnt += 1
                        if cnt >= (page-1)*5 and cnt <= page * 5:
                            print(f"ID: {row1[0]}, Name: {row1[1]}, Phone: {row1[2]}")
                elif choise == "next" and page == pages:
                    print("It is the last page")
                elif choise == "next" and page != pages and pages > 0:
                    page += 1
                    cnt = 0
                    for row1 in rows:
                        cnt += 1
                        if cnt >= (page-1)*5 and cnt <= page * 5:
                            print(f"ID: {row1[0]}, Name: {row1[1]}, Phone: {row1[2]}")
                elif choise != "next" and choise != "prev":
                    print("Wrong command!")
                    statement = False
                    break
    else:
        print("No such user found.")



# Delete data
def delete_data():
    filter = input("Delete by 'name' or 'phone'? ").strip().lower()
    value = input("Enter the value to delete: ")
    if filter == "name":
        cur.execute("SELECT * FROM phonebook2 WHERE first_name = %s", (value,))
        user = cur.fetchone()
        if user:
            cur.execute("DELETE FROM phonebook2 WHERE first_name = %s", (value,))
            conn.commit()
            print("User deleted.")
        else:
            print("No such user found.")
    elif filter == "phone":
        cur.execute("SELECT * FROM phonebook2 WHERE phone = %s", (value,))
        user = cur.fetchone()
        if user:
            cur.execute("DELETE FROM phonebook2 WHERE phone = %s", (value,))
            conn.commit()
            print("User deleted.")
        else:
            print("No such user found.")
    else:
        print("Wrong choice.")


#Inserting many stident in line
def many_users():
    names = list(map(str, input("Enter name: ").split()))
    phones = list(map(str, input("Enter phones: ").split()))
    wrong_users = []
    wrong_phones = []
    if len(names) != len(phones):
        print("The number of names and phone numbers do not match!")
    else:
        for i in range(len(names)):
            if phones[i][0] == '+':
                cur.execute("SELECT phone FROM phonebook2 WHERE first_name = %s", (names[i],))
                user = cur.fetchone()
                if user:
                    cur.execute("UPDATE phonebook2 SET phone = %s WHERE first_name = %s", (phones[i], names[i]))
                else:
                    cur.execute("INSERT INTO phonebook2 (first_name, phone) VALUES (%s, %s)", (names[i], phones[i]))
                conn.commit()
            else:
                wrong_users.append(names[i])
                wrong_phones.append(phones[i])
    print("Data is updated.")
    if len(wrong_phones) > 0:
        print("Incorrect phone number entered:")
        for i in range(len(wrong_users)):
            print(f"ID: {i}, Name: {wrong_users[i]}, Phone: {wrong_phones[i]}")




#Starting position
if __name__ == "__main__":
    create_table()
    while True:    
        mom = int(input("\nChoose one of the variations:\n1 - insert from console\n2 - insert from csv\n3 - update values\n4 - query data\n5 - delete data\n6 - many users\nInput number: "))

        if mom == 1:
            insert_from_console()
        if mom == 2:
            insert_from_csv("/Users/kuanyshev11/Documents/zhanibek/labs/lab11/data.csv")
        if mom == 3:
            update_data()
        if mom == 4:
            query_data()
        if mom == 5:
            delete_data()
        if mom == 6:
            many_users()



    cur.close()
    conn.close()