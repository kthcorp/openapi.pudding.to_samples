# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/photos/"


def get_photo_detailed_json(photoid, **args):
    """
    Get photo information by photo id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(photoid) + "/detailed" + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_photo_detailed_xml(photoid, **args):
    """
    Get photo information by photo id 
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(photoid) + "/detailed.xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    photoid = 454345

    #json = get_photo_detailed_json(photoid)
    #print json

    xml = get_photo_detailed_xml(photoid)
    print xml