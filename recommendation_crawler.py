# fetching recommended video links using a nested loop via one youtube video link that is given

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
#driver =( webdriver.Chrome(service = Service(ChromeDriverManager().install)), options==options)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


#driver.get("https://www.youtube.com/watch?v=Zq5K_5ec9Wg")
#time.sleep(10)

import sqlite3
import re

conn = sqlite3.connect('data')
cur = conn.cursor()

page_size = 1
offset = 0

#cur.execute("""CREATE TABLE links1(link text)""")


while True:
	cur.execute("SELECT link FROM link LIMIT ? OFFSET ?",(page_size, offset))
	links = cur.fetchall()

	if not links:
		break;

	for link in links:
		url = link[0]
		print(url)
#		patRegex = re.compile(r'https://www.youtube.com/*')
#		bro = patRegex.search(url)== None
#		while False:
#			print(url)
		try:
			driver.get(str(url)) 
			time.sleep(5)
			
			recommended_videos = driver.find_elements(By.CSS_SELECTOR, "#video-title")
			for video in recommended_videos:
				print(video.text)

			links1 = driver.find_elements(by=By.TAG_NAME,value="a")

			for links in links1:
				l = links.get_attribute("href")
				print(str(l))
				if str(l)!= "":
					query = "insert into link values('"
					query = query + str(l) + "');"
					print(query)
					conn.execute(query)
					conn.commit()
				print(str(l))
		
		except:
			print("try again")

#print(cur.fetchall())
conn.close()
driver.quit()
