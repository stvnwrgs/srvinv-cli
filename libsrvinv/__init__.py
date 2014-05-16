'''
libsrvinv - the main library serving default methods for srvinv clients
'''

import config
import requests
import json

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
  print resource

def register(resource, resourceid):
  print resource

def delete(resource, resourceid):
  print resource

def search(resource, attribute, value):
  print resource
