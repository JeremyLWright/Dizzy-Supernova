from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_utils.timing import add_timing_middleware, record_timing
import socketio
from core.socket_io import sio
from routes.ws_no_prefix import NoPrefixNamespace
from db.connections import connect, close
from db.mongodb import get_database, AsyncIOMotorClient
from fastapi import Depends
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
add_timing_middleware(app, record=logger.info, prefix="app", exclude="untimed")
logger = logging.getLogger(__name__)

sio.register_namespace(NoPrefixNamespace("/"))
sio_asgi_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)

app.add_route("/socket.io/", route=sio_asgi_app, methods=["GET", "POST", "OPTIONS"])
app.add_websocket_route("/socket.io/", route=sio_asgi_app)

app.add_event_handler("startup", connect)
app.add_event_handler("shutdown", close)

@app.get("/hello")
async def hello(
  db: AsyncIOMotorClient = Depends(get_database)
):
  logging.warning(f'Writing to db')
  doc = {
  "_id": 2,
  "name": {
    "first" : "Mohamed",
    "last" :"Hosam"
  },
  }
  r = await db.test_collection.insert_one(doc)
  logging.warning(f'Done')
  return {"message": "Hello World"}

@app.get("/")
async def root(
  request: Request,
  db: AsyncIOMotorClient = Depends(get_database)
):
  logging.warning(f'I got a database {db}')
  record_timing(request, note="Database start")
  d = await db.test_collection.find_one({"_id": 1} )
  record_timing(request, note="Database done")
  return {"message": d}

app.mount("/static", StaticFiles(directory="static"), name="static")