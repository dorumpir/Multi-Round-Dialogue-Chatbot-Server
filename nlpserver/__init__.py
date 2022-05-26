from flask import Flask


app = Flask(__name__)
#app.config.from_pyfile('blockchainbot.cfg')



from .views import api_view
app.register_blueprint(api_view)
