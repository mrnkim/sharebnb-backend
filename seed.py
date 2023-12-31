"""Seed database with sample data"""

from app import app
from models import  db, Listing, User, Message, Booking

db.drop_all()
db.create_all()

u1 = User(
    username="nonhostuser",
    first_name="nonhost",
    last_name="non",
    email="email@email.com",
    password="password",
    is_host=False
)

h1 = User(
    username="hostuser",
    first_name="host",
    last_name="yes",
    email="email1234@email.com",
    password="password",
    is_host=True
)

l1 = Listing(
    title="title",
    details="details",
    street="streetname",
    city="cityname",
    state="CA",
    zip=12345,
    country="USA",
    price_per_night=10,
    image_url="https://www.keywestnavalhousing.com/media/com_posthousing/images/nophoto.png",
    username="hostuser"
)

b1 = Booking(
    id=1,
    username="testuser",
    property_id=1,
    check_in_date="2008-11-09 15:45:21",
    check_out_date="2008-11-11 11:12:01",
    booking_price_per_night=9,
)

m1 = Message(
    id=1,
    from_username="nonhostuser",
    property_id=1,
    body="body of message",
    sent_at_date = "2008-11-12 11:12:01"
)

db.session.add_all([u1,h1])
db.session.commit()
db.session.add_all([l1])
db.session.commit()
db.session.add_all([m1])
db.session.commit()

