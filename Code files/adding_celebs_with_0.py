import MySQLdb

cnxn1 = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor1 = cnxn1.cursor()
cnxn1.autocommit(True)

#common_users = open('celebrity_common_mention_tweets.txt', 'a')

#friends_ids = []
#friends_values = {}

query_check = """select celebrity_twitter_name,celebrity_twitter_id from celebrities where celebrity_twitter_id not in (select celebrity_twitter_id from celebrity_specific_hashtags_count) """
cursor1.execute(query_check)   
results = cursor1.fetchall()

for row in results:  
    
    query_check4 = """ insert into celebrity_specific_hashtags_count(nodes,id,celebrity_twitter_id,weight) values('%s','%s','%s','%d')""" % (row[0],row[0],row[1],0)
    cursor1.execute(query_check4)