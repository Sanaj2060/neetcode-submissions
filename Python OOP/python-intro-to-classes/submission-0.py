class Pet:
    def __init__(obj, name: str, species: str):
        obj.name = name
        obj.species = species

# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
