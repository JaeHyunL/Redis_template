import datetime

from redis_om import HashModel, Field, Migrator
from pydantic import ValidationError
from typing import Optional


class Customer(HashModel):
    first_name: str
    last_name: str = Field(index=True)
    email: str
    join_date: datetime.date
    age: int = Field(index=True)
    bio: Optional[str] = "Super dope"  # <- We added a default here


andrew = Customer(
    first_name="Andrew",
    last_name="Brookins",
    email="andrew.brookins@example.com",
    join_date=datetime.date.today(),
    age=38,
)  # <- Notice, we didn't give a bio!

print(andrew.pk)
andrew.save()

joon = Customer(
    first_name="Joon",
    last_name="Lee",
    email="joon.lee@example.com",
    join_date=datetime.date.today(),
    age=40,
)

joon.save()

Migrator().run()  # 스키마를 저장하기 위해서 마이그레이터 실행.

# Find all customers with the last name "Brookins"
print(Customer.find(Customer.last_name == "Brookins").all())
print(Customer.find(Customer.last_name != "Brookins").all())
print(
    Customer.find(
        (Customer.last_name == "Brookins")
        | (Customer.age == 100) & (Customer.last_name == "Smith")
    ).all()
)
