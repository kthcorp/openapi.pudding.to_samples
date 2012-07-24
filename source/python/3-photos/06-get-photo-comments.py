# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-06 get photo's comments 

format : https://api.pudding.to/v1/photos/{photo-id}/comments?appToen=APP_TOKEN
sample : https://api.pudding.to/v1/photos/3635879/comments?appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/"

PHOTO_ID = 3635879


def get_photo_comments_json(photoid, **args):
    """
    Get photo comments by photo id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(photoid) + "comments.json" + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_photo_comments_xml(photoid, **args):
    """
    Get photo comments by photo id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(photoid) + "comments.xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_photo_comments_json(PHOTO_ID)
    print json

    xml = get_photo_comments_xml(PHOTO_ID)
    print xml