class Person:
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    def email(self):
        return f'{self.fullname()}@gmail.com'.replace(' ', '')
    
    
    
p1=Person('ghazal','hafezi')
print(p1.email())
