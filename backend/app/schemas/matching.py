from pydantic import BaseModel

from app.schemas.listing import ListingResponse


class MatchResponse(BaseModel):

    listing: ListingResponse

    rule_score: int

    compatibility_score: int

    summary: str

    pros: list[str]

    cons: list[str]

    class Config:
        from_attributes=True