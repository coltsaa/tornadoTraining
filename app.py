# !/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__='EiJi'
from tornado import web,httpserver,ioloop

import random


def get_lucky_num():
    red_num_list = list(range(1, 34))
    blue_num_list = list(range(1, 17))
    random.shuffle(red_num_list)
    res = {
        'red_num': red_num_list[:6],
        'blue_num': random.choice(blue_num_list),
    }
    return res

class IndexPageHander(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write('hello world')


application = web.Application([
    (r"/",IndexPageHander),
])

if __name__  == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()