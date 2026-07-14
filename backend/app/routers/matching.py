from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.auth.dependencies import get_current_user

from app.services.matching_service import get_matching_listings

from app.schemas.matching import MatchResponse

router=APIRouter(

    prefix="/matching",

    tags=["AI Matching"]

)

@router.get(

    "",

    response_model=list[MatchResponse]

)

def get_matches(

    current_user=Depends(get_current_user),

    db:Session=Depends(get_db)

):

    return get_matching_listings(

        db,

        current_user["id"]

    )