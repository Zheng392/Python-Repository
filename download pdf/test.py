import requests
from lxml import etree
import os
import re
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
import time

def get_html(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    r=requests.get(url,headers=headers)
    # print(r.text)
    html=etree.HTML(r.text)
    result=html.xpath('//*[@id="article-list"]/form/div[3]/ol/li/dl/dd[4]/a/@href')
    if result==[]:
        result = html.xpath('//*[@id="article-list"]/form/div[3]/ol//ol/li/dl/dd[4]/a/@href')
    return result

def save_pdf(url,folder,name):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    if os.path.exists(folder+'/'+name+'.pdf'):
        return

    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(url)
    # time.sleep(1)
    url=browser.current_url
    browser.close()

    r = requests.get(url, headers=headers)
    if not os.path.exists(folder):
        os.makedirs(folder)


    with open(folder+'/'+name+'.pdf','wb') as f:
        f.write(r.content)

'''test download pdf
url='https://ac.els-cdn.com/S0306457315000242/1-s2.0-S0306457315000242-main.pdf?_tid=44624573-386b-4ebf-921c-825259bf4488&acdnat=1545467755_f582eab50ca643aeeb8c4ecf4756a951'
save_pdf(url,'test','aaa')

'''

'''test selenium



browser= webdriver.Chrome()
url='https://www.sciencedirect.com/science/article/pii/S0306457315000242/pdfft?md5=abece181b57cc15e01f82237124b92d9&pid=1-s2.0-S0306457315000242-main.pdf'
browser.get(url)
print(browser.current_url)
browser.close()
pass


'''



if __name__=='__main__':
    links={}
    # for i in range(4):
    #     for j in range(6):
    #         url = 'https://www.sciencedirect.com/journal/information-processing-and-management/vol/%d/issue/%d'%(51+i,j+1)
    #         links['vol%dissue%d'%(51+i,j+1)]=get_html(url)
    #         print('get links of vol%d issue%d '%(51+i,j+1))


    # with open('data2.json','w') as file:
    #     file.write(json.dumps(links))
    with open('data2.json','r') as file:
        links=json.loads(file.read())



    for i in range(4):
        for j in range(6):
            part=links['vol%dissue%d'%(51+i,j+1)]
            for l,u in enumerate(part):
                url='https://www.sciencedirect.com'+u
                save_pdf(url, 'vol%d/issue%d'%(51+i,j+1),str(l))
                print('save pdf of vol%d issue%d %d'%(51+i,j+1,l))