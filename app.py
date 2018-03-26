#!/usr/bin/env python

import os
import sys
import json
import requests


def main(endpoint, args):
    if args[0].startswith('--'):
        query = dict(zip(map(lambda a: a[2:], args[::2]), args[1::2]))
    else:
        query = {
            'domain': args[0]
        }

    res = requests.post(
        'https://api.fullcontact.com/v3/%s.enrich' % endpoint,
        data=json.dumps(query),
        headers={
            'Authorization': 'Bearer %s' % os.getenv('API_KEY'),
            'User-Agent': os.getenv('USER_AGENT')
        }
    )

    try:
        res.raise_for_status()
    except:
        sys.stderr.write(res.text)
        raise
    else:
        return res.text


if __name__ == '__main__':
    sys.stdout.write(main(sys.argv[1], sys.argv[2:]))
