from sqlalchemy.orm import Session

from app.models.listing import Listing


def create_listing(
    db: Session,
    owner_id,
    listing
):
    db_listing = Listing(
        owner_id=owner_id,
        **listing.model_dump()
    )

    db.add(db_listing)

    db.commit()

    db.refresh(db_listing)

    return db_listing


def get_all_listings(db: Session):
    return db.query(Listing).all()


def get_listing_by_id(
    db: Session,
    listing_id
):
    return (
        db.query(Listing)
        .filter(Listing.id == listing_id)
        .first()
    )