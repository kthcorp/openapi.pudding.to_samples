# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-05 user duplicated check

format : https://api.pudding.to/v1/users/duplicate?email={emailaddress}&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/users/duplicate?email=km9ace%40gmail.com&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/users/duplicate"

USER_EMAIL_EXIST = "km9ace@gmail.com"
USER_EMAIL_NONEXIST = "unknown@example.com"

NICKNAME = 'debop'


def get_user_duplicate(**args):

    args.update({
            'access_key': ACCESS_KEY,
            })

    url = API_BASE + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result



if __name__ == "__main__" :
    
    json = get_user_duplicate(email=USER_EMAIL_EXIST)
    print json
    
    json = get_user_duplicate(email=USER_EMAIL_NONEXIST)
    print json
    
    json = get_user_duplicate(nickname=NICKNAME)
    print json

    xml = get_user_duplicate(email=USER_EMAIL_EXIST, format='xml')
    print xml
    
    xml = get_user_duplicate(email=USER_EMAIL_NONEXIST, format='xml')
    print xml
