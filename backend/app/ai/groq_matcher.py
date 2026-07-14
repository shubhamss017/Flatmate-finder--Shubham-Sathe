import json

from app.core.groq_client import client


def rank_matches(
    tenant,
    matches
):

    listings=[]

    for match in matches:

        listing=match["listing"]

        listings.append({

            "id":str(listing.id),

            "title":listing.title,

            "rent":listing.rent,

            "location":listing.location,

            "food":listing.food_preference.value,

            "wifi":listing.wifi,

            "parking":listing.parking,

            "rule_score":match["rule_score"]

        })

    prompt=f"""
You are an expert roommate recommendation engine.

Tenant:

Budget: {tenant.budget}

Location: {tenant.preferred_location}

Food: {tenant.food_preference.value}

Smoking: {tenant.smoking}

Pets: {tenant.pets}

Rank these listings.

Return ONLY JSON.

[
{{
"id":"",
"compatibility_score":0,
"summary":"",
"pros":["","",""],
"cons":["",""]
}}
]

Listings:

{json.dumps(listings)}
"""

    response=client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.2,

        response_format={
            "type":"json_object"
        },

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )

    return json.loads(
        response.choices[0].message.content
    )