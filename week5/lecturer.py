from person import Person

class lecturert(Person):
    def __init__(self, name, staff_id, tax_num, rate_of_pay, publications):
        super().__init__(name)
        self.staff_id = staff_id
        self.publications = publications

    def number_of_publication(self):

        
        return self



publication = lecturert.number_of_publication(10)


print("Number Of publication:",publication )
