var requ = require('request');
var cheerio = require('cheerio');
var http=require('http');
var qs=require('querystring');

var myvar;

requ('https://account.dui.ai/cas/login', function(error, response, body){
	if (!error && response.statusCode == 200){
		console.log("get success");
		console.log(response['headers']);
		console.log(response);
		// console.log(body);
		$=cheerio.load(body);
		// console.log($('input')[3].attr('name', 'value'));
		emm=$('input').attr('name', 'value')[3];
		execution = emm['attribs']['value'];
		console.log(execution);
		var paydata = {
			'username':'*****',
			'password':'*****',
			'execution':execution,
			'_eventId':'submit'
		};
		var content = qs.stringify(paydata);
		var options = {
			method:'POST',
			host: 'account.dui.ai',
			connection:'keep-alive',
			// port:443,
			accept:'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			cookie:'JSESSIONID=78AFD8C71958886CAA0456AD5958EAB7; gr_user_id=80dc98f9-e3f8-427b-a22b-ad111096740c; gr_session_id_8dbfb0987863dbc0=060d792b-0e0f-40f5-8974-3ce0556048a2',
           	headers:{
                  'Content-Type':'application/x-www-form-urlencoded',
                  'Content-Length':content.length
            }
		}
		console.log("post options:\n",options);
		console.log("content:",content);

		var body = '';
		var req = http.request(options, function(res) {
    		console.log("Got response: " + res.statusCode);
    		res.on('data',function(d){
        		body += d;
    		}).on('end', function(){
        		console.log("headers:\n",res.headers)
        		console.log("body:\n",body)
    		});
		}).on('error', function(e) {
    		console.log("Got error: " + e.message);
		})

		req.write(content);
        req.end();
	}else{
		console.log("Page Down!");
	}
})
