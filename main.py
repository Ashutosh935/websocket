from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio

import uvicorn

app = FastAPI()


@app.get("/")
async def get():
    return {'response': 'hi'}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            #query=eval(data)['content']


            await websocket.send_text(data)


    except WebSocketDisconnect:
        pass


async def astream_log():
    for i in range(5):
        yield f"Result {i}"


@app.websocket("/ws2")
async def websocket_endpoint2(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            print('################',data)
            query=eval(data)['content']
            async for result in astream_log():
               
                await websocket.send_text(result)
                await asyncio.sleep(1)

    except WebSocketDisconnect:
        print("WebSocket disconnected")
        await websocket.close()


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
