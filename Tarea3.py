import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Diccionario para almacenar los usuarios
users_dict = {}


# Clase de usuario
class User(BaseModel):
    user_name: str
    user_id: int
    user_email: str
    age: int = None
    recommendations: list = []
    ZIP: int = None


# 1. Crear un usuario con un ID único
# 2. Regresar mensaje de error si se envía un ID repetido
@app.post("/create_user/")
async def create_user(user: User):
    user_id = user.user_id
    if user_id in users_dict:
        raise HTTPException(status_code=400, detail="El ID de usuario ya existe")
    users_dict[user_id] = user
    return {"user_id": user_id, "message": "Usuario creado exitosamente"}


# 3. Actualizar información de un usuario por ID
@app.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in users_dict:
        raise HTTPException(status_code=404, detail="El ID de usuario no existe")
    users_dict[user_id] = user
    return {"user_id": user_id, "message": "Usuario actualizado exitosamente"}


# 4. Obtener información de un usuario por ID
@app.get("/get_user/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_dict:
        raise HTTPException(status_code=404, detail="El ID de usuario no existe")
    user = users_dict[user_id]
    return user


# 5. Eliminar información de un usuario por ID
@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_dict:
        raise HTTPException(status_code=404, detail="El ID de usuario no existe")
    del users_dict[user_id]
    return {"message": "Usuario eliminado exitosamente"}


if __name__ == "__main__":
    uvicorn.run("Tarea3:app", host="0.0.0.0", port=5002, log_level="info", reload=False)
