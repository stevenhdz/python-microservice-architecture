# Ejercicio Práctico: Comunicación entre Microservicios

Dos microservicios independientes construidos en **Python + Flask** que se
comunican entre sí mediante **API REST (HTTP/JSON)**:

| Servicio | Puerto | Responsabilidad |
|---|---|---|
| `user_service` | 5001 | Administrar usuarios (CRUD mínimo en memoria) |
| `order_service` | 5002 | Crear pedidos, validando el usuario contra `user_service` vía REST |

## Cómo ejecutar

Un solo entorno virtual en la raíz del proyecto es suficiente para correr
ambos servicios (comparten las mismas dependencias: `flask` y `requests`).

```bash
# 1. Crear el entorno virtual (una sola vez)
cd python-microservice-architecture
python -m venv venv

# 2. Activarlo (ver tabla de comandos según tu entorno más abajo)

# 3. Instalar dependencias
pip install -r requirements.txt
```

**Activación del venv según sistema operativo / shell:**

| Entorno | Comando de activación |
|---|---|
| Linux/Mac (bash/zsh) | `source venv/bin/activate` |
| Linux/Mac (fish) | `source venv/bin/activate.fish` |
| Windows (PowerShell) | `venv\Scripts\Activate.ps1` |
| Windows (CMD) | `venv\Scripts\activate.bat` |
| Windows (Git Bash) | `source venv/Scripts/activate` |

> **PowerShell:** si aparece un error de ejecución de scripts deshabilitada,
> corre una vez: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

Luego, en dos terminales distintas (activando el mismo venv en cada una con
el comando de la tabla que corresponda a tu entorno):

```bash
# Terminal 1 — Servicio de Usuarios
cd user_service
python app.py                     # http://localhost:5001
```

```bash
# Terminal 2 — Servicio de Pedidos
cd order_service
python app.py                     # http://localhost:5002
```

## Pruebas manuales (evidencia)

El archivo [`requests.http`](./requests.http) contiene todas las peticiones
listas para ejecutar (compatible con la extensión **REST Client** de VS Code
o el HTTP Client de JetBrains): salud de cada servicio, creación de un
pedido para un usuario existente y el intento fallido con un usuario
inexistente.