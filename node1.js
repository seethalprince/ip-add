const https = require('https');

var urll="malware_domains"

https.get("https://ti.cdcllp.com/"+urll,{"rejectUnauthorized": false}, (resp) => {
  var data = [];

  resp.on('data', (chunk) => {
    data.push(chunk);
  });

  resp.on('end', () => {
    data=Buffer.concat(data).toString();
    var temp = JSON.parse(data);
    console.log("\nFeed_Name : "+temp.feedinfo.name+"\n");
    //console.log("\nIMG : "+temp.feedinfo.icon+"\n");
    console.log("\nDesc : "+temp.feedinfo.summary+"\n");
    
temp.reports.forEach(function(element){
     element.iocs.ipv4.forEach(function(ip){
       console.log(ip)
  
     });
    

  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});