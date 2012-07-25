# -*- coding: utf8 -*-
import simplejson, urllib
import urllib2

"""
2-07 user's musics tags

format : https://api.pudding.to/v1/users/{user-id}/musics?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
sample : https://api.pudding.to/v1/users/181651/musics?access_key=TEST_ACCESS_KEY&token=TEST_TOKEN
"""

ACCESS_KEY = "96474e57-cb16-11e1-91b7-12313f062e84"
API_BASE = "http://openapi.pudding.to/api/v1/users/"

USER_ID = 77641


def get_user_music_tags(userid, **args):
    """
    get music tags written by user. response format is json
    """
    args.update({
            'access_key': ACCESS_KEY
            })

    url = API_BASE + str(userid) + "/musics" + '?' + urllib.urlencode(args)

    if('format' in args and args['format'] == 'xml'):
        result = urllib2.urlopen(url).read()
    else:
        result = simplejson.load(urllib.urlopen(url))

    return result


if __name__ == "__main__" :
    
    json = get_user_music_tags(USER_ID)
    print json

    xml = get_user_music_tags(USER_ID, format='xml')
    print xml
