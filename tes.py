#coding: UTF-8
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

def cinii_search(query):
    keyword=unicode(query,"utf-8")
    encoding='utf-8'
    search_result_list=[]
    search_keyword={'q':keyword.encode(encoding),'count':20}
    CINII="http://ci.nii.ac.jp/books/opensearch/search?"
    cinii_search=CINII+urllib.urlencode(search_keyword)
    try :
        res=urllib.urlopen(cinii_search)
        soup=BeautifulSoup(res)
        for tr in soup.findAll('link'):
            if dict(tr.attrs)['href'].find("rdf")!=-1:
               search_result_list.append(dict(tr.attrs)['href'])
    except  urllib2.URLError,e:
        print e.reason
    return search_result_list
        
cinii_result=u"http://ci.nii.ac.jp/ncid/BB02642167.rdf"
rdf=urllib.urlopen(cinii_result)
soup_r=BeautifulSoup(rdf)
print soup_r
