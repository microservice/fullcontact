#!/usr/bin/env python

import os
import sys
import urllib2
import json


def main(email, twitter):
    req = urllib2.Request('https://api.fullcontact.com/v3/person.enrich')
    req.add_header('Authorization', 'Bearer %s' % os.getenv('API_KEY'))
    req.add_header('User-Agent', os.getenv('USER_AGENT'))
    data = json.dumps({
        "email": email
    })
    try:
        response = urllib2.urlopen(req,data)
    except urllib2.HTTPError, e:
        raise
    try:
        twitter = json.loads(response.read())['twitter'].split("/")[3]
    except:
        twitter = None
    return twitter

if __name__ == '__main__':
    print(main(sys.argv[1], sys.argv[2]))
