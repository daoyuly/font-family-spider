#!/usr/bin/python

from spider_2 import FontFamilySpider


def printName(name):
    print '*---------------------------------------------*'
    print '               ' + name + '                  '
    print '                                             '
    print '*----------------------------------------------*'



#url="https://wx.qq.com/"
#url="http://www.difa.me/news/weekly-20161101"
#url="http://iknow.jp/"
#url =  "http://img3.douban.com/f/shire/bdb62d45fb145651da30ac3fec98f21c40cfc962/css/douban.css";
#url="https://www.umu.cn/"
#url="http://news.gxnews.com.cn/staticpages/20160225/newgx56ce4d96-14484600.shtml"
#url="https://app.asana.com/0/60697097430687/91030275767293"
#url = 'http://www.cnblogs.com/huangcong/archive/2011/08/31/2160633.html'
#url = 'http://www.yahoo.co.jp/'
#url='https://www.facebook.com/'
#url='http://www.zeldman.com/2010/07/25/the-puzzle-of-japanese-web-design/'
#url = 'http://www.renren.com/332325542'
#url='http://www.sanga-ryokan.com/blog/?m=201602'

urlList = ["https://wx.qq.com/",
"http://www.difa.me/news/weekly-20161101",
"http://iknow.jp/",
"http://img3.douban.com/f/shire/bdb62d45fb145651da30ac3fec98f21c40cfc962/css/douban.css",
"https://www.umu.cn/",
"http://news.gxnews.com.cn/staticpages/20160225/newgx56ce4d96-14484600.shtml",
"https://app.asana.com/0/60697097430687/91030275767293",
'http://www.cnblogs.com/huangcong/archive/2011/08/31/2160633.html',
'http://www.yahoo.co.jp/',
'https://www.facebook.com/',
'http://www.zeldman.com/2010/07/25/the-puzzle-of-japanese-web-design/',
'http://www.renren.com/332325542',
'http://www.sanga-ryokan.com/blog/?m=201602']

ffspider = FontFamilySpider()

for urlitem in urlList:
    print urlitem
    printName(urlitem)
    url = urlitem
    content = ffspider.open_url(url)
    ff = ffspider.getFontFamily(content)
    for item in ff:
        print item
    m = ffspider.getCssFile(content);
    for x in m:
        href = ffspider.getCssFileHref(x[1],url)
        print href
        css = ffspider.open_url(href)
        ff = ffspider.getFontFamily(css)
        for item in ff:
            print item


