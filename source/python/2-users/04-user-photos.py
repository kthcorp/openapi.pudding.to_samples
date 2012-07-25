# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-04 get user's photos

format : https://api.pudding.to/v1/users/{user-id}/photos?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/users/181651/photos?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/users/"

USER_ID = 181651


def get_user_photos(userid, **args):
    """
    get user's photos
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + str(userid) + "/photos" + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    json = get_user_photos(USER_ID)
    print json

    xml = get_user_photos(USER_ID, format='xml')
    print xml
