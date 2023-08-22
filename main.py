from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the static files directory
app.mount("/static/", StaticFiles(directory="static"), name="static")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "toggle":
            # Process the toggle action
            # You can send a response back to the client using `await websocket.send_text(response)`
            pass
            state = not state

            # Send a message back to the client to confirm that the toggle action was successful
            await websocket.send_text("Toggled!")


@app.get("/")
async def root():
    with open("/static/indexs.html") as file:
        content = file.read()
        return content.replace("%STATE%", "OFF")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
