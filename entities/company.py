class company:

    def __init__(self, id, name, office_address, formed_date):
        self.id = id
        self.name = name
        self.office_address = office_address
        self.formed_date = formed_date
    
    def save(self):
        # This is only a display as if something is saved to the db.
        print ("Data is saved. Name: %s. Office Addresss is: %d. Formed at: %s" %
        (self.name, self.office_address, self.formed_date))


