from sqlalchemy.orm import Session

from app.models.listing import Listing
from app.models.tenant_profile import TenantProfile

from app.services.rule_engine import calculate_rule_score

from app.ai.groq_matcher import rank_matches


def get_matching_listings(
    db: Session,
    user_id
):

    profile=(

        db.query(TenantProfile)

        .filter(
            TenantProfile.user_id==user_id
        )

        .first()

    )

    if not profile:

        return []

    listings=db.query(Listing).all()

    scored=[]

    for listing in listings:

        score,reasons=calculate_rule_score(

            profile,

            listing

        )

        scored.append({

            "listing":listing,

            "rule_score":score,

            "reasons":reasons

        })

    scored.sort(

        key=lambda x:x["rule_score"],

        reverse=True

    )

    top5=scored[:5]

    ai_response=rank_matches(

        profile,

        top5

    )

    final=[]

    ai_lookup={

        item["id"]:item

        for item in ai_response

    }

    for match in top5:

        listing=match["listing"]

        ai=ai_lookup.get(

            str(listing.id),

            {}

        )

        final.append({

            "listing":listing,

            "rule_score":match["rule_score"],

            "compatibility_score":ai.get(

                "compatibility_score",

                match["rule_score"]

            ),

            "summary":ai.get(

                "summary",

                "Good recommendation."

            ),

            "pros":ai.get(

                "pros",

                match["reasons"]

            ),

            "cons":ai.get(

                "cons",

                []

            )

        })

    final.sort(

        key=lambda x:x["compatibility_score"],

        reverse=True

    )

    return final