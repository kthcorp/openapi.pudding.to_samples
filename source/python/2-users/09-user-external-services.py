# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-09 Get user's external service information

format : https://api.pudding.to/v1/users/{user-id}/locations?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/users/77641/locations?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/users/"

USER_ID = 77641


def get_user_external_services(userid, **args):
    """
   Get user's external service information. Response format is json
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + str(userid) + "/external_services" + '?' + urllib.urlencode(args)

    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    json = get_user_external_services(USER_ID)
    print json

    xml = get_user_external_services(USER_ID, format='xml')
    print xml
