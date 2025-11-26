    // JS to format the table
        const machines = ["Machine A", "Machine B", "Machine C"];

        const tableBody = document.getElementById("machine-table-body");

        machines.forEach(machineName => {
            // Creates a table row
            const row = document.createElement("tr");
            
            // Creates the name cell
            const nameCell = document.createElement("td");
            nameCell.textContent = machineName;
            
            // Creates the state cell with default IDLE
            const stateCell = document.createElement("td");
            stateCell.textContent = "IDLE";
            stateCell.style.backgroundColor = "yellow";
            
            // Converts "Machine A" to "machine-a" for the ID
            const machineId = machineName.toLowerCase().replace(" ", "-");
            stateCell.id = machineId + "-state";
            
            // Adding cells to row, row to table
            row.appendChild(nameCell);
            row.appendChild(stateCell);
            tableBody.appendChild(row);
        });

        // === JS to use the Websocket from Challange.py === //

        // Connecting to the Python server
        const socket = new WebSocket("ws://localhost:8765");
        
        // Setting the correct colours per state
        const stateColours = {
            "PRODUCING": "green",
            "IDLE": "yellow",
            "STARVED": "red"
        };

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data)

            // Building the cell ID from the machine name in the message
            const machineId = data.machine.toLowerCase().replace(" ", "-");
            const cellId = machineId + "-state";

            const stateCell = document.getElementById(cellId);

            stateCell.textContent = data.state;

            stateCell.style.backgroundColor = stateColours[data.state];
        };