from django.shortcuts import render


from urllib.request import urlopen
import urllib3

import requests as req


import tldextract




def getStatus(link):
    http = urllib3.PoolManager()
    r = http.request('GET', link)
    status=r.status
    return status



def getDomain(link):
    list = tldextract.extract(link)
    domain_name = list.domain + '.' + list.suffix
    print(domain_name)
    return domain_name



def getinfo(link):
    response=[]
    html = urlopen(link)
    data=html.info()
    

   
    return dict(data)
    
        
    
def get301withUrl(url):
    resp = req.get(url)
    print(resp.history)
    print(resp.url)
    return resp.history,resp.url
    
    
    
   

def HomePageView(request):

    if(request.method=="POST"):
        info=[]
        mainUrl=""
        urls=[]
        isRedirection=False
        Url=request.POST.get('url')
        Url=getDomain(Url)
        url1="https://"+Url
        url2="http://"+Url
        url3="https://www."+Url
        url4="http://www."+Url
        urls.append(url1)
        urls.append(url2)
        urls.append(url3)
        urls.append(url4)
        print(urls)
        header_info=getinfo(url4)
        status=[]
        status.append(getStatus(url4))
       
        
        context={}
      
        redirect,redirectionURL=get301withUrl(url2)
        
        
        if(len(redirect)>0):
            context['numberOfredirect']=len(redirect)
            isRedirection=True

            context['redirectionURL']=redirectionURL
            
        if(isRedirection):
            for i in range (context['numberOfredirect']):
                status.append(301)
        

        mainUrl="http://"+Url 
        
      
       
        



        

        
        context['header_info']=header_info
        context['status_code']=status
        
        context['mainUrl']=mainUrl
        context['isRedirect']=isRedirection
        
        # print(context)
        return render(request,'index.html',context)
    

    return render(request,"index.html",{})