from models import storage

class State(BaseModel, Base):
    # Existing code

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter method to return the list of City objects from storage
            linked to the current State
            """
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

