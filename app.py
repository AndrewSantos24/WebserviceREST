from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis,Hotel
#começando com o flask
app = Flask(__name__)
api = Api(app)

api.add_resource(Hoteis,'/Hoteis')
api.add_resource(Hotel,'/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    app.run(debug=True)