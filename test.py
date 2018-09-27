# import tornado.web
# import tornado.ioloop
# import os
#
#
# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('get')
#
#     def post(self):
#         self.write('post')
#
#
# settings = {
#     'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
#     'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
#     'debug': True,
# }
#
#
# def make_app():
#     return tornado.web.Application(
#         [(r'/', IndexHandler)],
#         **settings
#     )
#
#
# def start(port):
#     app = make_app()
#     app.listen(port)
#     tornado.ioloop.IOLoop.current().start()
#
#
# if __name__ == '__main__':
#     start(8000)
