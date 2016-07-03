import MySQLdb

cnxn1 = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor1 = cnxn1.cursor()
cnxn1.autocommit(True)

#common_users = open('celebrity_common_mention_tweets.txt', 'a')

#friends_ids = []
#friends_values = {}

query_check = """ delete from celebrity_hashtags_common where weight = 0 """
cursor1.execute(query_check)