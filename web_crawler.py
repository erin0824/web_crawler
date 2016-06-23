import requests
from lxml import html

visited = [] #list of visited urls
to_visit = [] #list of urls to visit 
images = [] #url to images within url

def scrape_link(url):
    link = requests.get(url)
    text =  html.fromstring(link.content)
    
    #scrape all links on page
    for sites in text.xpath('//a/@href'):
        if sites == '#header' or sites == '#footer':
            continue
        #add url to list of websites to visit if not in either list
        if url in sites and sites not in visited and sites not in to_visit:
            to_visit.append(str(sites))
    visited.append(url) #add currently visiting url to the already visited list
        
    #scrape all links of images
    for pic in text.xpath('//img/@src'):
        if pic not in images:
            images.append(pic)
    
    if not to_visit:
        return False
    else:
        return True
            
def main():
    url = 'http://thought.so'
    scrape_link(url)
    
    #scrape all websites on the to-visit list until empty
    while scrape_link(url):
        for v in to_visit:
            scrape_link(v)
            #remove scraped url from to_visit list 
            to_visit.remove(v)
    
    print visited #print url of all visited sites
    print images #print src url of all images
            
if __name__ == '__main__':
    main()


