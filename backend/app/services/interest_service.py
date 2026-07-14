from sqlalchemy.orm import Session

from app.models.interest import Interest

from app.models.enums import InterestStatus


def create_interest(
    db: Session,
    tenant_id,
    listing_id
):

    interest = Interest(

        tenant_id=tenant_id,

        listing_id=listing_id,

        status=InterestStatus.PENDING

    )

    db.add(interest)

    db.commit()

    db.refresh(interest)

    return interest


def get_tenant_interests(
    db: Session,
    tenant_id
):

    return (

        db.query(Interest)

        .filter(
            Interest.tenant_id == tenant_id
        )

        .all()

    )


def update_interest_status(
    db: Session,
    interest_id,
    status
):

    interest = (

        db.query(Interest)

        .filter(
            Interest.id == interest_id
        )

        .first()

    )

    if not interest:

        return None

    interest.status = status

    db.commit()

    db.refresh(interest)

    return interest