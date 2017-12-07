//1
// var hello = require('./hello');
// hello.world();
//2
var Hello = require('./hello');
hello1 = new Hello();
hello1.setName('123456');
hello1.sayHello();


//文件模块缓存>原生模块（原生模块缓存区）>文件