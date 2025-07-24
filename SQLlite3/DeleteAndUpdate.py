from BOOK import Book
import sqlite3
connect = sqlite3.connect('Library.db')
cursor = connect.cursor()
sql_create_table = """
        CREATE TABLE Library (
            bookname text,
            author text,
            id integer   
        )
    """

sql_selectAll = """
    SELECT *FROM Library 
"""
sql_insert = """
        INSERT INTO Library VALUES(
            ?,?,?
        ) 
    """
sql_Delete_All = f"""
        DELETE FROM Library WHERE author = ?
    """
sql_Update_all = f"""
        UPDATE Library set author = ? WHERE bookname like ?
    """
def insert_book():
    newBook = Book()
    newBook.DataEntry()
    with connect:
        return cursor.execute(sql_insert, (newBook.bookname, newBook.author, newBook.ID))
    print("Enter data succesfully")
def Print():
    with connect:
        cursor.execute(sql_selectAll)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
def delete_book():
    with connect:
        author_name = input("Enter the name of author to delete all the books ")
        cursor.execute(sql_Delete_All,(author_name, ))
def main(): 
    try:
        # cursor.execute(sql_create_table)
        while(True):
            option = int(input("Press 0 to end request: "))
            if(option == 0): break
            insert_book()
        delete_book()
        connect.commit()
        Print()
        print()
        Print()        
    except Exception as e:
        
        print("Error: ", e)    
    connect.close()
main()