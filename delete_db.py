from database import Base,engine
from models import Admin

print("Drop database .....")

Admin.metadata.drop_all(engine)