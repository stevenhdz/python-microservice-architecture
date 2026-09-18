import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

USER_SERVICE_URL = "http://localhost:5001"

pedidos = {}
contador_id = 0


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "order-service"}), 200


@app.get("/pedidos")
def listar_pedidos():
    return jsonify(list(pedidos.values())), 200


@app.post("/pedidos")
def crear_pedido():
    global contador_id
    data = request.get_json(force=True)
    usuario_id = data.get("usuario_id")
    producto = data.get("producto")

    if usuario_id is None or producto is None:
        return jsonify({"error": "usuario_id y producto son obligatorios"}), 400

    # --- Comunicación entre microservicios vía REST ---
    try:
        respuesta = requests.get(
            f"{USER_SERVICE_URL}/usuarios/{usuario_id}", timeout=3
        )
    except requests.exceptions.ConnectionError:
        return jsonify(
            {"error": "El Servicio de Usuarios no está disponible"}
        ), 503

    if respuesta.status_code == 404:
        return jsonify({"error": "El usuario indicado no existe"}), 404
    if respuesta.status_code != 200:
        return jsonify({"error": "Error al validar el usuario"}), 502

    usuario = respuesta.json()

    contador_id += 1
    pedido = {
        "id": contador_id,
        "producto": producto,
        "usuario": usuario,
    }
    pedidos[contador_id] = pedido
    return jsonify(pedido), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)