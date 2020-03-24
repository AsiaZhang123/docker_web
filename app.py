from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from root_view import root
import configs


app = Flask(__name__)
app.config.from_object(configs)

app.register_blueprint(root)

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

#
# if __name__ == '__main__':
#     app.run()


def main():
    print('ing....')
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(3278)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
