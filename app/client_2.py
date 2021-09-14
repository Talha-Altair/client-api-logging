from faker import Faker

fake = Faker()

def get_details():

    name = fake.name()

    return name