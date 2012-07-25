# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
16 get emotion infomation 

format : https://api.pudding.to/v1/emotions/ko?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/emotions/ko?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/emotions/"


def get_emotions(lang_id, **args):
    """
    Get emotions 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + lang_id + "?" + urllib.urlencode(args)

    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    langid = "en" # ko, en, ja

    json = get_emotions(langid)
    print json

    xml = get_emotions(langid, format='xml')
    print xml
