# 🌐 Objetivo General

Desarrollar una API RESTful de un sistema de comercio electrónico para una tienda de abarrotes con funcionalidades
básicas de CRUD para las entidades:

- Cliente

- Artículo

- Orden de Compra

- Factura

Con integración a:

- PostgreSQL (base de datos relacional)

- MongoDB (base de datos no relacional)

Usando los frameworks:

- Flask

- Django

- FastAPI

Y bajo arquitectura limpia, todo en contenedores Docker, con documentación en Markdown y diagramas UML cuando sea
necesario.

## 💻 Entorno Base (común para los tres frameworks)

✅ Paso 1: Preparar entorno de trabajo (esto es usando el entorno de MacOS Sequoia 15.3.2):

- VS Code

- iTerm

- Docker

- Git

## 🛠️ Herramientas necesarias

Ejecuta estos comandos para confirmar instalación y versión de cada herramienta:

```bash
# Docker
docker --version

# Git
git --version

# Python
python3 --version

# Pip
pip3 --version

# Virtualenv
python3 -m pip install virtualenv

# Node.js (para documentación con herramientas como Mermaid.js si lo deseas)
node -v

```

## 🧰 Crear estructura general de carpetas

Creamos un directorio raíz con subproyectos para cada framework:

```bash
mkdir store-backend
cd store-backend
mkdir flask-app django-app fastapi-app

```

## 📂 Estructura sugerida para cada proyecto (modo inicial)

```bash
store-backend/
├── flask-app/
├── django-app/
└── fastapi-app/

```

Dentro de cada uno vamos a crear:

```bash
flask-app/
├── app/
├── tests/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

```
