# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
16 get emotion infomation 

format : https://api.pudding.to/v1/emotions/ko?appToen=APP_TOKEN
sample : https://api.pudding.to/v1/emotions/ko?appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE = "http://openapi.pudding.to/api/v1/emotions"


def get_emotions_json(langid, **args):
    """
    Get emotions 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + "/" + langid + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_emotions_xml(langid, **args):
    """
    Get emotions 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + "/" + langid + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    langid = "ko" # ko, en, ja

    json = get_emotions_json(langid)
    print json

    xml = get_emotions_xml(langid)
    print xml
