# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-10 search music tags 

format : https://api.pudding.to/v1/photos/musics/search?query=key&appToen=APP_TOKEN
sample : https://api.pudding.to/v1/photos/musics/search?query=lov&appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/musics/search"


def search_photos_by_music_json(music, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY,
            'query': music
            })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def search_photos_by_music_xml(tag, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY,
            'query': music
            })

    url = SEARCH_BASE + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    music = "ABBA"

    json = search_photos_by_music_json(music)
    print json

    xml = search_photos_by_music_xml(music)
    print xml