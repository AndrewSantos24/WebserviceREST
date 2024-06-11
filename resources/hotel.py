from flask_restful import Resource

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
    def get(self,hotel_id):
        for hotel in hoteis:
            # print(hotel)
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message':'Hotel not Fund!'}, 404 #status code nao encontrado
        # pass
    def post(self,hotel_id):
        pass
    def put(self,hotel_id):
        pass
    def delete(self,hotel_id):
        pass