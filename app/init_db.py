from app import db
from models import License
from datetime import datetime, timedelta

# Initialize the database
db.create_all()

# Seed some licenses for testing
def seed_data():
    licenses = [
        License(key="ABC123", product_id="SaaS-001", status="inactive", expires_at=datetime.utcnow() + timedelta(days=365)),
        License(key="DEF456", product_id="SaaS-002", status="inactive", expires_at=datetime.utcnow() + timedelta(days=365)),
        License(key="GHI789", product_id="SaaS-003", status="active", expires_at=datetime.utcnow() + timedelta(days=180)),
    ]

    for lic in licenses:
        db.session.add(lic)
    db.session.commit()
    print("Database seeded with test licenses!")

if __name__ == "__main__":
    seed_data()
