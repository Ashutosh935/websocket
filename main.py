import asyncio
import websockets

async def handle_client(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

            # Echo the received message back to the client
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected")

async def main():
    server = await websockets.serve(handle_client, "localhost", 8000)
    print("WebSocket server is running...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
