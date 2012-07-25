# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-12 get photos by emotion 

format : https://api.pudding.to/v1/photos/by_emotion/{emotion-id}?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/by_emotion/1?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/photos/by_emotion/"


def get_photos_by_emotion(emotion_id, **args):
    """
    Get photos by emotion id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + str(emotion_id) + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    emotion_id = 4

    json = get_photos_by_emotion(emotion_id)
    print json

    xml = get_photos_by_emotion(emotion_id, format='xml')
    print xml
