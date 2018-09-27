import json
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        language = self.get_query_argument('language')
        lst = ["www.lenotom.com", "tangeml@163.com"]
        lst.insert(0, language)
        self.render("index.html", info=lst)

    def post(self):
        data = self.request.body
        self.write(data)
