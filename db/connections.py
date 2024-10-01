
import logging
import os

from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db

async def connect():
  MONGODB_URL = os.environ.get('MONGODB_URL')
  logging.warning("Connecting to Mongo")
  db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                  maxPoolSize=100,
                                  minPoolSize=10)
  logging.warning("Connection Success！")


async def close():
  logging.warning("Disconnecting from Mongo...")
  db.client.close()
  logging.warning("Disconnected！")