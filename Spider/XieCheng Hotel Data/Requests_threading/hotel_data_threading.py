import requests,json,random
import re,threading
import json
from lxml import etree
import time
import random
lock=threading.Lock()

city='shanghai'
unsucesspage=[]
proxies=[]
# user_agent_list = [
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" ,\
#         "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
#         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
#         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
#         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
#         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
#     ]
user_agent_list = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'

    ]

count=0
def header_body_update(page):
    data = {'cityPY': 'shanghai', 'cityId': 2, 'cityCode': '021','page':page}
    headers = {'Referer': 'https://hotels.ctrip.com/hotel/shanghai2/sl1274819', "Host": "hotels.ctrip.com",
               'Origin':'http://hotels.ctrip.com',
               "Accept-Language": "en-US,en;q=0.9",
               "Connection": "keep-alive",
               'Accept': '* / *',
               "Accept-Encoding": "gzip, deflate",
               'Cache-Control':'max-age=0',}
               
    headers['User-Agent'] = random.choice(user_agent_list)
    return headers,data
def proxy_update():
    ip=random.sample(proxies,1)[0].replace('\n','')
    http='http://'+ip
    proxy={'http' : http,
                    'https': http}

    return proxy
def get_page():
    headers, data = header_body_update(1)
    se=[]
    while 1:
        try:
            proxy = proxy_update()
            hotel_list_requests = requests.post('https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx', data=data,
                                        headers=headers,proxies=proxy)#
            hotel_info = eval(hotel_list_requests.text)
            text = hotel_info['paging']
            se = etree.HTML(text)
            page_number=json.loads(se.xpath('//a[@rel="nofollow"]/text()')[0])

            break
        except Exception as e:
            print(e)

   
    return page_number

def fang_com(page):    ##列表页
    # print('page is ',page)
    headers,data=header_body_update(page)
    prices=[]
    hotel_lists=[]
    fail_try=10
    while(fail_try):                     ###这个主要是，fang.com会随机返回几个10054或者10053，如果连页面都没读取到，提取就是后话了，这网站没有封杀，即使使用单ip只会很少时候随机来几个10054 ，('Connection aborted.', error(10054, ''))
        hotel_info={}
        try:
            proxy = proxy_update()
            hotel_list_requests=requests.post('https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx', data=data,
                                              headers=headers)#,timeout=2,proxies=proxy
            text=hotel_list_requests.text
            
            hotel_info=eval(text)
            prices = json.loads(hotel_info['HotelMaiDianData']['value']['htllist'])
            hotel_lists = hotel_info['hotelPositionJSON']
            for hotel, price in zip(hotel_lists, prices):
                hotel.update(price)

                line = json.dumps(hotel) + '\n'
                file.write(line)
            print(hotel_lists)
            print('success',page)
            break
            #print text
        except Exception as e:
            print(e)
            fail_try=fail_try-1
    if fail_try==0:
        print('unsuccess page',page)




    time.sleep(1)

    # lock.acquire()
    # print(hotel_lists)
    # lock.release()

'''
    text=''
    se = etree.HTML(text)                                 ###########为了利于大家学习，这段演示xpath提取信息
    all_dl=se.xpath('//dl[@class="list rel"]')
    print(len(all_dl))
    for dl in all_dl:
        title=dl.xpath('.//dd[@class="info rel floatr"]/p[@class="title"]/a/text()')[0]
        url=dl.xpath('.//dd[@class="info rel floatr"]/p[@class="title"]/a/@href')[0]
        url='http://esf.sz.fang.com'+url

        info_list=dl.xpath('.//dd[@class="info rel floatr"]/p[@class="mt12"]/text()')
        #print json.dumps(info,ensure_ascii=False)    #py2显示汉字，py3可以直接print mt12
        info=''
        for l in info_list:
            l2= re.findall('\S*',l)[0]          ###消除空白和换行
            #print m_str
            info+=l2+'|'

        time.sleep(1)
        # total_price,price_squere,huxin,cankao_shoufu,shiyong_mianji,jianzhu_mianji,years,discription=get_detail(url)


        lock.acquire()                  ###这里叫锁，一是保证count计数准确，而是不会导致多个线程乱print，导致看不清楚。加锁的目的是别的线程不能运行这段代码了。但我之前看到有的人乱加锁，把消耗时间很长的代码加锁，那样导致多线程就基本个废物
        global count
        count+=1
        print(time.strftime('%H:%M:%S', time.localtime(time.time())), '    ', count)
        print('列表页：')
        print(' title: %s\n url: %s\n info: %s\n' % (title, url, info))

        print('详情页:')
        # print(
        #     ' total_price: %s\n price_squere: %s\n huxin: %s\n cankao_shoufu: %s\n shiyong_mianji: %s\n jianzhu_mianji: %s\n years: %s \n' % (
        #     total_price, price_squere, huxin, cankao_shoufu, shiyong_mianji, jianzhu_mianji, years))
        print('**************************************************************')
        lock.release()

'''

def get_detail(url):    ###详情页

    header={'User-Agent':random.choice(user_agent_list)}
    header.update({"Host":"esf.sz.fang.com"})

    while(1):
        content=''
        try:
            content=requests.get(url,headers=header,timeout=10).content
        except Exception as  e:
            print(e)
            pass
        if content!='':
            break

    content=content.decode('gbk').encode('utf8')  ##查看网页源代码可看到是gbk编码，直接print的话，如果你在pycharm设置控制台是utf8编码，那么控制台的中文则会乱码，cmd是gbk的恰好可以显示。如果你在pycharm设置控制台是utf8编码，需要这样做
    #print content

    inforTxt=getlist0(re.findall('(<div class="inforTxt">[\s\S]*?)<ul class="tool">',content))       ###########为了利于大家学习，这段演示正则表达式提取信息，某些信息可能在有的房子界面没有，要做好判断
    #print inforTxt

    total_price=getlist0(re.findall('</span>价：<span class="red20b">(.*?)</span>',inforTxt))

    price_squere=getlist0(re.findall('class="black">万</span>\((\d+?)元[\s\S]*?<a id="agantesfxq_B02_03"',inforTxt))
    huxin=getlist0(re.findall('<dd class="gray6"><span class="gray6">户<span class="padl27"></span>型：</span>(.*?)</dd>',inforTxt))
    cankao_shoufu=getlist0(re.findall('参考首付：</span><span class="black floatl">(.*?万)</span> </dd>',inforTxt))
    shiyong_mianji=getlist0(re.findall('>使用面积：<span class="black ">(.*?)</span></dd>',inforTxt))
    shiyong_mianji=getlist0(re.findall('\d+',shiyong_mianji))
    jianzhu_mianji=getlist0(re.findall('建筑面积：<span class="black ">(.*?)</span></dd>',inforTxt))
    jianzhu_mianji=getlist0(re.findall('\d+',jianzhu_mianji))
    years=getlist0(re.findall('<span class="gray6">年<span class="padl27"></span>代：</span>(.*?)</dd>',inforTxt))

    discription=getlist0(re.findall('style="-moz-user-select: none;">([\s\S]*?)<div class="leftBox"',content))
    #print discription
    #print total_price,price_squere,huxin,cankao_shoufu,shiyong_mianji,jianzhu_mianji,years

    return total_price,price_squere,huxin,cankao_shoufu,shiyong_mianji,jianzhu_mianji,years,discription




#get_detail('http://esf.sz.fang.com/chushou/3_193928457.htm')
def getlist0(list):
    if list:
        return list[0]
    else:
        return '空'

if __name__=='__main__':
    fr = open('proxy.txt', 'r')
    fr.readline()  # skip the header
    fr.readline()
    proxies = fr.readlines()
    fr.close()


    page_num=get_page()
    print(page_num)
    file = open('%s.json'%city, 'w', encoding='utf-8')
    #'''                                       ##这个是单线程，单线程爬很慢，3000个房子信息，一个5秒，那也得15000秒了，很耽误时间
    for i in range(1,page_num):
        data = {'page': i, 'cityPY': 'shanghai', 'cityId': 2, 'cityCode': '021'}
        fang_com(i)
    '''
    threads=[]                                            ###这个是演示多线程爬取
    for i in range(1,page_num):                                             #开了100线程，这样开100线程去爬100页面的详情页面，因为fang.com只能看100页

        t=threading.Thread(target=fang_com,args=(i,))           ###这样做没问题，但如果你是爬取1000页面，也这样做就不合适了，python开多了线程会导致线程创建失败，100线程已经很快了，网速是瓶颈了这时候，我开100线程时候网速是800KB左右的网速，我宽带才4M，运营商还算比较良心了，4M宽带400k

        threads.append(t)

        t.start()

    for t in threads:
        t.join()
    '''
    file.close()
    print('over')

