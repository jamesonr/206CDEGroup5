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
"https://euw.op.gg/summoner/userName=jolar27"
]

data = []

lista_partidas = []
lista_fechas   = []


for i in list_of_urls:

	print "scrapping this ...", i, 

	req = urllib2.Request(i, headers={'User-Agent' : "Magic Browser"}) 
	con = urllib2.urlopen( req )

	full_text = con.read()

	soup = BeautifulSoup(full_text, 'html.parser')

	print "\n" * 3
	for match in ( soup.findAll("div", { "class" :["GameItemWrap"] }) ):

		#print match.getText().replace("\n"," ").replace(" ","")
		print ("".join((match.getText()).split()))[0:90]

	#match_info = j.getText().replace("\n\n\n\n\n"," ").replace("\n\n"," ").replace("\n"," ")
	#lista_elements = str_list = filter(None, match_info.split(" "))
	#lista_partidas.append([lista_elements[0]])

	#print len(full_text)
	#a = open("a.html","w")
	#a.write(full_text)
	#a.close()
