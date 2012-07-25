# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-02 get popular photos 

format : https://api.pudding.to/v1/photos/popular?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/popular?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/photos/popular"


def get_popular_photos(**args):
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    json = get_popular_photos()
    print json

    xml = get_popular_photos(format='xml')
    print xml
