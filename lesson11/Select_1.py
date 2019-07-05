import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor() # 建立 cursor

# 查詢 Table META-INFO
cursor.execute('PRAGMA TABLE_INFO({})'.format('lotto'))
names = [t[1] for t in cursor.fetchall()]
for name in names:
    print(name, end='\t')
print('\n-----------------------------------------------')

conn.close()