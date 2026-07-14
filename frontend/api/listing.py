from api.client import (
    get,
    post,
    put,
    delete
)


# ==========================
# OWNER APIs
# ==========================

def get_my_listings(token):
    return get(
        "/listing/my",
        token
    )


def create_listing(token, data):
    return post(
        "/listing",
        data,
        token
    )


def update_listing(token, listing_id, data):
    return put(
        f"/listing/{listing_id}",
        data,
        token
    )


def delete_listing(token, listing_id):
    return delete(
        f"/listing/{listing_id}",
        token
    )


# ==========================
# TENANT APIs
# ==========================

def get_all_listings(token):
    return get(
        "/listing",
        token
    )


def get_listing_by_id(token, listing_id):
    return get(
        f"/listing/{listing_id}",
        token
    )


def search_listing(
    token,
    location="",
    min_rent=0,
    max_rent=100000,
    property_type=""
):

    endpoint = (
        f"/listing/search?"
        f"location={location}"
        f"&min_rent={min_rent}"
        f"&max_rent={max_rent}"
        f"&property_type={property_type}"
    )

    return get(
        endpoint,
        token
    )