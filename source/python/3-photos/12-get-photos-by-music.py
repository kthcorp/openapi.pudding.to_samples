# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
3-12 get photos by music 

format : https://api.pudding.to/v1/photos/by_music?artist={artist}&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/photos/by_music?artist=ABBA&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/photos/by_music"


def get_photos_by_artist(artist=None, title=None, **args):
    """
    Get photos by tag 
    """
    args.update({ 'access_key': ACCESS_KEY })
    
    if(artist != None):
        args.update({'artist':artist})
    if(title != None):
        args.update({'title': title})
    

    url = API_BASE + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    artist = "ABBA"
    title = "Dan"

    json = get_photos_by_artist(artist, title)
    print json

    xml = get_photos_by_artist(artist, title, format='xml')
    print xml
    
    json = get_photos_by_artist(artist)
    print json
