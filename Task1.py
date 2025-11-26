import random
from enum import Enum

class MachineState(Enum):
    PRODUCING = "PRODUCING"
    IDLE = "IDLE"
    STARVED = "STARVED"

class Subject:
    def __init__(self):
        self.state = None
        self._observers = []  # List to hold observer references
    
    def setState(self, state):
        # To prevent invalid states from being used
        if not isinstance(state, MachineState):
            raise ValueError(f"Invalid state: {state}. Must be a MachineState.")

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
        super().__init__()
        self.name = name
        self.state = random.choice(list(MachineState))  # Random initial state

    def startProduction(self):
        self.setState(MachineState.PRODUCING)

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
        print(f"Employee name: {self.name}, Role: {self.role}. Machine: {from_machine} has the STATE: {state}")


def main():
    # Create machines (they start in random states)
    machine1 = Machine("Assembly Arm")
    machine2 = Machine("Packing Machine")
    machine3 = Machine("Welding Machine")

    # Show initial random states
    print("=== Initial States (before observers attached) ===")
    print(f"{machine1.name}: {machine1.state}")
    print(f"{machine2.name}: {machine2.state}")
    print(f"{machine3.name}: {machine3.state}")

    # Create employees
    employee1 = Employee("Cole", "Manager")
    employee2 = Employee("Reece", "Technician")
    employee3 = Employee("Levi", "Team Player")

    # Attach observers
    machine1.attach(employee1)
    machine1.attach(employee2)
    machine2.attach(employee2)
    machine3.attach(employee3)

    # Start production - observers now get notified
    print("\n=== Starting Production ===")
    machine1.startProduction()
    machine2.startProduction()
    machine3.startProduction()

    return

if __name__ == "__main__":
    main()