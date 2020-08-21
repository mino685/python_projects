from googlesearch import search 
from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime
import os
import schedule
import time

#variables
keyword = "Boataround"	# keyword entered into google search engine
url = "boataround.com"  # link to have a scrapper search
resultsNumber = 30		# number of google search results
fileName = "scrapperResutls.csv" # the name of the file where the daily scrap data will be stored
hours = 9	# hour of the day when the auto scrapping will start


#functions

#scrapper functionality
def scrapper():
	links = 0
	allLinks = 0
	print("--------------------------------------")
	print("       scrapping is running...        ")
	print("--------------------------------------")
	for j in search(keyword, country='slovakia', stop=resultsNumber): 
		print("Webpage:", j)	
		page = requests.get(j)
		cont = page.content
		soup = BeautifulSoup(page.content, 'html.parser')
		resp = soup.text.find(url)
		allLinks +=resp
		
		if resp > 0: 
			links += 1
			print("Number of", keyword, "links on this Webpage is: ", resp)
		else:
			print("Number of", keyword, "links on this Webpage is: 0")

		print("--------------------------------------")
		resp = 0
	os.system('cls')
	print("-----------------------------------------------------------")
	print("|                   SCRAPPER RESULTS:                     |")
	print("-----------------------------------------------------------")
	print("| Number of Pages with Boataround links is : ", links,"/",resultsNumber,"    |")
	print("| Number of all Boataround links is : ", allLinks,"             |")
	print("-----------------------------------------------------------")
	print("*The data is stored in a",fileName," on your file system\n")

	print("Automatic scrapping will run every day at "+str(hours)+":00 o'clock." )
	
	updateFile(links, allLinks)
	
#csv writing functionality
def updateFile(links, allLinks):
	fields=[datetime.now().date(),str(datetime.now().hour) + ':' + str(datetime.now().minute), links, allLinks]
	with open(fileName, 'a', newline='') as f:
		writer = csv.writer(f, delimiter=';')
		writer.writerow(fields)	

#auto scrapper
if hours < 10: hours = "0"+str(hours)
#schedule.every().minute.do(scrapper) #Auto scrapper every minute - just for testing
schedule.every().day.at(str(hours)+":00").do(scrapper) #Auto scrapper every day

scrapper()

while True:
	schedule.run_pending()


		