# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/users/"


def get_user_musics_json(userid, **args):
    """
    get musics written by user response format is json
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/musics" + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_user_musics_xml(userid, **args):
    """
    get musics written by user response format is xml
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/musics.xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    userid = 77641

    json = get_user_musics_json(userid)
    print json

    xml = get_user_musics_xml(userid)
    print xml