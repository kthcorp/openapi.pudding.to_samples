# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-01 get photo 

format : https://api.pudding.to/v1/photos/{photo-id}?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/3635879?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE = "http://openapi.pudding.to/api/v1/photos/"

PHOTO_ID = 3635879


def get_photo(photo_id, **args):
    """
    Get photo information by photo id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(photo_id) + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :

    json = get_photo(PHOTO_ID)
    print json

    xml = get_photo(PHOTO_ID, format='xml')
    print xml
