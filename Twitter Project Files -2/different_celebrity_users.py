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
    
    query_check2 = """ select c.user_twitter_id,c.user_name,count(Distinct concat(c.tweet,' ',c.user_twitter_id)) from celebrity_tweets as c where c.users_mention_id = """+row[1]+""" group by c.user_twitter_id,c.user_name """      
    cursor1.execute(query_check2)
    results2 = cursor1.fetchall()
    
    query_check3 = """ create table """+row[0]+"""_unique_users(id INT NOT NULL AUTO_INCREMENT,user_id VARCHAR(191) NULL,user_name VARCHAR(191) NULL,count INT NULL,PRIMARY KEY ( id )) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci"""
    cursor.execute(query_check3)

    for row2 in results2:               
      
        query_check4 = """ insert into """+row[0]+"""_unique_users(user_name,user_id,count) values('%s','%s','%d')""" % (row2[1],row2[0],row2[2])
        cursor.execute(query_check4)