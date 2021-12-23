const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const io = require("socket.io")(server, {
  cors: {
    origin: "*:*"
  }
});
app.use(express.static('./public'));

io.on('connection', (socket) => {
    //testing
    console.log("Connect "+String(socket.id))
    socket.on('run', (msg) => {
        if(msg!=[''])
        {
        console.log("msg:"+msg);
      cmdline(`python middleman.py "${msg}"`);
        }
    });

    function cmdline(command){
      const exec = require('child_process').exec;
      exec(`${command}`, { encoding: 'utf-8' }, (error, stdout, stderr) => {
        if (error) {
          console.error(`exec error: ${error}, ${stderr}`);
          io.to(socket.id).emit("subprocess_out","Error");
        }else{
        console.log("stdout:"+stdout);
        io.to(socket.id).emit("subprocess_out","Success");
        }
      });
    }
});

server.listen(3000, () => {
    console.log('listening on *:3000');
  });