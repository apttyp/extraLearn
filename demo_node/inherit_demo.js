// var util = require('util');
// function Base(){
// 	this.name = 'base';
// 	this.base = 1991;
// 	this.sayHelllo = function(){
// 		console.log('Hello'+this.name);
// 	};
// }
// Base.prototype.showName = function(){
// 	console.log(this.name);
// };
// function Sub(){
// 	this.name = 'sub';
// }
// util.inherits(Sub, Base);

// var objBase = new Base();
// objBase.showName();
// objBase.sayHelllo();
// console.log(objBase);

// var objSub = new Sub();
// objSub.showName();
// // objSub.sayHelllo();
// console.log(objSub);


var util = require('util');

function Person(){
	this.name='person';
	this.toString = function(){
		return this.name;
	};
}

var perobj = new Person();
console.log(util.inspect(perobj));
console.log(util.inspect(perobj, true));

console.log(util.isRegExp(/asd asd/));

console.log(util.isDate(new Date()));
