from pymongo import MongoClient

client = MongoClient('mongodb://10.10.12.108',27017)

mydb = client['t31115db']

mycollection = mydb['Movies']
#Display records
print("Records Are: ")
print()
cursor = mycollection.find()
for record in cursor:
    print(record)


#Insert Documents
rec={
	"Name" : "",
	"Genre" : "",
	"Ticket": "",
	"Cast" : "",
	"Release" : "",
	"Director":"D6",
	"Producer":"P6"
}
rec1 = mycollection.insert(rec)

print()
print("Records after insert Are: ")
print()
cursor = mycollection.find()
for record in cursor:
    print(record)
    
#Update Records
rec2 = mycollection.update({"Producer" : "P6"},{"$set" : {"Name":"ABC"} },multi=1)
print("Records after update Are: ")
print() 
cursor = mycollection.find()
for record in cursor:
    print(record)
    
#Deleting records
rec3 = mycollection.remove({"Producer":"P6"},multi=1)
print("Records after remove Are: ")
print()
cursor = mycollection.find()
for record in cursor:
    print(record)

