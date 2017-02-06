
# 
# panel-body match
# 
# pip install beautifulsoup
#


from bs4 import BeautifulSoup
import urllib
import urllib2


list_of_urls = [
"http://www.lolking.net/summoner/euw/34061544/Jolar27"
]





for i in list_of_urls:

	print "scrapping this ...", i
	#full_text = full_text.encode('ascii',errors='ignore')
	#full_text = urllib.request.urlopen(i).read().decode("utf-8")
	#full_text = urllib.request.urlopen(i)

	#response = urllib2.urlopen(i)
	#full_text = response.read()
	#http://www.lolking.net/summoner/euw/34061544/Jolar27


	#response = urllib2.urlopen('http://www.lolking.net/summoner/euw/34061544/Jolar27?scroll=1407')


	#response = urllib2.urlopen(i)
	#response = urllib2.urlopen("http://www.lolking.net/summoner/euw/34061544/Jolar27")

	#print "", "acesing first"
	#response = urllib2.urlopen("http://www.lolking.net/")
	#print "", "acesing second"

	#response = urllib2.urlopen("http://www.lolking.net/summoner/euw/34061544/Jolar27")


	#req = urllib2.Request("http://www.lolking.net/summoner/euw/34061544/Jolar27", headers={'User-Agent' : "Magic Browser"})
	
	req = urllib2.Request(i, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )

	#full_text = response.read()
	full_text = con.read()

	soup = BeautifulSoup(full_text, 'html.parser')

	#wins_loses = []

	#for j in soup.findAll("div", { "class" : "matches-match" }):
	#for j in soup.findAll("div", { "class" : "matches-row" }):
	for j in soup.findAll("div", { "class" : "summoner-matches panel" }):

		print j





