from sql_alquemy import banco

class HotelModel(banco.Model):
    
    __tablename__ = 'hoteis'
    hotel_id = banco.Column(banco.String, primary_key = True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision=1))
    diaria = banco.Column(banco.Float(precision=2))
    cidade = banco.Column(banco.String(40))

    def __init__(self,hotel_id,nome,estrelas,diaria,cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade
    
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
    #cls e a abreviaçao da classe como um todo
    # usando o query basicamente so usamos o trecho o metodo para consulta pqp foda
    @classmethod
    def find_hotel(cls,hotel_id):
        # e pegando o primeiro resultado usando o first()
        hotel = cls.query.filter_by(hotel_id=hotel_id).first() # SELECT * FROM hoteis WHERE hotel_id = hotel_id                                                    
        if hotel:
            return hotel
        return None
    def save_hotel(self) :
        banco.session.add(self)
        banco.session.commit()                                               