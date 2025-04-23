# Practica 3

## Samuel Patiño Lucumí - 2226503

# FastAPI CI/CD Example

Este es un proyecto de ejemplo que implementa una API con [FastAPI](https://fastapi.tiangolo.com/) y un pipeline CI/CD completo usando **GitHub Actions**, **Docker** y despliegue en **Render**.

## Estructura

fastapi-ci-cd/
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .pre-commit-config.yaml
├── .github/
│   └── workflows/ci-cd.yml
└── README.md

## Tecnologías Utilizadas

- FastAPI
- Docker
- GitHub Actions
- Pytest
- Render.com
- pre-commit + Black

## Instalación Local

```bash
# Clona el repositorio
git clone https://github.com/Lucu1232004/fastapi-ci-cd.git
cd fastapi-ci-cd

# Crea entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala dependencias
pip install -r requirements.txt

uvicorn app.main:app --reload
