# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
5.2.5 user duplicated check

format : https://api.pudding.to/v1/users/duplicate?appToen=APP_TOKEN&email={emailaddress}
sample : https://api.pudding.to/v1/users/duplicate?appToken=APP_TOKEN&email=km9ace%40gmail.com
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
SEARCH_BASE ="http://openapi.pudding.to/api/v1/users/duplicate"

USER_EMAIL_EXIST= "km9ace@gmail.com"
USER_EMAIL_NONEXIST = "unknown@example.com"


def get_user_duplicate_json(email, **args):

    args.update({
            'access_key': ACCESS_KEY,
            'email' : email
            })

    url = SEARCH_BASE +  '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))

    return result

def get_user_duplicate_xml(email, **args):

    args.update({
            'access_key': ACCESS_KEY,
            'email' : email
            })

    url = SEARCH_BASE +  '.xml?' + urllib.urlencode(args)
    result = urllib2.urlopen(url).read()

    return result


if __name__ == "__main__" :
    
    json = get_user_duplicate_json(USER_EMAIL_EXIST)
    print json
    
    json = get_user_duplicate_json(USER_EMAIL_NONEXIST)
    print json

    xml = get_user_duplicate_xml(USER_EMAIL_EXIST)
    print xml
    
    xml = get_user_duplicate_xml(USER_EMAIL_NONEXIST)
    print xml