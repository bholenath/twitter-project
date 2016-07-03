import MySQLdb

cnxn1 = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor1 = cnxn1.cursor()
cnxn1.autocommit(True)

#common_users = open('celebrity_common_mention_tweets.txt', 'a')

#friends_ids = []
#friends_values = {}

query_check = """select nodes from celebrity_number_unique_users """
cursor1.execute(query_check)   
results = cursor1.fetchall()

for row in results:  
    
    query_check4 = """ insert into celebrity_number_unique_users(id) values('%s')""" % (row[0])
    cursor1.execute(query_check4)