import MySQLdb

cnxn = MySQLdb.connect(host="localhost", user="root", passwd="", db="twitter_data")
cursor = cnxn.cursor()
print  "Hello"