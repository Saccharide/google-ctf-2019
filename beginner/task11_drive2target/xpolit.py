#!/bin/python

#import urllib
#import urllib2
import requests
import re

url = 'https://drivetothetarget.web.ctfcompetition.com/'
normal_resp = requests.get(url).text


def get_response(text):

    return re.match(r"<p>.*</p>",text)[0]
def extract_value(string, keyword):
    keyword+='" value="'
    substr = string.find(keyword)
    total = substr+len(keyword)
    temp = string[total::]
    end = temp.find('"')
    return string[total:end+total]

def drive(original_resp):
    lat = extract_value(original_resp, 'lat')
    lon = extract_value(original_resp, 'lon')
    token = extract_value(original_resp, 'token')
    data = {
        'lat'   : lat,
        'lon'   : lon,
        'token' : token 
    }

    resp = requests.get(url, params=data).text
    print(get_response(resp))
    return lat, lon, token, resp

def load_prev(lat,lon,token):
    data = {
        'lat'   : lat,
        'lon'   : lon,
        'token' : token 
    }

    resp = requests.get(url, params=data).text
    print(get_response(resp))
    return lat, lon, token, resp

step = 0.0001
direction = [
    [1,0],
    [-1,0],
    [0,1],
    [0,-1]
]
x = 0 
while x == 0:
    lat, lon, token, resp = drive(normal_resp)
    if 'too fast' in resp:
        step = 0.0001

    elif 'getting closer' in resp:
        step += 0.0001

    elif 'getting away' in resp:
        step += 0.0001
    x+=1
