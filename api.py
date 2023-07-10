from flask import Flask, request
from datetime import datetime
from registro import Registro

app = Flask(__name__)

@app.route('/api/v0/<device_id>/<card_id>', methods=['POST'])
def registrar(device_id, card_id):
    # Obtener la IP del cliente que realiza la petición
    ip_request = request.remote_addr

    # Crear objeto Registro
    ts = datetime.now()
    registro = Registro(device_id=device_id, card_id=card_id, ts=ts, ip_request=ip_request)

    # Guardar registro en la base de datos
    registro.guardar_registro()

    return "",201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
