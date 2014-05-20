'''
libsrvinv - the main library serving default methods for srvinv clients
'''

import config
import helpers
import requests
import json
import os
import fnmatch
import time
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
    exit(1)
  elif apirequest.status_code == 500:
    print 'error communicating with srvinv daemon'
    exit(1)

def set(resource, resourceid, attribute, value):
  apirequest = requests.get(api_url + resource + 's/' + resourceid)
  if apirequest.status_code == 200:
      # validate if value is json so we dont put it in there as string
      if helpers.is_json(value):
        value = json.loads(value)
      to_set_value = json.dumps({"value": value})
      apirequest = requests.patch(api_url + resource + 's/' + resourceid + '/' + attribute, data=to_set_value)
      if apirequest.status_code == 202:
        print to_set_value
      else:
        print 'error communicating with srvinv daemon'
        exit(1)
  elif apirequest.status_code == 404:
    print 'resource not found'
    exit(1)
  elif apirequest.status_code == 500:
    print 'error communicating with srvinv daemon'
    exit(1)

def register(resource, resourceid):
  to_register_resource = {"name": resourceid, "created_at": unicode(datetime.utcnow()), "updated_at": unicode(datetime.utcnow())}
  to_register_resource = json.dumps(to_register_resource)
  apirequest = requests.post(api_url + resource + 's', data=to_register_resource)
  if apirequest.status_code == 201:
    print to_register_resource
  elif apirequest.status_code == 409:
    print 'conflict: already registered'
    exit(1)
  else:
    print 'error communicating with srvinv daemon'
    exit(1)

def delete(resource, resourceid):
  apirequest = requests.delete(api_url + resource + 's/' + resourceid)
  if apirequest.status_code == 202:
    print 'deleted ' + resource + ': ' + resourceid
  else:
    print 'error communicating with srvinv daemon'
    exit(1)

def search(resource, attribute, value):
  found_resources = []
  cache_file_path = config.cache_path + resource + '.json'

  if (os.path.isfile(cache_file_path)) and (os.path.getmtime(cache_file_path) > (time.time() - config.cache_duration_in_s)):
    cache_file = open(cache_file_path, 'r')
    cache = cache_file.read()
    cache_file.close
  else:
    apirequest = requests.get(api_url + resource + 's')
    if apirequest.status_code == 200:
      cache = apirequest.text
      cache_file = open(cache_file_path, 'w')
      cache_file.write(cache)
      cache_file.close
    else:
      print 'error communicating with srvinv daemon'
      exit(1)

  cache_as_obj = json.loads(cache)
  for resource_to_search in cache_as_obj:
    # we need to make sure to convert arrays to strings so we can fnmatch them
    if isinstance(resource_to_search[attribute], list):
       attribute_to_search = json.dumps(resource_to_search[attribute])
    else:
       attribute_to_search = resource_to_search[attribute]
    if fnmatch.fnmatch(attribute_to_search, value):
      found_resources.append(resource_to_search)

  print json.dumps(found_resources)
