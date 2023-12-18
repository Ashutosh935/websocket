from fastapi import FastAPI, WebSocket, WebSocketDisconnect

import uvicorn


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            query=eval(data)['content']
            
            
            await websocket.send_text(query)
           
               
    except WebSocketDisconnect:
        pass

if __name__ == '__main__':
    uvicorn.run(app, port = 8080, host = '0.0.0.0') 
