from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Modelos de datos
class Deporte(BaseModel):
    nombre: str

class Equipo(BaseModel):
    nombre: str
    deporte_id: int

class Liga(BaseModel):
    nombre: str
    deporte_id: int

# Almacenamiento de datos simulado en memoria
db_deportes: Dict[int, Deporte] = {}
db_equipos: Dict[int, Equipo] = {}
db_ligas: Dict[int, Liga] = {}
deporte_id_counter = 0
equipo_id_counter = 0
liga_id_counter = 0

# Operaciones CRUD para Deportes
@app.post("/deportes/", response_model=Deporte)
async def crear_deporte(deporte: Deporte):
    global deporte_id_counter
    deporte_id_counter += 1
    db_deportes[deporte_id_counter] = deporte
    return deporte

@app.get("/deportes/", response_model=List[Deporte])
async def listar_deportes():
    return list(db_deportes.values())

@app.put("/deportes/{deporte_id}/", response_model=Deporte)
async def actualizar_deporte(deporte_id: int, deporte: Deporte):
    if deporte_id not in db_deportes:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")
    db_deportes[deporte_id] = deporte
    return deporte

@app.delete("/deportes/{deporte_id}/", response_model=Deporte)
async def eliminar_deporte(deporte_id: int):
    if deporte_id not in db_deportes:
        raise HTTPException(status_code=404, detail="Deporte no encontrado")
    deporte_eliminado = db_deportes.pop(deporte_id)
    return deporte_eliminado

# Operaciones CRUD para Equipos
@app.post("/equipos/", response_model=Equipo)
async def crear_equipo(equipo: Equipo):
    global equipo_id_counter
    equipo_id_counter += 1
    db_equipos[equipo_id_counter] = equipo
    return equipo

@app.get("/equipos/", response_model=List[Equipo])
async def listar_equipos():
    return list(db_equipos.values())

@app.put("/equipos/{equipo_id}/", response_model=Equipo)
async def actualizar_equipo(equipo_id: int, equipo: Equipo):
    if equipo_id not in db_equipos:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    db_equipos[equipo_id] = equipo
    return equipo

@app.delete("/equipos/{equipo_id}/", response_model=Equipo)
async def eliminar_equipo(equipo_id: int):
    if equipo_id not in db_equipos:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    equipo_eliminado = db_equipos.pop(equipo_id)
    return equipo_eliminado

# Operaciones CRUD para Ligas
@app.post("/ligas/", response_model=Liga)
async def crear_liga(liga: Liga):
    global liga_id_counter
    liga_id_counter += 1
    db_ligas[liga_id_counter] = liga
    return liga

@app.get("/ligas/", response_model=List[Liga])
async def listar_ligas():
    return list(db_ligas.values())

@app.put("/ligas/{liga_id}/", response_model=Liga)
async def actualizar_liga(liga_id: int, liga: Liga):
    if liga_id not in db_ligas:
        raise HTTPException(status_code=404, detail="Liga no encontrada")
    db_ligas[liga_id] = liga
    return liga

@app.delete("/ligas/{liga_id}/", response_model=Liga)
async def eliminar_liga(liga_id: int):
    if liga_id not in db_ligas:
        raise HTTPException(status_code=404, detail="Liga no encontrada")
    liga_eliminada = db_ligas.pop(liga_id)
    return liga_eliminada
