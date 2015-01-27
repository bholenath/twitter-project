from igraph import *
import cairo
import MySQLdb
#import random
#import webcolors
#import matplotlib

cnxn = MySQLdb.connect(host="localhost", user ="root", passwd ="", db="twitter_data")
cursor = cnxn.cursor()
cnxn.autocommit(True)

# query = """ select celebrity_twitter_name,count(*) from celebrities """
# cursor.execute(query)
# result = cursor.fetchall()

query1 = """ select nodes,weight from celebrity_specific_distinct_hashtags_count """
cursor.execute(query1)
result1 = cursor.fetchall()

query2 = """ select count(*) from celebrity_specific_distinct_hashtags_count """
cursor.execute(query2)
result2 = cursor.fetchall()

query3 = """ select source,target,weight from celebrity_hashtags_common """
cursor.execute(query3)
result3 = cursor.fetchall()

for row in result2:
    vertices = row[0]

g = Graph()
g.add_vertices(vertices)

g.vs["name"] = [row[0] for row in result1]
g.vs["label"] = g.vs["name"]
g.vs["weight"] = [row[1] for row in result1]
g.vs["color"] = "white"

for index,value in enumerate(g.vs["weight"]):
    if value >= 200:
        g.vs[index]["color"] = "red"
    elif 100 <= value < 200:
        g.vs[index]["color"] = "blue"
    elif 50 <= value < 100:
        g.vs[index]["color"] = "green"
    else:
        g.vs[index]["color"] = "yellow"

source_id = 0
target_id = 0

for row in result3:
    for index,value in enumerate(g.vs["name"]):
        if row[0] == value:
            source_id = index
            break
        else:
            continue
    for index,value in enumerate(g.vs["name"]):   
        if row[1] == value:
            target_id = index
            break
        else:
            continue    
    g.add_edges([(source_id,target_id)]) 
    
g.es["label"] = [row[2] for row in result3]
g.es["weight"] = g.es["label"]
g.es["color"] = "white"
#g.es["scaled_weight"] = 10
  
for index,value in enumerate(g.es["weight"]):    
    if value >= 120:
        g.es[index]["color"] = "red"
        # #g.es[index]["weight"] = (value / 200) + 10
    elif 50 <= value < 120:
        g.es[index]["color"] = "blue"
        # #g.es[index]["weight"] = (value / 200) + 10
    elif 10 <= value < 50:
        g.es[index]["color"] = "green"
        # #g.es[index]["weight"] = (value / 200) + 10    
    else:
        g.es[index]["color"] = "yellow"
        # #g.es[index]["weight"] = (value / 200) + 10
        
# print summary(g)        
#community = g.community_multilevel(weights=g.es["weight"])
#community = g.community_fastgreedy()
#size = max(community.membership)

# color_list = ['aqua','azure','black','blue','brown','chocolate','cyan','darkturquoise','fuchsia','green','lime','magenta',
# 'maroon','navy','orange','pink','purple','red','violet','yellow','grey','teal','aquamarine','bisque','coral','cornsilk','darkkhaki',
# 'darkolivegreen','orchid','olive','royalblue','saddlebrown','salmon','sandybrown','seagreen','seashell','sienna','silver','skyblue','slateblue',
# 'slategray','gold','peru','powderblue','rosybrown','lime','steelblue','tan','tomato','forestgreen','ivory','honeydew']
# display_color_list = []

# for name in matplotlib.colors.cnames.iteritems():
    # color_list.append(name)
    
# size_color_list = len(color_list)    

# for i in range(size+1):
    # number = random.randint(0,(size_color_list-1))
    # display_color_list.append(color_list[number])
    # # color1 = webcolors.normalize_hex(number)
    # # try:
        # # color = webcolors.hex_to_name(color1, spec='css3')
        # # color_list.append(color)
    # # except ValueError,e:
        # # number = "#%03X" % random.randint(0,0Xffffff)
        # # color1 = webcolors.normalize_hex(number)
        # # color = webcolors.hex_to_name(color1, spec='css3')
        # # color_list.append(color)
   
layout = g.layout_fruchterman_reingold(dim=2)
#palette = ClusterColoringPalette(size)
# # #layout1 = g.layout("large")

# display_color_list = list(display_color_list)
# size_list = len(display_color_list)

# for i in range(size_list):
    # print display_color_list[i][0]

visual = {}

visual["vertex_size"] = 14
visual["vertex_color"] = g.vs["color"]
visual["vertex_label"] = g.vs["label"]
visual["vertex_label_size"] = 6
visual["vertex_label_dist"] = 3
#visual["edge_label"] = g.es["label"]
visual["edge_width"] = 1
visual["edge_curved"] = True
#visual["edge_label_dist"] = -1
visual["edge_color"] = g.es["color"]
visual["layout"] = layout
#visual["mark_groups"] = True
visual["bbox"] = (1000,1000)
visual["margin"] = 20

# visual1 = {}

# #visual["vertex_size"] = 1
# visual1["vertex_color"] = g.vs["color"] #[color_list[x] for x in community.membership]
# #visual["vertex_label"] = g.vs["label"]
# #visual["vertex_label_size"] = 15
# #visual["vertex_label_dist"] = 5
# #visual["edge_label"] = g.es["weight"]
# #visual["edge_width"] = 1
# visual1["edge_color"] = g.es["color"]
# visual1["layout"] = layout1
# visual["bbox"] = (2000,2000)
# #visual["margin"] = 20


# WIDTH, HEIGHT = 1000, 1000

# surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
# ctx = cairo.Context(surface)
# ctx.scale (WIDTH, HEIGHT)
# ctx.rectangle(0, 0, 1, 1)
# ctx.set_source_rgba(0,0,0,0)
# ctx.fill()

#g.__plot__("twitter_network_common_users_fr.svg",palette,**visual)
plot(g, "twitter_network_common_hashtags_fr_g2.svg", **visual)
#surface.write_to_svg('fr_g2.svg')
g.write_graphml("hashtags_fr_g2.graphml")
#plot(g, "twitter_network_common_users_large.png", **visual1)
