const https = require('https')
var url2="malware_domains"
//const a="https://ti.cdcllp.com/"
https.get("https://ti.cdcllp.com"+url2,{"rejectUnauthorized": false}, (resp) => {
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
    


    

  });

}).on("error", (err) => {
  console.log("Error: " + err.message);
});