from models import Property
from models import User

g=5
p=2000000579

john, jane, doe = User('a', 'a', 12345678), User(
    'Jane', 'jane', 87654321), User('Doe', 'doe', 23456789)
p1, p2, p3 = Property("Valmiki Bhavan", 10), Property(
    "Shankar Bhavan", 20), Property("Vyas Bhavan", 15)

john.reg_property(p1)
jane.reg_property(p2)
jane.reg_property(p3)

users = [john, jane, doe]
properties = [p1, p2, p3]
