var eventproxy = require('eventproxy');
var superagent = require('superagent');
var cheerio = require('cheerio');

var url = require('url');
var cnodeUrl = 'https://cnodejs.org';

var topicUrls = [];

superagent.get(cnodeUrl)
	.end(function (err, res){
		if(err){
			return console.log(err);
		}
		
		var $ = cheerio.load(res.text);
		console.log(res.text);
		$('#topic_list .topic_title').each(function(idx, element){
			var $element=$(element);
			var href = url.resolve(cnodeUrl, $element.attr('href'));
			topicUrls.push(href);
		});
		// 得到一个 eventproxy 的实例
		var ep = new eventproxy();
		// 命令 ep 重复监听 topicUrls.length 次（在这里也就是 40 次） `topic_html` 事件再行动
		ep.after('topic_html', topicUrls.length, function (topics) {
  		// topics 是个数组，包含了 40 次 ep.emit('topic_html', pair) 中的那 40 个 pair

  		// 开始行动
  		topics = topics.map(function (topicPair) {
    		// 接下来都是 jquery 的用法了
    		var topicUrl = topicPair[0];
    		var topicHtml = topicPair[1];
    		var $ = cheerio.load(topicHtml);
    		return ({
     			title: $('.topic_full_title').text().trim(),
      			href: topicUrl,
      			comment1: $('.reply_content').eq(0).text().trim(),
    		});
  		});

  		console.log('final:');
  		console.log(topics);
	});

	topicUrls.forEach(function (topicUrl) {
  	superagent.get(topicUrl)
    	.end(function (err, res) {
      		console.log('fetch ' + topicUrl + ' successful');
      		ep.emit('topic_html', [topicUrl, res.text]);
    	});
	});
});
