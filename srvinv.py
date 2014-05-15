#!/usr/bin/env python
'''
srvinv - a server inventory

usage examples:
---------------
srvinv get srv srvid --attribute interfaces: returns a srvid's interfaces formatted as json
srvinv set srv srvid --attribute is_provisioned --value "true": sets is_provisioned to true on a srvid
srvinv register srv srvid: will register a new srvid in inventory
srvinv delete srv srvid: will remove a srvid from inventory
'''

import argparse
#import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("verb",
      help="verbs to be used: get, set, register, delete",
      type=str
    )
    parser.add_argument("resource",
      help="resources to be used: env, net, srv",
      type=str
    )
    parser.add_argument("resourceid",
      help="the resource id",
      type=str
    )
    parser.add_argument("--attribute",
      help="the attribute to be accessed",
      type=str
    )
    parser.add_argument("--value",
      help="the value to be setted in an attribute",
      type=str
    )

    args = parser.parse_args()

    #if not args.dry_run:
    #    mkdir_p(dst)

    if args.verb == 'get':
      print args.verb
      # srvinv.get(resource, resourceid)
      if not args.attribute == None:
        # srvinv.get(resource, resourceid, attribute)
        print args.attribute

    elif args.verb == 'set':
      print args.verb
      if args.attribute == None:
        print 'missing attribute'
      else:
        print args.attribute
        if args.value == None:
          print 'missing value'
        else:
          print args.value
          # srvinv.set(resource, resourceid, attribute, value)

    elif args.verb == 'register':
      print args.verb
      # srvinv.reg(resource, resourceid)

    elif args.verb == 'delete':
      print args.verb
      # srvinv.reg(resource, resourceid)
