var fs = require("fs");

console.log('Ready to open file');
fs.stat('input.txt',function(err,stats){
	if (err){
		return console.error(err);
	}
	console.log(stats);
	console.log('Read file succeed');
	console.log("isFile? "+ stats.isFile());
	console.log("isDirectory? "+ stats.isDirectory());
})

