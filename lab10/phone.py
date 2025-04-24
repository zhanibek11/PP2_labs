import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="chessy228",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def create_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    ''')
    conn.commit()


def insert_from_console():
    username = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    print("Data inserted from console.")

def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Data inserted from CSV.")


def update_data():
    username = input("Enter existing username to update: ")
    new_name = input("New name (press enter to skip): ")
    new_phone = input("New phone (press enter to skip): ")

    if new_name:
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, username))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, new_name or username))
    conn.commit()
    print("Data updated.")


def query_data():
    filter_value = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s OR phone LIKE %s", (f"%{filter_value}%", f"%{filter_value}%"))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def delete_data():
    target = input("Enter username or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s", (target, target))
    conn.commit()
    print("Deleted record(s).")


def main():
    create_table()
    while True:
        print("\nChoose an option:")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            csv_file = input("Enter CSV file path: ")
            insert_from_csv(csv_file)
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()