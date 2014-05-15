#!/usr/bin/env python
'''
srvsearch - a tool to search the srvinv

usage examples:
---------------
srvsearch srv deployed_with "docker": returns a json array of srvids that are deployed with docker
'''

import argparse
#import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("resource",
      help="resources to be used: env, net, srv",
      type=str
    )
    parser.add_argument("attribute",
      help="the attribute to be searched",
      type=str
    )
    parser.add_argument("value",
      help="the value to be searched for",
      type=str
    )

    args = parser.parse_args()

    #if not args.dry_run:
    #    mkdir_p(dst)
