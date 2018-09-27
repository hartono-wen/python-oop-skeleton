class employee:

    def __init__(self, name, dob, gender, phone_number, email_address):  
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone_number = phone_number
        self.email_address = email_address
    
    def save(self):
        # This is only a display as if something is saved to the db.
        print ("Data is saved. Name: %s. Date of Birth is: %s. Gender is: %s. Phone Number is: %s. Email Address is: %s." %
        (self.name, self.dob, self.gender, self.phone_number, self.email_address))


