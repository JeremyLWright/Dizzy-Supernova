const socket = io("ws://localhost:8000", {transports: ["websocket"]});


socket.on("connect", () => {
  console.log("Connected to server");
});

socket.on("disconnect", () => {
  console.log("Disconnected from server");
});

socket.on("message", (message) => {
  console.log("Received message:", message);
});

socket.on("error", (error) => {
  console.error("Socket error:", error);
});

socket.on("connect_error", (error) => {
  console.log("Received message:", error);
});

socket.on("response",  (data) => {
  console.log("Received response",data);
  $(data+'<br/>').appendTo('#messages');
});


function sendMessage() {
  console.log($('#messageInput').val());
  socket.emit("message", $('#messageInput').val());
}