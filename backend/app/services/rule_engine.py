from app.models.tenant_profile import TenantProfile
from app.models.listing import Listing


def calculate_rule_score(
    profile: TenantProfile,
    listing: Listing
):

    score = 0

    reasons = []

    # Budget
    if listing.rent <= profile.budget:
        score += 25
        reasons.append("Budget fits")

    # Location
    if profile.preferred_location.lower() in listing.location.lower():
        score += 20
        reasons.append("Preferred location")

    # Food
    if listing.food_preference == profile.food_preference:
        score += 15
        reasons.append("Food preference matches")

    # Smoking
    if listing.smoking_allowed == profile.smoking:
        score += 10
        reasons.append("Smoking compatible")

    # Pets
    if listing.pets_allowed == profile.pets:
        score += 10
        reasons.append("Pet preference compatible")

    if listing.furnished:
        score += 5
        reasons.append("Furnished")

    if listing.wifi:
        score += 5
        reasons.append("WiFi")

    if listing.parking:
        score += 5
        reasons.append("Parking")

    if listing.ac:
        score += 5
        reasons.append("AC")

    return score, reasons