from api.client import get


def get_my_matches(token):

    return get(
        "/matching/my-matches",
        token
    )


def get_listing_matches(token, listing_id):

    return get(
        f"/matching/listing/{listing_id}",
        token
    )