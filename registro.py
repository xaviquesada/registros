from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import requests

Base = declarative_base()

class Registro(Base):
    __tablename__ = 'registros'

    id = Column(BigInteger, primary_key=True)
    device_id = Column(String)
    card_id = Column(String)
    ts = Column(DateTime)
    ip_request = Column(String)

    def __init__(self, device_id, card_id, ts, ip_request):
        self.device_id = device_id
        self.card_id = card_id
        self.ts = ts
        self.ip_request = ip_request

    def informar(self):
        requests.post(
            url="http://ntfy.sh/el_meu_topic",
            data=f"La targeta:{self.card_id} ha fitxat al dispositiu: {self.device_id} amb data i hora {self.ts} des de la IP: {self.ip_request}",
            headers={"Title": f"Nou fixatge a {self.device_id}"}
        )

    def guardar_registro(self):
        # Configurar la conexión a la base de datos
        engine = create_engine('mysql+mysqlconnector://app:1234@localhost/registros')
        Session = sessionmaker(bind=engine)
        session = Session()
        self.informar()

        # Guardar el registro en la base de datos
        session.add(self)
        session.commit()
        session.close()
