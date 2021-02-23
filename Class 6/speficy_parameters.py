def describe_pet(pet_name = "Spot", animal_type = "dog"):
    print("Pet name is " + pet_name)
    print("Animal type is " + animal_type)

describe_pet("Jack")
describe_pet("Jack", "Cat")

# How to just specify the animal type?

describe_pet(animal_type="Fish")