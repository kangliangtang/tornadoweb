from handler.index import IndexHandler
from handler.login import Login


url = [
    (r'/', IndexHandler),
    (r'/login', Login)
]
