# FastAPI_WebSocket_Toggle
This is a simple example of a FastAPI application that demonstrates WebSocket communication with a toggle action. The application serves static files and includes a WebSocket endpoint to handle toggling.

## Features

- WebSocket communication for toggling a state.
- Serving static HTML content.
- Basic example of FastAPI usage.

## Getting Started

1. Clone the repository:

   ```bash
    git clone https://github.com/gitofsajeed/fastapi-websocket-toggle.git
   cd fastapi-websocket-toggle

2. Install dependencies:
    ```bash 
    pip install -r requirements.txt

3. Run the FastAPI application:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
4. Access the application in your web browser:

      Open http://localhost:8000 in your web browser to interact with the example.
   
## Usage

- Open the application in your web browser and you should see the initial state as "OFF".
- Open the browser's developer console and use the WebSocket connection to send a "toggle" message to change the state.
- The application will respond to toggle messages and confirm the toggle action.

## Folder Structure

- main.py: Contains the FastAPI application and WebSocket endpoint logic.
- static/: Directory for static files, including index.html.
- static/index.html: HTML template with placeholder for the state.

## Contributing

  Contributions are welcome! Feel free to open issues or submit pull requests if you have any improvements or suggestions.
