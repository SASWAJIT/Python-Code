class Employee:
    def __init__(self,name,salary) -> None:
        self.name = name
        self.salary =salary
    def getsalary(self):
        return self.salary
rohan=Employee("Rohan", "5000")
print(rohan.salary)
print(rohan.name)