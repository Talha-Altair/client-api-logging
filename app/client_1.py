from faker import Faker

fake = Faker()

def get_details():

    country = fake.country()

    return country