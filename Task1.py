class Subject:
    def __init__(self):
        self.state = None
        self._observers = []  # List to hold observer references
    
    def setState(self, state):
        # Setting the state, then notify observers
        self.state = state
        self.notifyAllObservers()
    
    def attach(self, observer):
        # Add an observer to the list
        self._observers.append(observer)
    
    def notifyAllObservers(self):
        for observer in self._observers:
            observer.update(self.state, self.name)


class Machine(Subject):
    def __init__(self, name):
        super().__init__()  # Call parent's __init__
        self.name = name


class Observer:
    def __init__(self, name,):
        self.name = name

    def update(self, state, from_machine):
        pass

class Employee(Observer):
    def __init__(self, name, role): # Defiining the Emplyee Class
        super().__init__(name)
        self.role = role

    def update(self, state, from_machine): # The update function which returns a report string with all the required perameters passed
        print(f"Emplyee name: {self.name}, Role: {self.role}. Machine: {from_machine} has the STATE: {state}")


def main():

    machine1 = Machine("Assembly Arm")
    machine2 = Machine("Packing Machine")
    machine3 = Machine("Welding Machine")
    #Example machines

    employee1 = Employee("Cole", "Manager")
    employee2 = Employee("Reece", "Technician")
    employee3 = Employee("Levi", "Team Player")
    #Example Employees

    machine1.attach(employee1)
    machine2.attach(employee2)
    machine3.attach(employee3)
    # Using the attach methid to assign employees to a machine

    machine1.setState("PRODUCING")
    machine2.setState("PRODUCING")
    machine3.setState("PRODUCING")

    return

if __name__ == "__main__":
    main()