from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from sql_alquemy import banco 

app = Flask(__name__)

# Configuração do SQLAlchemy server se for um docker compose
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:32133@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

# Inicialização do SQLAlchemy com o aplicativo Flask
banco.init_app(app)

# Chamada para criar todas as tabelas uma vez na primeira requisiçao
with app.app_context():
    banco.create_all()

# Definindo os endpoints da API
api.add_resource(Hoteis, '/Hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>') 

if __name__ == '__main__':
    app.run(debug=True)
