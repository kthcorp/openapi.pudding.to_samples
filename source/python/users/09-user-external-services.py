# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
5.2.3 user's musics tags

format : https://api.pudding.to/v1/users/{user-id}/locations?appToen=APP_TOKEN
sample : https://api.pudding.to/v1/users/77641/locations?appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/users/"

USER_ID = 77641


def get_user_locations_json(userid, **args):
    """
    get locations written by user response format is json
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/locations" + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_user_locations_xml(userid, **args):
    """
    get locations written by user response format is xml
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/locations.xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_user_locations_json(USER_ID)
    print json

    xml = get_user_locations_xml(USER_ID)
    print xml