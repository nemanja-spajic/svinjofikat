from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()

users = {
    "Uros": True,
    "Dusan": True,
    "Coa": True,
    "Rile": True,
    "Rados": True,
    "Aleksic": True,
    "Spaja": True,
    "Bora": False,
}


@app.get("/certificate/{user}")
def get_certificate(user: str):
    if users.get(user):
        if users[user]:
            return FileResponse("certificates/positive.jpeg")
    return FileResponse("certificates/negative.jpeg")


@app.get("/updateStatus/{user}/{status}")
def update_status(user: str, status: bool):
    users[user] = status
