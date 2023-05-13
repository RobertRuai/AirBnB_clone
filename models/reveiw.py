from base_model import BaseModel

class Reveiw(BaseModel):
    """ Reveiw Class """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        