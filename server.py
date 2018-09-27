import tornado.options
import tornado.httpserver
import tornado.ioloop
from application import application


# 用来定义options选项变量的方法，定义的变量可以在全局的tornado.options.options中获取使用
tornado.options.define(name='port', default=8001, type=int, multiple=False, help='run on port')


def run():
    # 转换命令行define参数，并将转换后的值对应的设置到全局options对象相应的属性上
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    run()
