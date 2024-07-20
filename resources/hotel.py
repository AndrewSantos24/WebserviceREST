from flask_restful import Resource , reqparse
from models.hotel import HotelModel

hoteis =[
    {
        'hotel_id': 'alpha',
        'nome':'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.30,
        'cidade':'Recife'

    },
    {
        'hotel_id': 'lovethunder',
        'nome':'Amor e trovao',
        'estrelas': 3.7,
        'diaria': 250,
        'cidade':'Caruaru'

    },
    {
        'hotel_id': 'wolvdead',
        'nome':'wolverine e deadpool',
        'estrelas': 4.9,
        'diaria': 500,
        'cidade': 'Joao Pessoa'

    }
]

class Hoteis (Resource):
    def get(self):
        return {'Hoteis':hoteis}

class Hotel(Resource):
    
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')


    def get(self,hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {"message":'Hotel {} not Fund!'.format(hotel_id)}, 404 #status code nao encontrado

    def post(self,hotel_id):
        try:
            if HotelModel.find_hotel(hotel_id):
                return {"mensage":'Hotel {} ja cadastrado !'.format(hotel_id)}, 400 # erro com significado bad requests
            dados = Hotel.argumentos.parse_args()
            hotel_objeto = HotelModel(hotel_id, **dados)
            hotel_objeto.save_hotel()
            return hotel_objeto.json(), 200
        except:
            return 400

        
    def put(self,hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #OK
        hoteis.append(novo_hotel)
        return novo_hotel, 201  # created
    
    def delete(self,hotel_id):
        #para ele nao pensar que estamos usando o hoteis ja passado colocamos como global
        global hoteis
        #vamos usar list compreenchion 
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'hotel Deleted.'}
        pass