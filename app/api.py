import urllib, urllib2, json

def pcr (middle=''):
  path=''.join(('http://pennapps.com/courses-ceasarb/',middle,'?token=pcr_e4a04ecd6aaadc2fe927e00205d9b039'))
  response = urllib2.build_opener().open(path)
  page = response.read()
  data = json.loads(page)
  return data['result']


