//流中读取数据
// var fs = require("fs");
// var data = '';

// // 创建可读流
// var readerStream = fs.createReadStream('input.txt');

// // 设置编码为 utf8。
// readerStream.setEncoding('UTF8');

// // 处理流事件 --> data, end, and error
// readerStream.on('data', function(chunk) {
//    data += chunk;
// });

// readerStream.on('end',function(){
//    console.log(data);
//    console.log("read success");
// });

// readerStream.on('error', function(err){
//    console.log(err.stack);
// });

// console.log("程序执行完毕");



//写入流
// var fs = require('fs');
// var data1 = '菜鸟教程官网地址：www.runoob.com';
// var writeStream = fs.createWriteStream('output.txt');
// writeStream.write(data1,'utf8');
// writeStream.end();

// writeStream.on('finish',function(){
// 	console.log('写入完成');
// });

// writeStream.on('error',function(error){
// 	console.log(error.stack);
// });



//管道流
var fs = require("fs");
var readStream = fs.createReadStream('input1.txt');
var writeStream = fs.createWriteStream('output1.txt');
readStream.pipe(writeStream);
console.log('end');



//链式流 
var fs = require("fs");
var zlib = require('zlib');

// 压缩 input.txt 文件为 input.txt.gz
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));
console.log("文件压缩完成。");



//链式流
var fs1 = require("fs");
var zlib1 = require('zlib');

// 解压 input.txt.gz 文件为 input.txt
fs1.createReadStream('input.txt.gz')
  .pipe(zlib1.createGunzip())
  .pipe(fs1.createWriteStream('input.txt'));
  
console.log("文件解压完成。");