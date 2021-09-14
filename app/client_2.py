from faker import Faker

fake = Faker()

def get_details():

    name = fake.name()

    data = {
            "name" : name
        }

    print(data)

    return data