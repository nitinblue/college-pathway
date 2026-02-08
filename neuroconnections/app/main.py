from fastapi import FastAPI
from neuroconnections.app.api import journeys, steps


app = FastAPI(title="NeuroConnections")


app.include_router(journeys.router)
app.include_router(steps.router)