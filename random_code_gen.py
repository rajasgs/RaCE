#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://www.programcreek.com/python/index/module/?action=index&page=37

    https://www.programcreek.com/python/example/123648/optimization.create_optimizer

    https://www.programcreek.com/python/index/module/?action=index&page=60
'''

# Import necessary modules
from bs4 import BeautifulSoup
import urllib
import random

PYTHON_PAGES_COUNT = 60

def get_soup_base(address):

    print(f"[get_soup_base] : {address}")

    getRequest  = urllib.request.Request(address, None, {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
    urlfile     = urllib.request.urlopen(getRequest)
    htmlResult  = urlfile.read(50000)

    urlfile.close()

    soup = BeautifulSoup(htmlResult, features="html.parser")

    return soup

def get_random_codelink(soup):

    li_list = soup.select('ul#api-list li')

    if(len(li_list) ==0 ):
        return None

    random_li = random.choice(li_list)
    a_link = random_li.select_one('div#api-list-apiname a')
    # print(a_link['href'])

    return a_link['href']

def get_info():

    # random_page = random.randint(0, PYTHON_PAGES_COUNT)
    random_page = 60

    address     = f"https://www.programcreek.com/python/index/module/?action=index&page={random_page}"

    soup = get_soup_base(address)
    link = get_random_codelink(soup)

    if(not link):
        print('No links found')
        return

    soup1 = get_soup_base(link)
    link1 = get_random_codelink(soup1)
    if(not link1):
        print('No links found')
        return

    # print(link1)

    soup2 = get_soup_base(link1)
    box_list = soup2.select('div#main div.examplebox')

    random_box = random.choice(box_list)
    _code = random_box.select_one('div.exampleboxbody').text

    print(_code)

def startpy():
    print('Hey there')

    get_info()

if __name__ == '__main__':
    startpy()