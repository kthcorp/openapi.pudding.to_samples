# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/popular"


def get_photo_popular_json(**args):
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_photo_popular_xml(**args):
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_photo_popular_json()
    print json

    xml = get_photo_popular_xml()
    print xml