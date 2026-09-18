from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = {
    1: {"id": 1, "nombre": "Camila Restrepo", "email": "camila@example.com"},
    2: {"id": 2, "nombre": "Juan Pérez", "email": "juan@example.com"},
}


@app.get("/health")
def health():
    """Endpoint de salud, útil para monitoreo entre servicios."""
    return jsonify({"status": "ok", "service": "user-service"}), 200


@app.get("/usuarios")
def listar_usuarios():
    return jsonify(list(usuarios.values())), 200


@app.get("/usuarios/<int:usuario_id>")
def obtener_usuario(usuario_id):
    usuario = usuarios.get(usuario_id)
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario), 200


@app.post("/usuarios")
def crear_usuario():
    data = request.get_json(force=True)
    nuevo_id = max(usuarios.keys()) + 1 if usuarios else 1
    usuario = {
        "id": nuevo_id,
        "nombre": data.get("nombre"),
        "email": data.get("email"),
    }
    usuarios[nuevo_id] = usuario
    return jsonify(usuario), 201


if __name__ == "__main__":
    # Puerto 5001 para no chocar con el Servicio de Pedidos (5002)
    app.run(host="0.0.0.0", port=5001, debug=True)