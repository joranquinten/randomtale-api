const express = require('express');

const config = {
  server: {
    port: 3100
  }
}

let app = express();

const device = {
  platform: {
    connected: false,
    status: 'idle',
  },
  randomtale: {
    status: 'idle', // 'playing', 'sending', 'receiving'
    playlist: []
  }
}

app.get('/status', function(req, res) {
  res.json(device);
})

console.log(`Server is up and running at port ${config.server.port}!`);

app.listen(config.server.port);