from fastapi import FastAPI

from app.database.base import Base
from app.database.connection import engine

import app.models

from app.routers.auth import router as auth_router

app = FastAPI(
    title="Flatmate Finder API"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

from app.routers.users import router as users_router
app.include_router(users_router)

from app.routers.listing import router as listing_router
app.include_router(listing_router)

from app.routers.tenant_profile import router as tenant_profile_router
app.include_router(tenant_profile_router)

from app.routers.matching import router as matching_router
app.include_router(matching_router)

from app.routers.search import router as search_router
app.include_router(search_router)


@app.get("/")
def root():
    return {
        "message": "Flatmate Finder Backend Running"
    }