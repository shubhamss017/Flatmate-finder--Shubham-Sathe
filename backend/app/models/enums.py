from enum import Enum

class UserRole(str, Enum):
    TENANT = "tenant"
    OWNER = "owner"
    ADMIN = "admin"

class PropertyType(str, Enum):
    APARTMENT = "apartment"
    PG = "pg"
    VILLA = "villa"


class FoodPreference(str, Enum):
    VEG = "veg"
    NON_VEG = "non_veg"
    VEGAN = "vegan"


class GenderPreference(str, Enum):
    MALE = "male"
    FEMALE = "female"
    ANY = "any"