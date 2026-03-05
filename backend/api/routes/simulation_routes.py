from fastapi import APIRouter
from api.models.simulation_models import SimulationRequest, SimulationResponse

router = APIRouter()

@router.post("/simulate", response_model=SimulationResponse)
def simulate_career(request: SimulationRequest):

    return {
        "simulation_id": "sim_demo_001",
        "career_archetype": request.career_archetype,
        "regret_probability": 0.42
    }