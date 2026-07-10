from enum import Enum

class UserRole(str, Enum):
    TENANT = "tenant"
    OWNER = "owner"
    ADMIN = "admin"