import socketio
from core.socket_io import sio

class NoPrefixNamespace(socketio.AsyncNamespace):
    async def on_connect(self, sid, environ):
        print(f"Client {sid} connected")

    async def on_disconnect(self, sid):
        print(f"Client {sid} disconnected")

    async def on_message(self, sid, data):
      await sio.emit("response", f"<b>{sid}</b>: <i>{data}</i>")
      print(f"Client {sid} sent message: {data}")


  