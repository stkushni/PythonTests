from models.ui.domain.customer.customer import Customer


class CustomerHarryPotter(Customer):
    name = "Harry"
    lastname = "Potter"
    postcode = "E725JB"
    account_default_id = 1004

    def __init__(self):
        super().__init__(self.name, self.lastname, self.postcode)
