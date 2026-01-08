# python-backend-fastapi-junior
Junior backend project using Python and FastAPI.

# python-backend-fastapi-junior

Proyecto backend desarrollado en **Python** usando **FastAPI**, creado con el objetivo de **aprender y reforzar conceptos de backend** mientras construyo algo funcional, viniendo de un background en **Node.js y NestJS**.

Este repositorio sirve como práctica progresiva para entender la arquitectura, buenas prácticas y flujo de trabajo en backend con Python.

---

## 🚀 Tech Stack

- **Python**
- **FastAPI** – Framework web
- **Uvicorn** – Servidor ASGI
- **SQLAlchemy** – ORM
- **Pydantic** – Validación de datos

---

## 🧱 Arquitectura

El proyecto utiliza una **arquitectura modular por capas**, similar al enfoque por módulos de NestJS, separando responsabilidades de forma clara:

- **routes** → manejo de endpoints HTTP
- **schemas** → validación y serialización de datos (DTOs)
- **services** → lógica de negocio
- **models** → modelos de base de datos (ORM)
- **db** → configuración de base de datos y sesiones
- **core** → configuración general del proyecto

Esta estructura facilita el mantenimiento, la escalabilidad y la comprensión del proyecto.

---

## 📁 Estructura del proyecto

```text
app/
├── core/
│   └── config.py
├── db/
│   ├── base.py
│   └── session.py
├── modules/
│   └── avatar/
│       ├── models/
│       │   └── avatar.py
│       ├── routes/
│       │   └── avatar.py
│       ├── schemas/
│       │   └── avatar.py
│       └── services/
│           └── avatar_service.py
├── main.py
└── __init__.py

⚙️ Setup del proyecto

1️⃣ Clonar el repositorio
git clone https://github.com/pucara05/python-backend-fastapi-junior.git
cd python-backend-fastapi-junior

2️⃣ Crear y activar entorno virtual

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python3 -m venv venv
source venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

▶️ Ejecutar la aplicación
uvicorn app.main:app --reload

▶️ Ejecutar la aplicación
uvicorn app.main:app --reload

📌 Estado del proyecto

🟡 En desarrollo

El proyecto se irá ampliando progresivamente a medida que se incorporen:

modelos

endpoints

lógica de negocio

buenas prácticas adicionales

🎯 Objetivo personal

Este proyecto forma parte de mi proceso de aprendizaje como Backend Developer Junior, con el objetivo de:

reforzar Python

entender FastAPI a fondo

aplicar buenas prácticas

construir bases sólidas para proyectos más grandes