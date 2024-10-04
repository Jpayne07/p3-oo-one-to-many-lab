class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner =""):
        self.name = name
        self.owner = owner
        if pet_type in __class__.PET_TYPES:
            self.pet_type = pet_type
        else: raise Exception('Sorry')

        __class__.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
   
    def pets(self):
        owner_pets=[]
        for pet in Pet.all:
            if pet.owner == self:
                owner_pets.append(pet)
                print(owner_pets)
                print(pet.owner)
        return owner_pets
            
    def add_pet(self, pet):
        if(type(pet) != Pet):
            raise Exception("not of object type pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda pet: pet.name)

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)
owner.get_sorted_pets()