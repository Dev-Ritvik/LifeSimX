from pydantic import BaseModel

class PersonalityVectors(BaseModel):
    risk_tolerance: int
    structured_learning: int
    creative_drive: int
    social_energy: int
    technical_aptitude: int
    long_term_orientation: int


class SimulationRequest(BaseModel):
    career_archetype: str
    vectors: PersonalityVectors


class SimulationResponse(BaseModel):
    simulation_id: str
    career_archetype: str
    regret_probability: float