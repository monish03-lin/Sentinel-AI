from fastapi import FastAPI

from backend.app.database import engine, base

from backend.app.routes.url_routes import router as url_router
from backend.app.routes.email_routes import router as email_router
from backend.app.routes.history_routes import router as history_router
from backend.app.routes.home_routes import router as home_router

base.metadata.create_all(bind=engine)

app = FastAPI(title="Sentinel AI")

app.include_router(home_router)
app.include_router(url_router)
app.include_router(email_router)
app.include_router(history_router)