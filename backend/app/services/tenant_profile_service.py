from sqlalchemy.orm import Session

from app.models.tenant_profile import TenantProfile


def get_profile(db: Session, user_id):

    return (
        db.query(TenantProfile)
        .filter(TenantProfile.user_id == user_id)
        .first()
    )


def create_profile(
    db: Session,
    user_id,
    profile
):

    db_profile = TenantProfile(

        user_id=user_id,

        **profile.model_dump()

    )

    db.add(db_profile)

    db.commit()

    db.refresh(db_profile)

    return db_profile


def update_profile(
    db: Session,
    db_profile,
    profile
):

    for key, value in profile.model_dump().items():
        setattr(db_profile, key, value)

    db.commit()

    db.refresh(db_profile)

    return db_profile