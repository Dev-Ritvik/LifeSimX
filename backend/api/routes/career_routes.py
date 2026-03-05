from fastapi import APIRouter

router = APIRouter()

@router.get("/careers")
def get_careers():

    return {
        "careers":[
            {
                "id":"software_engineering",
                "title":"Software Engineering",
                "automation_risk":0.35
            },
            {
                "id":"product_design",
                "title":"Product Design",
                "automation_risk":0.25
            },
            {
                "id":"data_science",
                "title":"Data Science",
                "automation_risk":0.30
            }
        ]
    }