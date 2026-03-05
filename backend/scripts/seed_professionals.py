import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from db.database import SessionLocal
from db.models import Professional

db = SessionLocal()

demo_professionals = [
    Professional(
        name="Alex Chen",
        career_archetype="software_engineering",
        title="Senior Software Engineer",
        company="Google",
        reputation_score=4.9
    ),
    Professional(
        name="Maya Patel",
        career_archetype="product_design",
        title="Product Designer",
        company="Adobe",
        reputation_score=4.7
    ),
    Professional(
        name="Daniel Kim",
        career_archetype="data_science",
        title="Data Scientist",
        company="OpenAI",
        reputation_score=4.8
    )
]

for p in demo_professionals:
    db.add(p)

db.commit()

print("Demo professionals inserted.")