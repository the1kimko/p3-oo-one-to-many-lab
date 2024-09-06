class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types are: {', '.join(Pet.PET_TYPES)}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = None # Default if no owner is provided

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)

        # Store every instance in the class variable `all`
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        
        self.name = name
        self._pets = []

    def pets(self):
        """Returns a list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's list of pets, after type checking."""
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        """Returns a sorted list of the owner's pets by their names."""
        return sorted(self._pets, key=lambda pet: pet.name)
        