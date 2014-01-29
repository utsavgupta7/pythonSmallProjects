import cgi, cgitb 
import urllib
from urllib import urlopen
import urllib2
url_list=[]
index={}

def record_user_click(index,keyword,url):
    urls=lookup(index,keyword)
    if urls:
        for entry in urls:
            if(entry[0]==url):
                entry[1]+=1

def add_to_index_count(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            ##if url not in entry[1]:
            entry[1].append([url,0])
            return
    index.append([keyword,[[url,0]]])

def split_string(source,splitlist):
    i=0
    j=0
    return_list=[]
    while i<len(source):
        if source[i] in splitlist:
            if(source[j:i] not in splitlist):
                return_list.append(source[j:i])
            j=i+1
            
        if i==len(source)-1 and j!=len(source):
            return_list.append(source[j:])
        i+=1
    
    return return_list

def get_page(pagesource):
    try:
        return urlopen(pagesource).read()
    except:
        return ""

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return 'Not Found'
	
def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]

def add_page_to_index(index,url,content):
    str=content.split()
    for word in str:
        add_to_index(index,word,url)
        ##add_to_index(index,word,url)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link==-1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    
    while True:
        url,endpos=get_next_target(page)
        if url:
            url_list.append(url)
            page=page[endpos:]
        else:
            break
    return url_list


def crawler(seed):
    to_crawl=[seed]
    crawled=[]
    count=0
    while to_crawl and count<10:
        page=to_crawl.pop()
        print page
        count=count+1
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            to_crawl=to_crawl+get_all_links(content)
            crawled.append(page)
    return index        
            
crawler("http://www.vnit.ac.in")
print lookup(index,'filmleri')










