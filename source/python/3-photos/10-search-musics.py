# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-10 search music tags 

format : https://api.pudding.to/v1/photos/musics/search?query=key&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/musics/search?query=lov&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/photos/musics/search"


def search_photos_by_music(music, **args):
    """
    Get photos by tag 
    """
    args.update({
            'access_key': ACCESS_KEY,
            'query': music
            })

    url = API_BASE + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    music = 'ABBA'

    json = search_photos_by_music(music)
    print json

    xml = search_photos_by_music(music, format='xml')
    print xml
