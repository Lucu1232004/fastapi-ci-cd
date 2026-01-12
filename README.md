# # FastAPI Backend con CI/CD Pipeline
Este proyecto demuestra un backend FastAPI listo para producción con pruebas automatizadas, Dockerización e implementación de CI/CD.

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

Autor: Samuel Patiño Lucumí
