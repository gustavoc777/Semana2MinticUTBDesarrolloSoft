from fastapi import FastAPI

app= FastAPI()

@app.get("saludos")
async def root():
    return {"message":"Hola MisionTIC 2022"}

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
    return{"user_id": user_id}

cursos=[{"curso":" Fundamentos programacion"},{"curso":"Programacion Basica"},{"curso:Desarrollo Siftware"} ]

@app.get("/cursos")
async def read_item(skip: int=o, limit: int =10):
    return cursos[skip : skip + limit]