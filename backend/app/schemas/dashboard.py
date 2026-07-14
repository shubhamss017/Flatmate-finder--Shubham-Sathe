from pydantic import BaseModel


class OwnerDashboard(BaseModel):

    total_listings: int

    pending_requests: int

    accepted_requests: int

    rejected_requests: int

    total_requests: int