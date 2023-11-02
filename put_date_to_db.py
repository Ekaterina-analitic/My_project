import pymysql
connection = pymysql.connect(host='10.10.101.161', user = 'pyuser', password = '123456', database = 'test')
cursor = connection.cursor()
cursor.execute("insert into telsprav values('Ekaterina','Veselova','f','89123765643')")
connection.commit()
