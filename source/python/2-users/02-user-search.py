# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-02 search user

format : https://api.pudding.to/v1/users/search?nickname={nickname}&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/users/search?nickname=debop&access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/users/search"


def get_user_search(**args):
    """
    get user information by userid, response format is json
    """
    args.update({
            'appToken': ACCESS_KEY,
            })

    url = API_BASE + '?' + urllib.urlencode(args)
    
    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    json = get_user_search(nickname='debop')
    print json

    xml = get_user_search(nickname='debop', format='xml')
    print xml
