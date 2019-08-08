#!/bin/python

#import urllib
#import urllib2
import requests

url = 'https://drivetothetarget.web.ctfcompetition.com/'
normal_resp = requests.get(url).text


def extract_value(string, keyword):
    keyword+='" value="'
    substr = string.find(keyword)
    total = substr+len(keyword)
    temp = string[total::]
    end = temp.find('"')
    return string[total:end+total]

lat = extract_value(normal_resp, 'lat')
print(lat)
lon = extract_value(normal_resp, 'lon')
print(lon)
token = extract_value(normal_resp, 'token')
print(token)
print("------------------------")
#lat  = normal_resp.find('lat" value="')
#lat +=12 
##print(lat)
#normal_resp = normal_resp[lat::]
##print('After truncating...')
##print('normal_resp = ', normal_resp)
#value = normal_resp.find('"')
##print('value = ', value)
#print(normal_resp[:value])
#lat = normal_resp[:value]
#
#lon = normal_resp.find('lon" value="')
#lon +=12 
#normal_resp = normal_resp[lon::]
#value = normal_resp.find('"')
#print(normal_resp[:value])
#lon = normal_resp[:value]
#
#token = normal_resp.find('token" value="')
#token +=14 
#normal_resp = normal_resp[token::]
#value = normal_resp.find('"')
#print(normal_resp[:value])
#token = normal_resp[:value]
#
#
#print('')
#print('-----------------------------')
#print('BEGIN STEPPING')
#print('-----------------------------')

data = {
    'lat'   : lat,
    'lon'   : lon,
    'token' : token 
}

print(data)
first_resp = requests.get(url, params=data)

print(first_resp.text)
