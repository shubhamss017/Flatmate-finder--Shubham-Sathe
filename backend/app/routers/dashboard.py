from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user

from app.schemas.dashboard import OwnerDashboard

from app.services.dashboard_service import (
    get_owner_dashboard
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/owner",
    response_model=OwnerDashboard
)
def owner_dashboard(

    current_user=Depends(get_current_user),

    db: Session = Depends(get_db)

):

    return get_owner_dashboard(

        db,

        current_user["id"]

    )