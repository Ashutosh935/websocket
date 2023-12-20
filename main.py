from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
import json
import websockets
import uvicorn

# app = FastAPI()


# @app.get("/")
# async def get():
#     return {'response': 'hi'}


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             data = await websocket.receive_text()
#             #query=eval(data)['content']


#             await websocket.send_text(data)


#     except WebSocketDisconnect:
#         pass



# @app.websocket("/ws2")
# async def websocket_endpoint2(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             data = await websocket.receive_text()
#             print('################',data)
#             query=eval(data)['content']
#             async for result in astream_log():
               
#                 await websocket.send_text(result)
#                 await asyncio.sleep(1)

#     except WebSocketDisconnect:
#         print("WebSocket disconnected")
#         await websocket.close()


# if __name__ == '__main__':
#     uvicorn.run(app, port=8080, host='0.0.0.0')

async def astream_log():
    for i in range(5):
        yield f"Result {i}"

async def websocket_handler(websocket,path):
    await websocket.send("Connection established. Send data.")
    try:
        data = await websocket.recv()
    
        for value in range(5):
              
            try:
                print(value, end='#')
                await websocket.send(value)
                await asyncio.sleep(0.2)
            except Exception as e:
                print(f"Error processing data: {e}")
    except websockets.exceptions.ConnectionClosed:
        print("WebSocket disconnected")

if __name__ == '__main__':
    start_server = websockets.serve(
        websocket_handler, "0.0.0.0", 8080
    )

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
