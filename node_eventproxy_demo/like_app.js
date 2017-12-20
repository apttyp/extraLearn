var superagent = require('superagent');
var cheerio = require('cheerio');
url = 'https://account.dui.ai/cas/login'
var execution = ''
superagent.get(url).end(function(err, res){
	if (err){
		return console.log(err);
	}
	var $ = cheerio.load(res.text);
	emm=$('input').attr('name', 'value')[3];
	execution = emm['attribs']['value'];
		// console.log(res.cookies);
	console.log(execution);
	console.log(res.headers);
})