from routes.user import user
from fastapi import FastAPI

app=FastAPI()

app.include_router(user)

#@app.get("/")
#def read_something():
 #   return {"msg":"Hellow World"}
