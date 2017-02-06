# 
# class that contains the rest of the divs
# panel-body match
# 
# apt-get update
# pip install beautifulsoup4
#


from bs4 import BeautifulSoup
import urllib
import urllib2

list_of_urls = [
"http://www.lolking.net/summoner/euw/34061544/Jolar27"
]

for i in list_of_urls:

	print "scrapping this ...", i

	req = urllib2.Request(i, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )

	full_text = con.read()

	soup = BeautifulSoup(full_text, 'html.parser')

	for j in soup.findAll("div", { "class" : "summoner-matches panel" }):

		for k in j:

			print k.findAll("div", {"":""})





