# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-09 search tags 

format : https://api.pudding.to/v1/photos/tags/search?query=key&appToen=APP_TOKEN
sample : https://api.pudding.to/v1/photos/tags/search?query=lov&appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/tags/search"


def get_photos_by_tag_json(tag, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY,
            'query': tag
            })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_photos_by_tag_xml(tag, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY,
            'query': tag
            })

    url = SEARCH_BASE + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    tag = "lov"

    json = get_photos_by_tag_json(tag)
    print json

    xml = get_photos_by_tag_xml(tag)
    print xml