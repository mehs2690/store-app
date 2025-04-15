# 🛒 Tienda de Abarrotes - Backend Flask API

Este proyecto es una API REST desarrollada en **Python con Flask**, diseñada para gestionar operaciones básicas de un
comercio electrónico de una tienda de abarrotes. Está estructurada con **arquitectura limpia**, integra
**PostgreSQL y MongoDB**, y todo corre en **contenedores Docker**.

---

## 📦 Stack Tecnológico

- **Flask**
- **PostgreSQL** (Relacional)
- **MongoDB** (No Relacional)
- **SQLAlchemy** + **Marshmallow**
- **Docker + Docker Compose**
- **Python Logging**
- **Validación de datos con Marshmallow**
- **Manejo de errores centralizado**

---

## 📁 Estructura del Proyecto

```plaintext
flask-app/
├── app/
│   ├── api/               # Rutas (BluePrints)
│   ├── core/              # Configuración, DB, Logging
│   ├── errors/            # Manejadores de errores
│   ├── models/            # Entidades
│   ├── repositories/      # Acceso a datos
│   └── schemas/           # Validación con Marshmallow
├── run.py                 # Punto de entrada
├── requirements.txt       # Dependencias
├── Dockerfile             # Imagen base
├── docker-compose.yml     # Orquestación de servicios
├── .env                   # Variables de entorno
└── README.md              # Esta documentación
```

---

## 🚀 Cómo correr el proyecto

### 1. Clonar repositorio

```bash
git clone https://github.com/tu-usuario/tienda-backend.git
cd tienda-backend/flask-app
```

### 2. Configurar entorno

Crea un archivo `.env` basado en esto:

```env
FLASK_ENV=development

# PostgreSQL
POSTGRES_DB=tienda_db
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# MongoDB
MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DB=tienda_mongo
```

### 3. Levantar con Docker

```bash
docker-compose up -d --build
```

---

## 🧪 Endpoints de prueba

- `GET /ping` – Prueba de vida
- `GET /db-check/postgres` – Verifica conexión con PostgreSQL
- `GET /db-check/mongo` – Verifica conexión con MongoDB
- `POST /clientes` – Valida un cliente (requiere body JSON)

---

## 🧰 Scripts útiles

```bash
# Ver logs
docker-compose logs -f

# Apagar contenedores
docker-compose down

# Reconstruir
docker-compose up --build
```

---

## ✅ Validación y manejo de errores

- Validaciones con `marshmallow`
- Manejo global de errores 404, 500 y excepciones personalizadas
- Logs centralizados usando el módulo `logging`

---

## 🧠 Futuro inmediato

- CRUD completo para Cliente, Artículo, Orden y Factura
- Repositorios desacoplados por tipo de base de datos
- Autenticación y autorización
- Pruebas unitarias e integración
- Diagramas UML de arquitectura

---

## 👨‍💻 Autor

Mauro Etzael (Tu nombre o equipo)
[GitHub](https://github.com/mehs2690)

---

## ⚖️ Licencia

MIT License
