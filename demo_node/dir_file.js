var fs = require("fs");


console.log("查看目录");
fs.readdir('rout',function(err,files){
   if (err){
      return console.error(err);
   }
   files.forEach(function(file){
      console.log(file);
   });
});

var ss = new Date();
console.log(ss.getTime());
// fs.open('input.txt', 'r+', function(err, fd) {
//    if (err) {
//        return console.error(err);
//    }
//    console.log("文件打开成功！");
//    console.log("准备读取文件！");
//    fs.read(fd, buf, 0, buf.length, 0, function(err, bytes){
//       if (err){
//          console.log(err);
//       }

//       // 仅输出读取的字节
//       if(bytes > 0){
//          console.log(buf.slice(0, bytes).toString());
//       }

//       // 关闭文件
//       fs.close(fd, function(err){
//          if (err){
//             console.log(err);
//          } 
//          console.log("文件关闭成功");
//       });
//    });
// });
