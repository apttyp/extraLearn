var events = require('events');
var eventEmitter = new events.EventEmitter();

var connectHandler = function connected(){
	console.log('connect success');
	eventEmitter.emit('data_received');
}
eventEmitter.on('connection',connectHandler);
eventEmitter.on('data_received',function(){
	console.log('date receive succeed');
});
eventEmitter.emit('connection');
console.log('end');

var events = require('events'); 
var emitter = new events.EventEmitter(); 
emitter.on('someEvent', function(arg1, arg2) { 
    console.log('listener1', arg1, arg2); 
}); 
emitter.on('someEvent', function(arg1, arg2) { 
    console.log('listener2', arg1, arg2); 
}); 
emitter.emit('someEvent', 'arg1 参数', 'arg2 参数'); 