var express = require('express');
var app = express();

app.get('/', function(req, res){
	console.log('主页GET请求');
	res.send('GET START');
})

app.post('/', function(req, res){
	console.log('主页POST请求');
	res.send('POST START');
})

app.get('del_user', function(req, res){
	console.log('del_user get请求');
	res.send('GET DEL_USER');
})

app.get('/list_user', function(req, res){
	console.log('show list');
	res.send('USER LIST');
})

app.get('/ab*cd', function(req, res){
	console.log('ab*cd GET请求');
	res.send('zhengzepipei');
})

var server = app.listen(8081, function(){
	var host = server.address().address
	var port = server.address().port
	console.log(server.address());
	console.log(port);
	console.log("access site: %s:%s", host, port);
})