import cherrypy
import requests
import json
import time
import os



def gen_report(list,type,title,id,link = "https://ti.cdcllp.com",score=50):
    report=[]
    for item in list:
        obj={
            "title": item + " " + title,
		    "timestamp": int(time.time()),
		    "iocs": {
			    type: [
				    item
                ]
		    },
		    "score": score,
		    "link":link,
		    "id": id+ "-" + item
            }
        report.append(obj)
    return report

def create_header(cat= "Open Source",provider_url ="https://ti.cdcllp.com",d_name ="CDCLLP Feed",name="feedcdcllp",summery ="Feed processed by CDCLLP",tech_data ="There are no requirements to share any data to receive this feed."):
    feed_info = {
	"category": cat,
	"provider_url": provider_url,
	"display_name": d_name,
	"name": name,
	"tech_data": tech_data,
	"summary": summery,
	"icon_small": "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",
	"icon": "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"
	}

    return feed_info

def ip_list_from_range(start,mask=24):
    ip_list =[] 
    ip_split_by_dot = start.split('.')
    for i in range(0,256):
        ip_split_by_dot[3] = str(i)
        ip_list.append('.'.join(ip_split_by_dot))
    return ip_list
    

class Feeds(object):
    @cherrypy.expose
    def index(self,**params):
      
        return "Sponsored by CDCLLP"
    
    

    @cherrypy.expose
    def malware_domains(self,**params):
        list_ip = []
        res = requests.get("https://panwdbl.appspot.com/lists/mdl.txt",stream=True)
        for line in res.raw:
            line= line.decode('utf-8').replace('\n','')
            if(line[0] != '#'):
                if(line.find('-')>-1):
                    continue # to be considered
                else:
                    list_ip.append(line)
        
        results= {
            "feedinfo":create_header(d_name="Malware domains",name="Malwaredomains",summery ="This feed contains intelligence provided by Malware domains. It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in malware domains","Malware-domain")
            }
        return json.dumps(results)
    @cherrypy.expose
    def zeus_bad_ip(self,**params):
        list_ip = []
        res = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=badips")
        lines= str(res.text).splitlines()
        for line in lines:
            if(len(line) > 2 and line[0] != '#'):
                if(line.find('-')>-1):
                    continue
                else:
                    list_ip.append(line)
        results= {
            "feedinfo":create_header(provider_url="https://zeustracker.abuse.ch/blocklist.php?download=badips",d_name="Zues Bad id",name="zuesbadip",summery ="This feed contains intelligence provided by zeustracker. It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in Zues Bad IP List","zeus-bad-ip")
            }
        return json.dumps(results)
    @cherrypy.expose
    def zeus_std_ip(self,**params):
        list_ip = []
        res = requests.get("https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist")
        lines= str(res.text).splitlines()
        for line in lines:
            if(len(line) > 2 and line[0] != '#'):
                if(line.find('-')>-1):
                    continue
                else:
                    list_ip.append(line)
        results= {
            "feedinfo":create_header(provider_url="https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist",d_name="Zues Standard id",name="zuesstdip",summery ="This feed contains intelligence provided by zeustracker. It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in Zues Standrad IP List","zeus-std-ip")
            }
        return json.dumps(results)
    @cherrypy.expose
    def ramnit_cnc(self,**params):
        list_ip = []
        res = requests.get("http://osint.bambenekconsulting.com/feeds/ramnit-iplist.txt")
        lines= str(res.text).splitlines()
        for line in lines:
            if(len(line) > 2 and line[0] != '#'):
                line = line.split(',')[0]
                if(line.find('-')>-1):
                    continue
                else:
                    list_ip.append(line)
        results= {
            "feedinfo":create_header(provider_url="http://osint.bambenekconsulting.com/feeds/ramnit-iplist.txt",d_name="Ramnit CC IP addresses",name="ramnitcc",summery ="This feed contains intelligence provided by ramnitc&c. It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " one of Ramnit C_C server","ramnit-cnc-server",score=80)
            }
        return json.dumps(results)
    @cherrypy.expose
    def emerging_threats_compromised_ip(self,**params):
        list_ip = []
        res = requests.get("https://rules.emergingthreats.net/blockrules/compromised-ips.txt")
        lines= str(res.text).splitlines()
        for line in lines:
            if(len(line) > 2 and line[0] != '#'):
                if(line.find('-')>-1):
                    continue
                else:
                    list_ip.append(line)
        results= {
            "feedinfo":create_header(provider_url="https://rules.emergingthreats.net/blockrules/compromised-ips.txt",d_name="Emerging Threats comprimised IPs",name="emergecompip",summery ="This feed contains intelligence provided by emerging_threats. It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in emerging threats comprimised ip list",id="emerge-comp-ip",score=60)
            }
        return json.dumps(results)
    @cherrypy.expose
    def emerging_threats_ip_blocklist(self,**params):
        list_ip = []
        res = requests.get("https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt")
        lines= str(res.text).splitlines()
        for line in lines:
            if(len(line) > 2 and line[0] != '#'):
                if(line.find('-')>-1 or line.find('/') > 1 ):
                    continue # to be considered
                else:
                    list_ip.append(line)
        results= {
            "feedinfo":create_header(provider_url="https://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt",d_name="Emerging Threats IPs",name="emergeip",summery ="This feed contains intelligence provided by emergingthreats . It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in emerging threats cc ip list",id="emerge-cc-ip",score=60)
            }
        return json.dumps(results)
    
    #complex feed starts from here
    @cherrypy.expose
    def sans_top(self,**params):
        list_ip = []
        res = requests.get("https://isc.sans.edu/block.txt")
        lines= str(res.text).splitlines()
        for line in lines:
         if(len(line) > 2 and line[0] != '#' and line[0] != 'S' ):
            splited_entries = line.split('\t')
            list_ip.extend(ip_list_from_range(splited_entries[0],int(splited_entries[2])))   
        results= {
            "feedinfo":create_header(provider_url="https://isc.sans.edu/block.txt",d_name=" IPs from SANS top blocklists",name="sansblocklist",summery="This feed contains intelligence provided by sansblocklist . It leverages insights into attacks across the community and will show you hostile scanning hosts, malware hosts, and other targeting and security event information. This feed is a list of high-confidence threat indicators, updated periodically. Generally, hits on this feed should be suitable for generating alerts.There are no requirements to share any data to receive this feed"),
            "reports":gen_report(list_ip,"ipv4", " listed in SANS top ip blocklists",id="sans-block-list",score=70)
            }
        return json.dumps(results)

PATH = os.path.abspath(os.path.dirname(__file__))
cherrypy.quickstart(Feeds(),'/',config={
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.join(PATH,"static"),
                'request.show_tracebacks' : False
            },
    })
