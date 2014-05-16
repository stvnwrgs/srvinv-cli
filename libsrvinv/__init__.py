'''
libsrvinv - the main library serving default methods for srvinv clients
'''

import config
import requests
import json
from datetime import datetime

api_url = config.master_url + config.api_version + '/'

def get(resource, resourceid, attribute):
  apirequest = requests.get(api_url + resource + 's/' + resourceid)
  if apirequest.status_code == 200:
    if not attribute:
      print apirequest.text
    else:
      resource_as_obj = json.loads(apirequest.text)
      print resource_as_obj[attribute]
  elif apirequest.status_code == 404:
    print 'resource not found'
  elif apirequest.status_code == 500:
    print 'error communicating with srvinv daemon'

def set(resource, resourceid, attribute, value):
  apirequest = requests.get(api_url + resource + 's/' + resourceid)
  if apirequest.status_code == 200:
      resource_as_obj = json.loads(apirequest.text)
      resource_as_obj[attribute] = value
      to_set_resource = json.dumps(resource_as_obj)
      apirequest = requests.put(api_url + resource + 's/' + resourceid, data=to_set_resource)
      if apirequest.status_code == 202:
        print to_set_resource
      else:
        print 'error communicating with srvinv daemon'
  elif apirequest.status_code == 404:
    print 'resource not found'
  elif apirequest.status_code == 500:
    print 'error communicating with srvinv daemon'

def register(resource, resourceid):
  to_register_resource = {"name": resourceid, "created_at": unicode(datetime.utcnow())}
  to_register_resource = json.dumps(to_register_resource)
  apirequest = requests.post(api_url + resource + 's', data=to_register_resource)
  if apirequest.status_code == 201:
    print to_register_resource
  elif apirequest.status_code == 409:
    print 'conflict: already registered'
  else:
    print 'error communicating with srvinv daemon'

def delete(resource, resourceid):
  apirequest = requests.delete(api_url + resource + 's/' + resourceid)
  if apirequest.status_code == 202:
    print 'deleted ' + resource + ': ' + resourceid
  else:
    print 'error communicating with srvinv daemon'

def search(resource, attribute, value):
  print resource
