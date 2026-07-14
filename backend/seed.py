import random
from datetime import date, timedelta

from faker import Faker

from app.database.connection import engine
from app.database.session import SessionLocal
from app.database.base import Base

import app.models

from app.auth.hashing import hash_password

from app.models.user import User
from app.models.owner_profile import OwnerProfile
from app.models.tenant_profile import TenantProfile
from app.models.listing import Listing
from app.models.interest import Interest
from app.models.message import Message

from app.models.enums import (
    UserRole,
    PropertyType,
    FoodPreference,
    GenderPreference,
    InterestStatus
)

fake = Faker("en_IN")

db = SessionLocal()

PASSWORD = "Password@123"

print("=" * 50)
print("STARTING DATABASE SEEDING")
print("=" * 50)

owners = []
tenants = []
listings = []

locations = [
    "Baner",
    "Hinjewadi",
    "Wakad",
    "Kothrud",
    "Shivajinagar",
    "Hadapsar",
    "Viman Nagar",
    "Kharadi",
    "Pimple Saudagar",
    "Aundh"
]

occupations = [
    "Software Engineer",
    "Data Scientist",
    "Student",
    "Doctor",
    "Teacher",
    "Designer",
    "Business Analyst",
    "Product Manager"
]

hobbies = [
    "Cricket",
    "Football",
    "Gym",
    "Music",
    "Cooking",
    "Movies",
    "Reading",
    "Gaming",
    "Photography",
    "Travelling"
]

languages = [
    "English",
    "Hindi",
    "Marathi",
    "English,Hindi",
    "English,Marathi",
    "Hindi,Marathi",
    "English,Hindi,Marathi"
]
print("Creating Owners...")

for i in range(20):

    owner = User(
        email=f"owner{i+1}@gmail.com",
        password=hash_password(PASSWORD),
        role=UserRole.OWNER,
        is_active=True
    )

    db.add(owner)

    owners.append(owner)

db.commit()

for owner in owners:
    db.refresh(owner)

print("20 Owners Created")
print("Creating Owner Profiles...")

for owner in owners:

    profile = OwnerProfile(

        user_id=owner.id,

        full_name=fake.name(),

        phone=fake.msisdn()[:20],

        property_name=f"{fake.last_name()} Residency",

        property_address=fake.address()[:240]

    )

    db.add(profile)

db.commit()

print("Owner Profiles Created")
print("Creating Tenants...")

for i in range(100):

    tenant = User(

        email=f"tenant{i+1}@gmail.com",

        password=hash_password(PASSWORD),

        role=UserRole.TENANT,

        is_active=True

    )

    db.add(tenant)

    tenants.append(tenant)

db.commit()

for tenant in tenants:
    db.refresh(tenant)

print("100 Tenants Created")
print("Creating Tenant Profiles...")

for tenant in tenants:

    profile = TenantProfile(

        user_id=tenant.id,

        full_name=fake.name(),

        age=random.randint(18,35),

        occupation=random.choice(occupations),

        budget=random.randint(7000,30000),

        preferred_location=random.choice(locations),

        bio=fake.sentence(),

        food_preference=random.choice(list(FoodPreference)),

        smoking=random.choice([True,False]),

        drinking=random.choice([True,False]),

        pets=random.choice([True,False]),

        cleanliness=random.randint(1,10),

        sleep_schedule=random.choice(
            [
                "Early",
                "Late"
            ]
        ),

        work_mode=random.choice(
            [
                "WFH",
                "Office",
                "Hybrid"
            ]
        ),

        languages=random.choice(languages),

        hobbies=", ".join(
            random.sample(
                hobbies,
                3
            )
        )

    )

    db.add(profile)

db.commit()

print("Tenant Profiles Created")
print("PART 1 COMPLETED")
print("Creating Listings...")

listing_titles = [
    "Spacious PG",
    "Luxury Apartment",
    "Affordable Flat",
    "Cozy Studio",
    "Modern Villa",
    "Student Friendly PG",
    "Fully Furnished Apartment",
    "Premium Flat",
    "Budget Room",
    "Family Apartment"
]

descriptions = [
    "Near Metro Station",
    "24x7 Water Supply",
    "Excellent Ventilation",
    "Walking distance from IT Park",
    "Peaceful Society",
    "New Construction",
    "Near Market",
    "Near College",
    "Prime Location",
    "Gated Community"
]

for _ in range(50):

    owner = random.choice(owners)

    listing = Listing(

        owner_id=owner.id,

        title=random.choice(listing_titles),

        description=random.choice(descriptions),

        rent=random.randint(7000,30000),

        deposit=random.randint(10000,60000),

        location=random.choice(locations),

        property_type=random.choice(list(PropertyType)),

        occupancy=random.randint(1,4),

        available_from=date.today()+timedelta(days=random.randint(1,30)),

        furnished=random.choice([True,False]),

        parking=random.choice([True,False]),

        wifi=random.choice([True,False]),

        ac=random.choice([True,False]),

        washing_machine=random.choice([True,False]),

        gender_preference=random.choice(list(GenderPreference)),

        food_preference=random.choice(list(FoodPreference)),

        smoking_allowed=random.choice([True,False]),

        drinking_allowed=random.choice([True,False]),

        pets_allowed=random.choice([True,False])

    )

    db.add(listing)

    listings.append(listing)

db.commit()

for listing in listings:
    db.refresh(listing)

print("50 Listings Created")
print("Creating Interests...")

used_pairs = set()

count = 0

while count < 150:

    tenant = random.choice(tenants)

    listing = random.choice(listings)

    pair = (tenant.id, listing.id)

    if pair in used_pairs:
        continue

    used_pairs.add(pair)

    interest = Interest(

        tenant_id=tenant.id,

        listing_id=listing.id,

        status=random.choice(list(InterestStatus))

    )

    db.add(interest)

    count += 1

db.commit()

print("150 Interests Created")
print("Creating Messages...")

chat_messages = [

    "Hi, is this property still available?",

    "Can I visit tomorrow?",

    "Is parking available?",

    "Is WiFi included?",

    "Can we negotiate the rent?",

    "What is the deposit?",

    "Looks good.",

    "Interested in the property.",

    "Please share location.",

    "Thank you."

]

for _ in range(300):

    tenant = random.choice(tenants)

    listing = random.choice(listings)

    owner = next(
        o for o in owners
        if o.id == listing.owner_id
    )

    if random.choice([True,False]):

        sender = tenant.id
        receiver = owner.id

    else:

        sender = owner.id
        receiver = tenant.id

    message = Message(

        sender_id=sender,

        receiver_id=receiver,

        content=random.choice(chat_messages)

    )

    db.add(message)

db.commit()

print("300 Messages Created")
print()

print("="*60)

print("DATABASE SEEDED SUCCESSFULLY")

print("="*60)

print("Owners          :", len(owners))

print("Tenants         :", len(tenants))

print("Listings        :", len(listings))

print("Interests       : 150")

print("Messages        : 300")

print()

print("Login Credentials")

print("----------------------------")

print("Owner")

print("Email : owner1@gmail.com")

print("Password : Password@123")

print()

print("Tenant")

print("Email : tenant1@gmail.com")

print("Password : Password@123")

print("="*60)

db.close()