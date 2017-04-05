#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:chenshyiuan 
@file: Url_Util.py 
@time: 2017/04/04 
"""

# Client ID
# cbb90c8c9e00b757a07a
# Client Secret
# 3061191bfcd5879717b3b764c574d9ec806b2aa1
from distutils.log import Log

CLIENTID = 'cbb90c8c9e00b757a07a'
CLIENT_SECRET = '3061191bfcd5879717b3b764c574d9ec806b2aa1'
USER_BASE_URL = 'https://api.github.com/users'


def get_userlist_url(since=0):
    if isinstance(since, int):

        since = str(since)
        url = set_get_request_param(USER_BASE_URL, since=since, client_id=CLIENTID, client_secret=CLIENT_SECRET)
        return url
    elif isinstance(since, basestring):

        url = set_get_request_param(USER_BASE_URL, since=since, client_id=CLIENTID, client_secret=CLIENT_SECRET)
        return url
        # pass


def set_get_request_param(url, **params):  # 设置HTTP的GET方法的参数，并返回URL。
    if url is None:

        Log.error('url is none')
        return
    elif isinstance(url, basestring):  # 设置参数

        format_url = url + '?'
        for key in params:
            format_url = format_url + key + '=' + params[key] + '&'
        format_url = format_url[0:len(format_url) - 1]  # 去除掉最后的&
        return format_url


def set_client_key(url):  # 为url添加ClientKey 增加访问次数
    return set_get_request_param(url, client_id=CLIENTID, client_secret=CLIENT_SECRET)
    pass


# 0 29
if __name__ == '__main__':
    print get_userlist_url(0)
    print get_userlist_url(30)
    pass