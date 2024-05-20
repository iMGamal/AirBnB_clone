"""This is a module for class Company."""


class Company:
    """This is class of the project."""

    def __init__(self, employee, salary):
        """CLASS constructor."""
        self.employee = employee
        self.salary = salary

    def __str__(self):
        """RETURN string."""
        return f"Employee : {self.employee} - Salary : {self.salary}"


Agent0 = Company("Alex", 10000)
print(Agent0)

