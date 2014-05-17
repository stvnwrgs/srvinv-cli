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
import libsrvinv

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

    if args.verb == 'get':
      libsrvinv.get(args.resource, args.resourceid, args.attribute)

    elif args.verb == 'set':
      if args.attribute == None:
        print 'missing attribute'
      else:
        if args.value == None:
          print 'missing value'
        else:
          libsrvinv.set(args.resource, args.resourceid, args.attribute, args.value)

    elif args.verb == 'register':
      libsrvinv.register(args.resource, args.resourceid)

    elif args.verb == 'delete':
      libsrvinv.delete(args.resource, args.resourceid)
