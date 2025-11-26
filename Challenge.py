import asyncio
import random
import json
from websockets.server import serve
from Task1 import MachineState, Subject, Machine, Observer

# === Dashboard Server Code === #

class Dashboard(Observer):
    def __init__(self, name):
        super().__init__(name)
        # Storeing a reference to the WebSocket connection
        self.websocket = None

    
    def update(self, state, from_machine):
        data = {"machine": from_machine, "state": state.value}
        # Converting Dictionary to json
        message = json.dumps(data)
        
        # Will olnly send data if there is a connection
        if self.websocket is not None:
            asyncio.create_task(self.websocket.send(message))
            # Schedules the websocket.send() to run asynchronously in the background without blocking the current code. This allows the synchronous notifyAllObservers() method to call this update() without needing to await it.


# === Global instances === #
machines = [
    Machine("Machine A"),
    Machine("Machine B"),
    Machine("Machine C")
]
dashboard = Dashboard("Main Dashboard")

for machine in machines:
    machine.attach(dashboard)

# === Websocket Server Code === #

async def handler(websocket):
    # This function runs when a browser connects
    dashboard.websocket = websocket
    
    # Random state change loop for each machine
    while True:
        # Picks random machine from the list
        random_machine = random.choice(machines)
        
        # Picks random state
        random_state = random.choice(list(MachineState))
        
        # Changes the state, this triggers dashboard.update()
        random_machine.setState(random_state)
        
        # Waits 2-10 seconds before next change
        await asyncio.sleep(random.uniform(2, 10))

async def main():
    # Stating the WebSocket server on localhost, port 8765
    async with serve(handler, "localhost", 8765):
        await asyncio.Future()  # Keeps the server running forever

if __name__ == "__main__":
    asyncio.run(main())