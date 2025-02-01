from models.index import users
from schemas.index import User
from fastapi import APIRouter
from config.db import con

user = APIRouter()

@user.get("/")
async def read_data():
    return con.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_data(id: int):
    return con.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write_data(user: User):
    con.execute(users.insert().values(
        name=user.name,
        email=user.email
    ))
    return con.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_data(id: int, user: User):
    con.execute(users.update().where(users.c.id == id).values(
        name=user.name,
        email=user.email
    ))
    return con.execute(users.select()).fetchall()

@user.delete("/{id}")  # ✅ Fix: Add 'id' parameter
async def delete_data(id: int):
    con.execute(users.delete().where(users.c.id == id))
    return con.execute(users.select()).fetchall()
