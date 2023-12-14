class PersonPrinter:

    people = []

    def __init__(self,people):
        self.people = people

    def run(self):
        i = 0 
        for person in self.people:
            print (f"{person.get_full_name()} ({person.sex})")
      
