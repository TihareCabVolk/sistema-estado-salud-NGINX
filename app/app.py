# Este es el archivo principal para utilizar el Flask
from flask import Flask, jsonify, request, render_template
import os
import redis

app = Flask(__name__)

# Configuración del REDIS BD
redis_host = os.environ.get('REDIS_HOST', 'db_redis')
bd = redis.Redis(host=redis_host, port=6379, decode_responses=True)

# Inicializar cupos si no existen en la Base de Datos
if not bd.exists('cupos'):
    bd.set('cupos', 200)


# Configuración de las replicas
IDreplica = os.environ.get('HOSTNAME','replica_desconocida')
puerto_usado = int(os.environ.get('PUERTO', 3000))

# Ruta del Frontend
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/estado', methods=['GET'])
def estado():
    cupos_actuales = int(bd.get('cupos'))
    return jsonify({
        "disponibilidad": cupos_actuales > 0,
        "cupos_restantes": cupos_actuales,
        "mensaje": 'Atención disponible',
        "atendido_por_contenedor": IDreplica,
        "puerto_interno": puerto_usado
    })

# Crear una reseerva, este quita un cupo
@app.route('/reserva', methods=['POST'])
def crear_reserva():
    # decr es una operación atomica de Redis
    # resta 1 y devuelve el nuevo valor. 
    nuevos_cupos = bd.decr('cupos')

    # No permite cupos negativos
    if nuevos_cupos < 0:
        bd.set('cupos', 0) 
        return jsonify({"error": "No hay cupos disponibles"}), 400

    return jsonify({
        "mensaje": "Reserva confirmada",
        "cupos_actualizados": nuevos_cupos,
        "atendido_por": IDreplica
    }), 201

# Cancelar una reserva, este suma una reserva
@app.route('/reserva', methods=['DELETE'])
def cancelar_reserva():
    # incr es una operación atomica de Redis
    # suma 1 y devuelve el nuevo valor. 
    nuevos_cupos = bd.incr('cupos')

    # No permite cupos negativos
    if nuevos_cupos > 200:
        bd.set('cupos', 200) 
        return jsonify({"error": "No hay reservas para cancelar, todos los cupos estan disponibles"}), 400

    return jsonify({
        "mensaje": "Reserva cancelada, cupo liberado exitosamente",
        "cupos_actualizados": nuevos_cupos,
        
        "atendido_por": IDreplica,
        "puert_interno": puerto_usado
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=puerto_usado)