from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.listing import Listing
from app.models.interest import Interest
from app.models.enums import InterestStatus


def get_owner_dashboard(
    db: Session,
    owner_id
):

    listings = db.query(Listing).filter(
        Listing.owner_id == owner_id
    ).all()

    listing_ids = [l.id for l in listings]

    total_listings = len(listings)

    if not listing_ids:

        return {
            "total_listings": 0,
            "pending_requests": 0,
            "accepted_requests": 0,
            "rejected_requests": 0,
            "total_requests": 0
        }

    pending = db.query(func.count(Interest.id)).filter(
        Interest.listing_id.in_(listing_ids),
        Interest.status == InterestStatus.PENDING
    ).scalar()

    accepted = db.query(func.count(Interest.id)).filter(
        Interest.listing_id.in_(listing_ids),
        Interest.status == InterestStatus.ACCEPTED
    ).scalar()

    rejected = db.query(func.count(Interest.id)).filter(
        Interest.listing_id.in_(listing_ids),
        Interest.status == InterestStatus.REJECTED
    ).scalar()

    total = db.query(func.count(Interest.id)).filter(
        Interest.listing_id.in_(listing_ids)
    ).scalar()

    recent_requests = (
    db.query(Interest)
    .filter(Interest.listing_id.in_(listing_ids))
    .order_by(Interest.created_at.desc())
    .limit(5)
    .all()
)

    return {

        "total_listings": total_listings,

        "pending_requests": pending,

        "accepted_requests": accepted,

        "rejected_requests": rejected,

        "total_requests": total
        
       

    }