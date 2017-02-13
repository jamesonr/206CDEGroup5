#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# requests is not a python dfault library, so you need to install it executing the following command :
# pip install requests
#

# example :
# https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=RGAPI-f21db90a-e1e0-45b4-b4fc-ec60cc447bb8
#
#

import requests, json, urllib2

url = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/RiotSchmick?api_key=RGAPI-f21db90a-e1e0-45b4-b4fc-ec60cc447bb8'

print json.load(urllib2.urlopen(url))
