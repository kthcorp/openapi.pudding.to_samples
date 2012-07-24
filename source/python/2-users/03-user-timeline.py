# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-03 get user timeline

format : https://api.pudding.to/v1/users/{user-id}/timeline?appToen=APP_TOKEN
sample : https://api.pudding.to/v1/users/181651/timeline?appToken=APP_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/users/"

USER_ID = 181651


def get_user_timeline_json(userid, **args):
    """
    get user's timeline
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/timeline.json" + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_user_timeline_xml(userid, **args):
    """
    get user's timeline
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = SEARCH_BASE + str(userid) + "/timeline.xml" + '?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_user_timeline_json(USER_ID)
    print json

    xml = get_user_timeline_xml(USER_ID)
    print xml