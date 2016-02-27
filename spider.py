#!/usr/bin/python
#coding: utf-8

import urllib2  # functions and classes which help in opening URLs
import bs4      # extract data from HTML or XML files
import chardet  # detect encoding character of HTML file
import re
import urlparse

class FontFamilySpider:
    def __init__(self):
        self.__headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36')
    
    def open_url(self, url):
        try:
           opener = urllib2.build_opener()           
           opener.addheaders = [self.__headers]      
           content = opener.open(url).read()        
           encoding = chardet.detect(content)['encoding']
           content = content.decode(encoding, 'ignore')
        except Exception, e:
            content = ''
        else:
            pass
        finally:
            pass
        return content

    def getFontFamily(self, content):
        m = re.findall(r"font-family:\s*[^;]*;", content)
        return m

    def getCssFile(self, content):
        cssList = []
        #匹配所有带.css后缀的文件
        m = re.findall(r"""<link\s+.*href=("|')([^\s]*\.css[^\s]*)("|').*>""", content)
        #m = re.findall(r"""<link\s+.*href=("|')([^\s]*.css[^\s].*)("|').*>""", content)
        #m = re.findall(r"""<link\s+.*href=("|')([^>].*)("|').*>""", content)
        for x in m:
            cssList.append(x)
        return cssList

    def getCssFileHref(self, link, url):
        parsedTuple = urlparse.urlparse(link)
        if (len(parsedTuple[1]) ==0):
            host = self.getHost(url)
            link = host + '/' + link
        return link

    def getHost(self, url):
        parsedTuple = urlparse.urlparse(url)
        #print parsedTuple[0]+'://'+parsedTuple[1] + '/'
        return parsedTuple[0]+'://'+parsedTuple[1] + '/'
        


    def get_demo(self, content):
        soup = bs4.BeautifulSoup(content)
        div = soup.find('div', id='nowplaying')               # return the first "div" tag
        demo_list = div.findAll('li', class_="list-item")  # return the list of "li" tag under "div"
        return demo_list
