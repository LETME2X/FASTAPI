from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Dictionary to store connected WebSocket clients
connected_users = {}

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handler for root path "/"
@app.get("/")
async def read_root():
    return {"message": "Welcome to the WebSocket server!"}

# WebSocket endpoint
@app.websocket("/ws/{user_id}")
async def websocket_endpoint(user_id: str, websocket: WebSocket):
    await websocket.accept()

    # Store the WebSocket connection in the dictionary
    connected_users[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            # Send the received data to the other user
            for user, user_ws in connected_users.items():
                if user != user_id:
                    await user_ws.send_text(data)
    except WebSocketDisconnect:
        # If a user disconnects, remove them from the dictionary
        del connected_users[user_id]
