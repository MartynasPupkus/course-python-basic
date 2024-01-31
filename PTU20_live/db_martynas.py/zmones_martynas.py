import sqlite3

connector = sqlite3.connect('zmones_martynas.db')
cursor = connector.cursor()

def create_table(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    query = '''
CREATE TABLE IF NOT EXISTS friends (
first_name VARCHAR(50),
last_name VARCHAR(50)
email VARCHAR(250)
);
'''
    cursor.execute(query)
    connector.commit()

def insert_friend(connector: sqlite3.Connection, cursor: sqlite3.Cursor):
    print('Inserting a friend')
    first_name = input('First name:  ')
    last_name = input('Last name:  ')
    email = input('E-mail:  ')
    with connector:
        cursor.execute("INSERT INTO friends (first_name, last_name, email)")
    print("Done.")


if __name__ == "__main__":
    create_table(connector, cursor)
    while True:
        choice = input('Enter Command (help for help):  ')
        if choice.lower() in ['q', 'quit']:
            break
        if choice in ['h', 'help']:
            print('h, help\t this help')
            print('q, quit\t quit this program')
            print('i, insert\t a friend')
            print('a, all\tprint all friends')
            print('ff\t\tfind by first name')
        if choice.lower() in ['i', 'insert']:
            insert_friend(connector, cursor)
        if choice.lower() in ['a', 'all']:
        if choice.lower() in ['ff', 'find by first name']:
    
    
    
    connector.close()