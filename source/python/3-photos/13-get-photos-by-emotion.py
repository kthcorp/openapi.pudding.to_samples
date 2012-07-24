# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE = "http://openapi.pudding.to/api/v1/photos/"


def get_photos_by_emotion_json(emotionid, **args):
    """
    Get photos by emotion id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + "by_emotion/" + str(emotionid) + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_photos_by_emotion_xml(emotionid, **args):
    """
    Get photos by emotion id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + "by_emotion/" + str(emotionid) + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    emotionid = 4

    json = get_photos_by_emotion_json(emotionid)
    print json

    xml = get_photos_by_emotion_xml(emotionid)
    print xml
