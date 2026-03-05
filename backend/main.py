from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="LifeSimX API")

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}
from api.routes.simulation_routes import router as simulation_router

app.include_router(simulation_router)
from api.routes.professional_routes import router as professional_router

app.include_router(professional_router)
from db.database import engine
from db.models import Base

from api.routes.career_routes import router as career_router
app.include_router(career_router)
from api.routes.network_routes import router as network_router
app.include_router(network_router)