import pyhdb
connection = pyhdb.connect(
    host="10.88.20.1",
    port=30015,
    user="HANABI",
    password="Sap123456"
)

cursor = connection.cursor()
cursor.execute('select * from portal.bi_dim_werks')
for i in cursor.fetchall():
    print(i)

connection.close()