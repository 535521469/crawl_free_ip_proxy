BOT_NAME = 'FiveOneNewHTTPProxySpider'
SPIDER_MODULES = ['fiveone.spiders', ]
LOG_LEVEL = 'DEBUG'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': None,
}


DOWNLOAD_TIMEOUT = 1
RETRY_ENABLED = 0


