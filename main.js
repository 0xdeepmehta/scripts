const http = require('http')
const url = require("url");
const fs = require("fs");

http.createServer((request, response) => {
	template = fs.readFile('index.html', function(error, template){
		response.writeHead(200, {'Content-Type': "text/html"});
		console.log(request.url);
		var parsed_url = url.parse(request.url, true);
		console.log(parsed_url);
		if (parsed_url.pathname == '/home'){
			var data = parsed_url.query.name + "<br>" + template
			response.end(data);
		}
		else{
			response.end("This is Not How it Works.");
		}
	});
	
}).listen(8880);