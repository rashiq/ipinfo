#!/usr/bin/env python

import sys
import requests

tor_url = 'http://istorexitnode.setgetgo.com/get.php?ip={ip}'
info_url = 'http://ip-api.com/json/{ip}'

def main(ip):
  if not ip: return None
  spam = check_spam(ip)
  if spam: return 'Spam'
  info = get_info(ip)
  if info: return '\n'.join(list(info))
  return 'Failed'


def check_spam(ip):
  tor = requests.get(tor_url.format(ip=ip))
  if tor.status_code == 200:
    return (True in tor.json().values())
  return False


def get_info(ip):
  info = requests.get(info_url.format(ip=ip)).json()
  if not info: return None

  city = info.get('city')
  country = info.get('country')
  org = info.get('org')
  items = (city, country, org)
  if any(i == None for i in items): return None
  return items


if __name__ == '__main__':
  if len(sys.argv) == 1:
    print('You need to provide me with an ip, mate.')
  else:
    print(main(sys.argv[1]))


