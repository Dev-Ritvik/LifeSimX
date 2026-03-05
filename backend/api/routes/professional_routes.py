from fastapi import APIRouter

router = APIRouter()

@router.get("/professionals")
def get_professionals():

    return {
        "professionals": [
            {
                "id": "prof_001",
                "name": "Alex Chen",
                "career_archetype": "software_engineering",
                "title": "Senior Software Engineer",
                "company": "Tech Company",
                "reputation_score": 4.8
            }
        ]
    }