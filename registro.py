from datetime import datetime
from sqlalchemy import Column, DateTime, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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

def guardar_registro(registro):
    # Configurar la conexión a la base de datos
    engine = create_engine('mysql+mysqlconnector://app:1234@localhost/registros')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Guardar el registro en la base de datos
    session.add(registro)
    session.commit()
    session.close()
