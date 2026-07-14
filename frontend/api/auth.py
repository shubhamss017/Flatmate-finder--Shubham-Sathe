from api.client import post


def register(data):

    return post(

        "/auth/register",

        data

    )


def login(data):

    return post(

        "/auth/login",

        data

    )