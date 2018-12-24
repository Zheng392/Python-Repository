# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tutorial.pipelines.TutorialPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# 如果不想使用代理IP，可以将下面这段DOWNLOADER_MIDDLEWARES代码注释掉
DOWNLOADER_MIDDLEWARES = {
    'tutorial.middlewares.RandomUserAgent': 1,
    # 不用ip代理的话就把下面注释掉
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    # 'tutorial.middlewares.ProxyMiddleware': 100,

    #pause Scrapy and resume after x minutes
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'tutorial.middlewares.SleepRetryMiddleware': 100,
}

RETRY_TIMES=30

USER_AGENTS=[]
with open('./User agent.txt','r') as f:
    for line in f.readlines():
        USER_AGENTS.append(line.strip())


PROXIES = [
    {'ip_port': '120.83.103.119:808', 'user_pass': ''},
    {'ip_port': '110.73.0.38:8123', 'user_pass': ''},
    {'ip_port': '183.32.88.18:808', 'user_pass': ''},
    {'ip_port': '113.121.254.192:808', 'user_pass': ''},
    {'ip_port': '180.110.6.6:808', 'user_pass': ''},
    {'ip_port': '61.191.173.31:808', 'user_pass': ''},
    {'ip_port': '110.72.33.106:8123', 'user_pass': ''},

    # {'ip_port': '202.108.2.42:80', 'user_pass': ''},
    # {'ip_port': '122.96.59.104:80', 'user_pass': ''},
    # {'ip_port': '120.76.243.40:80', 'user_pass': ''},
    # {'ip_port': '139.196.108.68:80', 'user_pass': ''},
    # {'ip_port': '60.194.100.51:80', 'user_pass': ''},
    # {'ip_port': '202.171.253.72:80', 'user_pass': ''},
    # {'ip_port': '123.56.74.13:8080', 'user_pass': ''},
]

# DEFAULT_REQUEST_HEADERS={
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#                'Accept - Encoding':'gzip, deflate, br',
#                'Accept-Language':'en-US,en;q=0.9',
#                'Connection':'Keep-Alive',
# 	      'Cache-Control': 'max-age=0',
# }

LOG_LEVEL = 'INFO'