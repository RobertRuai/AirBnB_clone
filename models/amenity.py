from base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity Class """

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        