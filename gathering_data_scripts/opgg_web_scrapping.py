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
		match_data = ("".join((match.getText()).split()))

		print match_data

		#match_data[0:90]
