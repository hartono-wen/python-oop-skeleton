class department:

    def __init__(self, id, name, floor):  
        self.id = id
        self.name = name
        self.floor = floor
    
    def save(self):
        # This is only a display as if something is saved to the db.
        print ("Data is saved. ID: %s. Name is: %s. Floor is: %d" % (self.id, self.name, self.floor))
