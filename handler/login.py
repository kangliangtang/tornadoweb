import tornado.web


class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        self.render("login.html")
