# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-02 get popular photos 

format : https://api.pudding.to/v1/photos/popular?appToen=APP_TOKEN
sample : https://api.pudding.to/v1/photos/popular?appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/popular"


def get_popular_photos_json(**args):
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_popular_photos_xml(**args):
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_popular_photos_json()
    print json

    xml = get_popular_photos_xml()
    print xml