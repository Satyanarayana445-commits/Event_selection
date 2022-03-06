from database import Base,engine
from models import Admin

print("Create database .....")

Admin.metadata.create_all(engine)