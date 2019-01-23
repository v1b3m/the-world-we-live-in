class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name

    def _repr__(self):
        return '<Person {}>'.format(self.name)  

class Developer(Person):

    def __init__(self, age, sex, name, language):
        Person.__init__(self, age, sex, name)
        self.language = language
    

    def get_language(self):
        return self.language

class Child(Person):
    def __init__(self, age, sex, name, parent, school):
        Person.__init__(self, age, sex, name) 
        self.parent = parent
        self.school = school

    def get_school(self):
        return self.school

    def child_of(self):
        return "Child of " + self.parent

if __name__=='__main__':
    enoch = Developer(18, "male", "Enoch", "ruby on rails" )
    print(enoch.get_language())

    amon = Child(4, "male", "Amon", "Betty", "Child's Paradise")
    print(amon.get_school())
    print(amon.child_of())
    
