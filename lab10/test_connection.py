import psycopg2

try:
    conn = psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="chessy228",
        host="localhost",
        port="5432"
    )
    print("✅ Connection successful")
    conn.close()
except Exception as e:
    print("❌ Error:", e)