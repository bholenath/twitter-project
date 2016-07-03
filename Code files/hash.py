import MySQLdb

cnxn = MySQLdb.connect(host = "localhost" ,user = "root" ,passwd= "" ,db= "twitter_data")
cursor = cnxn.cursor()
cnxn.autocommit(True)

common_users = open('common_hashtags.txt', 'a')

friends_ids = []
#friends_values = {}

query_check = """show tables from twitter_data"""
cursor.execute(query_check)   
results = cursor.fetchall()

for row in results:
    
    if (row[0] not in ("celebrity_tweets","celebrities",'celebrity_mentioned_count','celebrity_distinct_hashtags_count','celebrity_hashtags_count','users_common','hashtags_common')):
        query_check1 = """select user_id,user_name from """+row[0]+""""""        
        cursor.execute(query_check1)
        results1 = cursor.fetchall()
         
        for row1 in results1:        
            friends_ids.append(row1[0])
            #friends_values.update({row1[0]:row1[1]}) 
            
friends_ids = set(friends_ids)
friends_ids = list(friends_ids)
row3 = []
row2 = []

for index in range(len(friends_ids)):

    for index1 in range(index+1,len(friends_ids)):
    
        query_check3 = """ select c.celebrity_twitter_name,c1.celebrity_twitter_name from celebrities as c Join celebrities as c1 where c.celebrity_twitter_id = """+friends_ids[index]+""" and c1.celebrity_twitter_id = """+friends_ids[index1]+""""""  
        cursor.execute(query_check3)
        results3 = cursor.fetchall() 

        for row3 in results3:
            common_users.write("\nHashtags Common Between "+row3[0]+" and "+row3[1]+"\n")
        
        query_check2 = """ select count(c.hashtags) from celebrity_tweets as c JOIN celebrity_tweets as c1 ON c.users_mention_id = """+friends_ids[index]+""" and c1.users_mention_id = """+friends_ids[index1]+""" where (Distinct concat(c.user_twitter_id,' ',c.tweet)) in (Distinct concat(c1.user_twitter_id,' ',c1.tweet)) """      
        cursor.execute(query_check2)
        results2 = cursor.fetchall()
        
        for row2 in results2:
            print row2[0]
        
        common_users.write("\n"+str(row2[0])+"\n")
        common_users.write("\n*****************************\n")    
        
        query_check4 = """ insert into hashtags_common(celebrity1_name,celebrity2_name,celebrity1_id,celebrity2_id,common_hashtags) values('%s','%s','%s','%s','%d')""" % (row3[0],row3[1],friends_ids[index],friends_ids[index1],row2[0])
        cursor.execute(query_check4)
        
                
common_users.write("\n********** The End ************\n")  
common_users.close()      
