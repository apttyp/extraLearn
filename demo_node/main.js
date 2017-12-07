console.log(__filename);
console.log(__dirname);


function printHello(){
	console.log('nihao');
}
setTimeout(printHello, 5000);



function printgg(){
   console.log( "Hello, World!");
}
// 两秒后执行以上函数
var t = setTimeout(printgg, 2000);

// 清除定时器
clearTimeout(t);

console.log('byvoid%diovyb', 1991); 