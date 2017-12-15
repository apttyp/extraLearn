var requ = require('request');
var cheerio = require('cheerio');
var http=require('http');
var qs=require('querystring');

// var app = requ();
// requ('https://www.dui.ai', function(error, response, body){
// 	if (!error && response.statusCode == 200){
// 		console.log("get success");
// 		console.log(body);
// 	}
// })
var myvar;

requ('https://account.dui.ai/cas/login', function(error, response, body){
	if (!error && response.statusCode == 200){
		console.log("get success");
		console.log(response['headers']);
		// console.log(body);
		$=cheerio.load(body);
		// console.log($('input')[3].attr('name', 'value'));
		emm=$('input').attr('name', 'value')[3];
		execution = emm['attribs']['value'];
		var paydata = {
			'username':'****',
			'password':'****',
			'execution':execution,
			'_eventId':'submit'
		};
		var content = qs.stringify(paydata);
		var options = {
			method:'POST',
			host: 'www.dui.ai',
			accept:'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',

			cookie:'gr_user_id=80dc98f9-e3f8-427b-a22b-ad111096740c; gr_session_id_8dbfb0987863dbc0=fcb2852f-3f8f-4fcf-b999-4d8bf2c7a600; _ps=QrbuLRhiWm0dRw3CA_QjLg..|1513302875|NdleeTMohpFPTK0cIHIStXH8eqY.',
           	headers:{
                  'Content-Type':'application/x-www-form-urlencoded',
                  'Content-Length':content.length
            }
		}
		console.log("post options:\n",options);
		console.log("content:",content);
		var req = http.request(options, function(res) {
  			console.log("statusCode: ", res.statusCode);
  			console.log("headers: ", res.headers);
  			var _data='';
  			res.on('data', function(chunk){
     			_data += chunk;
  			});
  			res.on('end', function(){
     		console.log("\n--->>\nresult:",_data)
   			});
		});
		req.write(content);
        req.end();
	}else{
		console.log("Page Down!");
	}
})