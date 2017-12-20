//example1
/*
function f1(){
	var n=999;
	nAdd=function(){
		n+=1
	}
	function f2(){
		console.log(n);
	}
	return f2;
}
var result=f1();
result(); // 999
nAdd();
result(); // 1000
*/

/*
var name = "The Window";
var object = {
	name : "My Object",
	getNameFunc : function(){
　　    return function(){
　　　　	return this.name;
　　       	};
　　}
};
console.log(object.getNameFunc()());
*/

/*
function outerFun()
{
	var a=0;
 	function innerFun(){
		a++;
  		console.log(a);
	}
	return innerFun;  //注意这里
}
var obj=outerFun();
obj();  //结果为1
obj();  //结果为2
var obj2=outerFun();
obj2();  //结果为1
obj2();  //结果为2
*/

var name = "The Window";
var object = {
	name : "My Object",
	getNameFunc : function(){
　　    return function(){
　　　　	return this.name;
　　　　};
　　}
};
console.log(object.getNameFunc()());

var name = "The Window";
var object = {
	name : "My Object",
　　getNameFunc : function(){
　　    var that = this;
　　　　return function(){
　　　　    return that.name;
　　　　};
　　}
};

console.log(object.getNameFunc()());