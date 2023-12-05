from flask import Flask, request, jsonify
from datetime import datetime
from registro import Registro

app = Flask(__name__)


@app.route('/api/v0/events', methods=['GET'])
def get_events():
    resultados = Registro.get_all(Registro)
    return jsonify(resultados),200

@app.route('/api/v0/<device_id>/<card_id>', methods=['POST'])
def registrar(device_id, card_id):
    ip_request = request.remote_addr
    ts = datetime.now()
    registro = Registro(device_id=device_id, card_id=card_id, ts=ts, ip_request=ip_request)
    registro.guardar_registro()
    return "",201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
