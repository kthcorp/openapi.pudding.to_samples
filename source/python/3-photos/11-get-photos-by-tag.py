# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-11 get photos by tag 

format : https://api.pudding.to/v1/photos/by_tag/{tag}&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/by_tag/dog&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/photos"


def get_photos_by_tag(tag, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + "/by_tag/" + str(tag) + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    tag = "dog"

    json = get_photos_by_tag(tag)
    print json

    xml = get_photos_by_tag(tag, format='xml')
    print xml
