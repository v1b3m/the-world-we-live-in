class Person:
    def __init__(self, age, sex, name):
        self.age = age
        self.sex = sex
        self.name = name

    def _repr__(self):
        return '<Person {}>'.format(self.name)  

class Developer(Person):

    def __init__(self, age, sex, name, language):
        super().__init__(age, sex, name)
        self.language = language
    

    def get_language(self):
        return self.language

    def __str__(self):
        return "%s is a %s developer" % (self.name, self.language)

    def speak(self):
        print("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.\n")

class Child(Person):

    def __init__(self, age, sex, name, parent, school):
        super().__init__(age, sex, name)
        self.__maxage = 12
        if self.age > self.__maxage: 
            print("Child cannot be older than 12. Setting age to 12")
            self.age = 12
        self.parent = parent
        self.school = school

    def get_school(self):
        return self.school

    def speak(self):
        print("momy bots me tedde aw kends ob pwesents todas!")

    def child_of(self):
        return "Child of " + self.parent

if __name__=='__main__':
    enoch = Developer(18, "male", "Enoch", "ruby on rails" )
    print(enoch.get_language())
    print(enoch)
    enoch.speak()

    amon = Child(4, "male", "Amon", "Betty", "Child's Paradise")
    print(amon.get_school())
    print(amon.child_of())
    amon.speak()
    
