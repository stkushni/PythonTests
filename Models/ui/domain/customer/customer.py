class Customer:
    name: str
    lastname: str
    account_default_id: int
    postcode: int

    def __init__(self, name, lastname, postcode, account_id):
        self.name = name
        self.lastname = lastname
        self.postcode = postcode
        self.account_default_id = account_id
