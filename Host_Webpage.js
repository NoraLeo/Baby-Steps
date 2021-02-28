var fs=require('fs');
var http=require('http');

http.createServer(function (req,res) {
  fs.readFile('my_webpage.html', function (err, data){
    res.writeHead(200, {'Content-type':'txt/html'});
    res.write(data);
    return res.end();
  })
}).listen(8080);
