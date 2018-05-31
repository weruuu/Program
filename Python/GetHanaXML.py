import pyhdb
connection = pyhdb.connect(
    host="10.88.20.1",
    port=30015,
    user="HANABI",
    password="Sap123456"
)
def writefile(PackageName,ModelName):
    cursor = connection.cursor()
    cursor.execute('select cdata from _sys_repo.active_object where object_suffix like \'%view\' and package_id like \'%'+ PackageName +'%\' and object_name like \''+ ModelName +'\'')

    xmlfile = cursor.fetchone()[0].read(999999)
    fp = open("model.xml","w")
    fp.write(xmlfile)
    fp.close
    connection.close()