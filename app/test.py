import database

db = database.Database()
db.load_db()
print(db.Codes)
''' 
db = database.Database()
db.create_db()
code = database.Code()
code.href = "123"
code.id = 45
code.data = "xzxcvbnm"
db.Codes.append(code)

db.update()
'''