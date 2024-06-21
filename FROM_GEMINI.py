import pycurl
import certifi
from io import BytesIO

buffer = BytesIO()
pyc = pycurl.Curl()
pyc.setopt(c.URL, 'http://pycurl.io/')
pyc.setopt(c.WRITEDATA, buffer)
pyc.setopt(c.CAINFO, certifi.where())
pyc.perform()
pyc.close()
