# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
4-05 get banned user list

format : https://api.pudding.to/v1/relations/{user-id}/banned?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/relations/self/banned?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/relations/"

USER_ID = 181651


def get_banned_users(userid, **args):
    """
    get user's follwers
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + str(userid) + "/banned" + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result

if __name__ == "__main__" :
    
    json = get_banned_users(USER_ID)
    print json

    xml = get_banned_users(USER_ID, format="xml")
    print xml
