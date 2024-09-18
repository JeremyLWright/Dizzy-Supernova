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

/**
 * sendMessage - The workhorse function for sending messages
 * 
 * This function retrieves the message from the input field,
 * sends it to the server via socket.io, and clears the input.
 * It's triggered when the user wants to send a message.
 */
function sendMessage() {
    const messageInput = $('#messageInput');
    const message = messageInput.val().trim();
    
    if (message) {
        // Emit the message to the server
        socket.emit("message", message);
        
        // Clear the input field after sending
        messageInput.val('');
    }
}