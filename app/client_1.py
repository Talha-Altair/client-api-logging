from faker import Faker

fake = Faker()

def get_details():

    country = fake.country()

    data = {
            "country" : country
        }

    print(data)

    return data