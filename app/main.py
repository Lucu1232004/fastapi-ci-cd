from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello CI/CD"}


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
