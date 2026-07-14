from sqlalchemy.orm import Session

from app.models.listing import Listing


def search_listings(
    db: Session,

    location=None,

    min_rent=None,

    max_rent=None,

    property_type=None,

    food_preference=None,

    wifi=None,

    parking=None,

    ac=None
):

    query = db.query(Listing)

    if location:

        query = query.filter(
            Listing.location.ilike(f"%{location}%")
        )

    if min_rent is not None:

        query = query.filter(
            Listing.rent >= min_rent
        )

    if max_rent is not None:

        query = query.filter(
            Listing.rent <= max_rent
        )

    if property_type:

        query = query.filter(
            Listing.property_type == property_type
        )

    if food_preference:

        query = query.filter(
            Listing.food_preference == food_preference
        )

    if wifi is not None:

        query = query.filter(
            Listing.wifi == wifi
        )

    if parking is not None:

        query = query.filter(
            Listing.parking == parking
        )

    if ac is not None:

        query = query.filter(
            Listing.ac == ac
        )

    return query.all()