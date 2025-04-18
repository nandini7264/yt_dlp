from yt_dlp import YoutubeDL
from pprint import pprint
import sqlite3

conn = sqlite3.connect('data')
cur = conn.cursor()

page_size = 1
offset = 0

links_all = []


while True:
	cur.execute("select link from link limit ? offset ?", (page_size, offset))
	links = cur.fetchall()
	
	if not links:
		break;
	
	for link in links:
		url = link[0]
		print(url)
		links_all.append(url)
		print(links_all)
#		print(link[0])
		try:
			video_url = str(link[0])
			#video_url ="https://www.youtube.com/watch?v=tWCLD8wmBs8"
			opts = {
				"title": True,
				"getcomments": True,
				"getdescription": True,
				"likecount": True,
				"viewcount": True
			}
			
			cur.execute("""CREATE TABLE info(title text, desc text, likes int, views int)""")	


			with YoutubeDL(opts) as yt:
				info = yt.extract_info(video_url, download=False)
				comments = info["comments"]
				pprint(comments)

				title = info["title"]
				pprint(title)
				query = "insert into title values('"
				query= query + str(title) + "');"
				print(query)
				conn.execute(query)
				conn.commit()

				desc = info["description"]
				query = "insert into title values('"
				query= query + str(title) + "');"
				print(query)
				conn.execute(query)
				conn.commit()
			
				likes = info["like_count"]
				query = "insert into title values('"
				query= query + str(title) + "');"
				print(query)
				conn.execute(query)
				conn.commit()
			
				views = info["view_count"]
				query = "insert into title values('"
				query= query + str(title) + "');"
				print(query)
				conn.execute(query)
				conn.commit()
			
				thread_count = info["comment_count"]
				
		except:
			print("ooooooooo")

	offset += page_size
conn.close()

