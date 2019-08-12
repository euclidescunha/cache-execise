from flask import Flask

from app.views.localization import index, healthcheck, get_closest_location

app = Flask(__name__)

app.add_url_rule('/healthcheck', methods=['GET'], endpoint='healthcheck', view_func=healthcheck)
app.add_url_rule('/', methods=['POST', 'GET'], endpoint='index', view_func=index)
app.add_url_rule('/closest', methods=['POST', 'GET'], endpoint='closest', view_func=get_closest_location)

