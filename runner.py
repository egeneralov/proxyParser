import os
import json


types = 'SOCKS5'

try:
  limit = os.environ['LIMIT']
except KeyError:
  limit = 100

try:
  threads = os.environ['THREADS']
except KeyError:
  threads = 50

os.system(
  '/usr/local/bin/proxybroker find --types {} --limit {} --format json --outfile test.json'.format(
    types, limit
  )
)

with open('test.json', 'r') as src:
  with open('test.txt', 'w+') as f:
    for item in json.loads(src.read()):
      payload = '{}:{}'.format(item['host'], item['port'])
      f.write(payload + '\n')

os.system(
  '/usr/bin/python2 check_socks5.py -t {} -o 5 test.txt out.txt'.format(
    threads
  )
)

with open('out.txt', 'r') as src:
  data = src.read()

print(data)



