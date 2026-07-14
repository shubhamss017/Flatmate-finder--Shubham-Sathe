from api.client import (
    get,
    post,
    put
)


def send_interest(token, listing_id):

    return post(
        "/interest",
        {
            "listing_id": listing_id
        },
        token
    )


def received_interest(token):

    return get(
        "/interest/received",
        token
    )


def sent_interest(token):

    return get(
        "/interest/sent",
        token
    )


def accept_interest(token, interest_id):

    return put(
        f"/interest/{interest_id}/accept",
        {},
        token
    )


def reject_interest(token, interest_id):

    return put(
        f"/interest/{interest_id}/reject",
        {},
        token
    )