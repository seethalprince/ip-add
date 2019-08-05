
const axions = require('https');
var url2="malware_domains"

axions.get("https://ti.cdcllp.com/"+url2,{"rejectUnauthorized": false}, (resp) => {
  var data = [];
  
 var d= new Object()
  

  resp.on('data', (chunk) => {
    data.push(chunk);
  });

  resp.on('end', () => {
    data=Buffer.concat(data).toString();
    var temp = JSON.parse(data);
    d=temp.feedinfo.name;
    d=temp.feedinfo.summary;
    Ip=[];
  //  console.log("\nFeed_Name : "+temp.feedinfo.name+"\n");
    
    
    //console.log("\nDesc : "+temp.feedinfo.summary+"\n");
    temp.reports.forEach(function(element){
        element.iocs.ipv4.forEach(function(ip){
         // console.log()
         d.Ip.push(ip)




        }); 

  });
console.log(d)
  })
}).on("error", (err) => {
  console.log("Error: " + err.message);
});
