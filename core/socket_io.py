import socketio

# This is our broadcast socket connection
# It allows for real-time, bidirectional communication between the server and clients
# The AsyncServer is used for asynchronous operations, improving scalability
# CORS is allowed from all origins for development purposes, but should be restricted in production
sio = socketio.AsyncServer(
  async_mode="asgi", 
  cors_allowed_origins="*"
  # If your deployment uses multiple servers (horizontally)
  # use a message queue and attach it here to client_manager
  )