import urllib2
import json
import logging

log = logging.getLogger(__name__)

BASE_URL = "http://hackers-api.goshippo.com/v1/tracking_numbers/"


try:
    request = urllib2.Request(BASE_URL)
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        data = json.loads(content)
except urllib2.HTTPError, e:
    log.error('Error while getting tracking numbers: %s' %e)
