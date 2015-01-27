import MySQLdb

cnxn = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "unique_users")
cursor = cnxn.cursor()
cnxn.autocommit(True)

cnxn1 = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor1 = cnxn1.cursor()
cnxn1.autocommit(True)

#common_users = open('celebrity_common_mention_tweets.txt', 'a')

friends_ids = []
#friends_values = {}

query_check = """select celebrity_twitter_name,celebrity_twitter_id from celebrities"""
cursor1.execute(query_check)   
results = cursor1.fetchall()

for row in results:  
    
    query_check2 = """ select count(*) from """+row[0]+"""_unique_users """      
    cursor.execute(query_check2)
    results2 = cursor.fetchall()
    
    for row2 in results2:               
      
        query_check4 = """ insert into number_unique_users(celebrity_name,celebrity_id,count) values('%s','%s','%d')""" % (row[0],row[1],row2[0])
        cursor1.execute(query_check4)