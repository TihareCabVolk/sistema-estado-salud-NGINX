# Este es el archivo principal para utilizar el Flask
from flask import Flask, jsonify
import os

app = Flask(__name__)

IDreplica = os.environ.get('HOSTNAME','replica_desconocida')
puerto_usado = int(os.environ.get('PUERTO', 5000))

@app.route('/estado', methods=['GET'])

def estado():
    return jsonify({
        "disponibilidad": True,
        "cupos_restantes": 12,
        "mensaje": 'Atención disponible',
        "atendido_por_contenedor": IDreplica,
        "puerto_interno": puerto_usado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=puerto_usado)