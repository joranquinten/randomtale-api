const express = require("express");
let app = express();
let server = require("http").createServer(app);
let io = require("socket.io")(server);

const config = {
  server: {
    port: 4400
  }
};

app.use(express.static(__dirname + "/client"));

app.get("/", function(req, res, next) {
  res.sendFile(__dirname + "/index.html");
});

console.log(`Server is up and running at port ${config.server.port}!`);

io.on("connection", function(client) {
  console.log("Client connected...");

  client.on("join", function(data) {
    console.log(data);
  });

  client.on("controls", function(data) {
    console.log(data);
    client.emit("broad", data);
    client.broadcast.emit("broad", data);
  });
});

server.listen(config.server.port);
