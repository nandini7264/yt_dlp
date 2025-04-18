from yt_dlp import YoutubeDL
from pprint import pprint
import sqlite3
from random import randint
from time import sleep

conn = sqlite3.connect('data')
cur = conn.cursor()

#print(len(links))

# Create the table outside the loop
cur.execute("""CREATE TABLE IF NOT EXISTS data1(
	       url TEXT,
               title TEXT,
               description TEXT,
               likes INTEGER,
               views INTEGER
               )""")

page_size = 1
offset = 0

while True:
	cur.execute("SELECT link FROM links LIMIT ? OFFSET ?", (page_size, offset))
	links = cur.fetchall()

	if not links:
		break

	for link in links:
		url = link[0]
		print(url)

		try:
			with YoutubeDL() as yt:
				info = yt.extract_info(url, download=False)

				title = info.get("title", "")
				pprint(title)
				description = info.get("description", "")
				likes = info.get("like_count", 0)
				views = info.get("view_count", 0)
				print("HAHAHA")

				# Insert the information into the database
				cur.execute("INSERT INTO data1 (url, title, description, likes, views) VALUES (?, ?, ?, ?, ?)",
					    (url, title, description, likes, views))
				conn.commit()
				print("jhala bc")

		except Exception as e:
			print(f"Error processing {url}: {e}")

	offset += page_size

conn.close()

sleep(randint(10,20))

