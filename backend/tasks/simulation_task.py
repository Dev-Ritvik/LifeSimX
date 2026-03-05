from core.celery_app import celery

@celery.task
def run_simulation(data):

    return {
        "income_percentile": [50000, 120000],
        "burnout_probability": 0.37,
        "automation_risk": 0.35
    }