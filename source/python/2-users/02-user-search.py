# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-02 search user

format : https://api.pudding.to/v1/users/search?user_id={user-id}&appToen=APP_TOKEN
sample : https://api.pudding.to/v1/users/search?user_id=181651&appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE = "http://openapi.pudding.to/api/v1/users/search"
USER_ID = 181651


def get_user_search_json(userid, **args):
    """
    get user information by userid, response format is json
    """
    args.update({
            'appToken': ACCESS_KEY,
            'user_id' : str(userid)
            })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_user_search_xml(userid, **args):
    """
    get user information by userid, response format is xml
    """
    args.update({
            'appToken': ACCESS_KEY,
            'user_id' : str(userid)
            })

    url = SEARCH_BASE + ".xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_user_search_json(USER_ID)
    print json

    xml = get_user_search_xml(USER_ID)
    print xml