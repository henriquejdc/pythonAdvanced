from abc import ABCMeta


class IDepartament(metaclass=ABCMeta):

    @staticmethod
    def __init__(self, employees):
        """ Implement in child class """

    @staticmethod
    def print_department():
        """ Implement in child class """


class Accounting(IDepartament):

    def __init__(self, employees):
        super().__init__(self, employees)
        self.employees = employees

    def print_department(self):
        print(f"Accounting Departament: {self.employees}")


class Development(IDepartament):

    def __init__(self, employees):
        super().__init__(self, employees)
        self.employees = employees

    def print_department(self):
        print(f"Development Departament: {self.employees}")


class ParentDepartament(IDepartament):

    def __init__(self, employees):
        super().__init__(self, employees)
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Departament Base Employees: {self.base_employees}")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Parent Departament Total Employees: {self.employees}")


class IPerson(metaclass=ABCMeta):

    @staticmethod
    def person_method():
        """ Interface Method """

    @staticmethod
    def print_data():
        """ Implement in child class """


class Person(IPerson):

    def person_method(self):
        print("I am a person!")


class Student(IPerson):

    def __init__(self):
        self.name = "Student"

    def person_method(self):
        print("I am a Student")


class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher"

    def person_method(self):
        print("I am a Teacher")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy funcionality!")
        self.person.person_method()


class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"

    @staticmethod
    def print_data():
        print(PersonSingleton.__instance)

    def person_method(self):
        print("I am a person singleton!")


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        elif person_type == 'Teacher':
            return Teacher()
        elif person_type == 'Person':
            return Person()
        elif person_type == 'Proxy':
            return ProxyPerson()
        elif person_type == 'Singleton':
            ps = PersonSingleton("Henrique", 25)
            # ps_error = PersonSingleton("Pedro", 55)  # Raise Exception
            ps.print_data()
            return ps
        print("Invalid Type")
        return -1


if __name__ == "__main__":
    # s1 = Student()
    # s1.person_method()
    #
    # t1 = Teacher()
    # t1.person_method()

    choice_main = input("Person or Departament?\n")
    if choice_main == 'Person':
        choice = input("What type of person to create?\n")
        person = PersonFactory.build_person(choice)
        person.person_method()
    elif choice_main == 'Departament':
        accounting = Accounting(200)
        accounting.print_department()

        development = Development(50)
        development.print_department()

        parent_dept = ParentDepartament(50)
        parent_dept.add(accounting)
        parent_dept.add(development)
        parent_dept.print_department()
    else:
        print("Invalid Type")
