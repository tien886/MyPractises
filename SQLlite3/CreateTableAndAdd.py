import sqlite3
conn = sqlite3.connect('car.db')
c = conn.cursor()
sql_create_table = """
    CREATE TABLE cars (
        name text,
        brand text,
        year integer
    )
"""
# sql_insert_table = f"""
#     INSERT INTO cars VALUES(
#     '{}', 
#     '{}',
#     {}
#     )
# """
def Insert():
    print("Nhập tên xe:")
    name = input()

    print("Nhập hãng xe:")
    brand = input()

    print("Nhập năm sản xuất:")
    year = int(input())
    sql_insert_table = f"""
    INSERT INTO cars VALUES(
    '{name}',
    '{brand}',
    {year}
    )
    """
    return sql_insert_table
def Print():
    conn = sqlite3.connect('car.db')
    c = conn.cursor()
    sql_selectAll_table = """
        SELECT * FROM cars
    """
    c.execute(sql_selectAll_table)
    rows = c.fetchall() 
    for row in rows:
        print(row)
def main():
    try:
        # c.execute(sql_create_table)
        while(True):
            option = input()
            if(option == "0"): break
            c.execute(Insert())
        c.commit()
    except Exception as e:
        print("Error:", e)
    conn.close()
    Print()
main()