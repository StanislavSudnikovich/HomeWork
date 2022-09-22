import sqlite3

conn = sqlite3.connect('alpha_digit.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_alpha
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                col_1 TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_digit
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                col_1 INTEGER)''')
list_ = ['sdsf', 1, 5, 7, 4, 'fdg']
for i in list_:
    if type(i) == str:
        cursor.execute("""
                    INSERT INTO tab_alpha(
                        col_1)
                    VALUES(?)
                    """, (i,))
        cursor.execute("""
                    INSERT INTO tab_digit(
                        col_1)
                    VALUES(?)
                    """, (len(i),))
    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute("""
                        INSERT INTO tab_digit(
                            col_1)
                        VALUES(?)
                        """, (i,))
        else:
            cursor.execute("""
                        INSERT INTO tab_alpha(
                            col_1)
                        VALUES ('Нечетное')
                        """)
conn.commit()
cursor.execute('''SELECT*FROM tab_alpha''')
alpha = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_digit''')
digit = cursor.fetchall()
print(alpha, digit)
a = 0
for i in digit:
    a += 1
if a > 5:
    cursor.execute('''DELETE FROM tab_alpha WHERE id=1''')
    print('Число записей в числовой таблице больше 5, удаляем первую запись в текстовой таблице')
else:
    cursor.execute('''UPDATE tab_alpha SET col_1='world' WHERE id=1''')
    print('Число записей в числовой таблице меньше либо равно 5, обновляем первую запись в текстовой таблице')
conn.commit()
cursor.execute('''SELECT*FROM tab_alpha''')
alpha = cursor.fetchall()
cursor.execute('''SELECT*FROM tab_digit''')
digit = cursor.fetchall()
print(alpha, digit)
