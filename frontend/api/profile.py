from api.client import (
    get,
    put
)


def get_profile(token):

    return get(
        "/profile/me",
        token
    )


def update_profile(
    token,
    data
):

    return put(
        "/profile/me",
        data,
        token
    )