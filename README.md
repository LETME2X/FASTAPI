# FastAPI WebSocket Chat Project

This project demonstrates a simple WebSocket chat application built using [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Overview

The chat application allows users to connect via WebSocket and exchange messages in real-time. Each user is identified by a unique user ID provided by the client.

## Features

- Real-time communication using WebSocket protocol.
- Allows multiple users to connect simultaneously.
- Simple user interface for sending and receiving messages.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LETME2X/FASTAPI.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

2. Open `index.html` in a web browser to access the chat interface.

3. Enter a user ID (e.g., user1, user2) and start sending messages.

## Project Structure

- `main.py`: Contains the FastAPI application code, including WebSocket endpoints.
- `index.html`: Simple HTML interface for the chat application.
- `README.md`: Documentation for the project.
- `requirements.txt`: List of Python dependencies.

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python.
- [WebSocket](https://websockets.readthedocs.io/en/stable/): WebSocket implementation for Python.
- [Python](https://www.python.org/): Programming language used for development.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
