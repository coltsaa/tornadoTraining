# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @author:'ryo'
from tornado import web,httpserver,ioloop
import time


class IndexHandler(web.RequestHandler):
    def get(self,*args,**kwargs):#handle get request
        # self.write('hello world')
        self.render('index.html',time = time.strftime('%Y-%m-%d %H:%M:%S'))

class FindHandler(web.Application):
    def post(self,*args,**kwargs):
        name = self.get_argument('name',None)
        if name:
            spider = JobSpider()
            data = spider.run(name)
            self.render('find.html',data = data)

application = web.Application([
    (r"/",IndexHandler),
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()

