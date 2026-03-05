from fastapi import APIRouter

router = APIRouter()

@router.get("/network")
def get_network():

    return {
        "nodes":[
            {"id":"student","type":"student"},
            {"id":"alex","type":"professional"},
            {"id":"maya","type":"professional"}
        ],
        "edges":[
            {"source":"student","target":"alex"},
            {"source":"student","target":"maya"}
        ]
    }