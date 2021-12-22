import sqlite3

conn = sqlite3.connect("app.db")
c = conn.cursor()

c.execute("""INSERT INTO items (name,barcode,description,sku,exgst )VALUES(1,2,3,4,5)""")
c.execute("""INSERT INTO items (name, barcode, description,sku,exgst )VALUES('brain',123423,1234,5,'cv')""")
c.execute("""INSERT INTO items (name, barcode, description,sku,exgst )VALUES('brain',326823,'good',554,7)""")
c.execute("""INSERT INTO items (name, barcode, description,sku,exgst )VALUES('brain',345435,'bad',1631,6)""")

c.execute("""INSERT INTO users (firstname,lastname,email,yearlevel,team )VALUES('John','Doe','johndoe@gmail.com','9','')""")
c.execute("INSERT INTO users (firstname, lastname, email, yearlevel,team)VALUES('Craig','Cereberus','craigorphankicker@gmail.com','11','Big fluffy dogs')")


conn.commit()
conn.close()
