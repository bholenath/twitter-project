import MySQLdb

cnxn1 = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor1 = cnxn1.cursor()
cnxn1.autocommit(True)

#common_users = open('celebrity_common_mention_tweets.txt', 'a')

#friends_ids = []
#friends_values = {}

query_check = """select c.celebrity_twitter_name,c.celebrity_twitter_id,count(distinct concat(ct.user_name,' ',ct.tweet)) from (celebrity_tweets as ct join celebrities as c on((ct.users_mention_id = c.celebrity_twitter_id))) group by c.celebrity_twitter_name,c.celebrity_twitter_id """
cursor1.execute(query_check)   
results = cursor1.fetchall()

for row in results:  
    
    query_check4 = """ insert into celebrity_mentions_count(nodes,id,celebrity_twitter_id,weight) values('%s','%s','%s','%d')""" % (row[0],row[0],row[1],row[2])
    cursor1.execute(query_check4)