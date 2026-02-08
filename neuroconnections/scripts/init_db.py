from neuroconnections.app.db.base import Base
from neuroconnections.app.db.session import engine
from neuroconnections.app.db import models  # noqa

Base.metadata.create_all(bind=engine)
print("Database initialized.")
