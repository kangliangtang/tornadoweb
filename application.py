import tornado.web
import os
from url import url

settings = {
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'template_path': os.path.join(os.path.dirname(__file__), 'template')

}


application = tornado.web.Application(
    handlers=url,
    **settings
)
