# Sony UK TEC - Software Engineer Coding Challenge

**Author:** Oliver Owens

## Overview

This project demonstrates the Observer design pattern applied to a production line monitoring system. Machines can be in one of three states (PRODUCING, IDLE, STARVED), and observers are notified when states change.

## Project Structure
```
├── Task1.py          # Core Observer pattern implementation
├── Challenge.py      # WebSocket server for real-time updates
├── README.md
└── frontend/
    ├── dashboard.html    # Frontend dashboard
    └── dashboard.js      # JavaScript for WebSocket handling
```

## Requirements

- Python 3.x
- websockets library

## Installation
```bash
pip install websockets
```

## Running Task 1 (Observer Pattern Demo)
```bash
python Task1.py
```

This demonstrates the Observer pattern with Employees receiving notifications when Machine states change.

## Running the Challenge (Real-Time Dashboard)

1. Start the WebSocket server:
```bash
python Challenge.py
```

2. Open `frontend/dashboard.html` in a web browser

3. Watch the machine states update in real-time with colour-coded status:
   - Green: PRODUCING
   - Yellow: IDLE
   - Red: STARVED

## Technologies Used

- Python (Object-Oriented Programming, asyncio, websockets)
- HTML/CSS/JavaScript (Vanilla)
- WebSocket protocol for real-time communication