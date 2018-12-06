const express = require('express');
const fs = require('fs');
const https = require('https');
const app = express();
const socketio = require('socket.io');

const server = https.createServer(
	{
		key: fs.readFileSync('./ssl/key.pem'),
		cert: fs.readFileSync('./ssl/cert.pem')
	},
	app
);

app.use(express.static('public'));

const io = socketio(server);
const words = ['apple', 'mom', 'dad', 'find', 'was', 'how'];

server.listen(3000, function() {
	console.log(
		'Example app listening on port 3000! Go to https://localhost:3000/'
	);
});

app.get('/', function(req, res) {
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket) {
	index = 0;
	socket.emit('spell', words[index]);
	index++;
	socket.on('nextWord', function(data) {
		//checkSpelling(data);
		socket.emit('spell', words[index]);
		index++;
		console.log(data);
	});
});
