#
# class that contains the rest of the divs
# panel-body match
#
# apt-get update
# pip install beautifulsoup4

from bs4 import BeautifulSoup
import urllib
import urllib2

list_of_urls = [
"http://www.lolking.net/summoner/euw/34061544/Jolar27"
]

for i in list_of_urls:
	print "scrapping this ...", i

	#req = urllib2.Request(i, headers={'User-Agent' : "Magic Browser"})
	#con = urllib2.urlopen( req )
	#full_text = con.read()
	full_text = open("a.html","r+").read()


	soup = BeautifulSoup(full_text, 'html.parser')

	for j in soup.findAll("div", { "class" :["matches-match", "matches-match-win", "matches-row"] })[1:6]:
		print j.getText().replace("\n\n\n\n\n"," ").replace("\n\n"," ").replace("\n"," ")

	print "\n" * 3

	print "dates :\n"
	for j in soup.findAll("small", { "class" :["matches-match-time"] })[0:5]:

		stupid = False
		tmp = ""
		final_str = []

		for letra in str(j):
			if letra == '"' and stupid == True: stupid = False; final_str.append(tmp); tmp = ""
			if letra == '"' and stupid == False:stupid = True;

			if stupid == True:
				tmp = tmp + letra

		print "","",final_str[2]
