import requests
import re
#from OTXv2 import OTXv2
from collections import defaultdict
from datetime import datetime, timedelta

# Defines the list that is going to populate the different feeds
d = defaultdict(list)

# Your API key for OTX. If you do not have any, please comment out
# "get_alienvault" in the main function.
#otx = OTXv2("XXXXX")


class GetFeeds(object):
    """
    Main class to gather and output feed results
    """
    url="/home/seethalprince/Desktop/cb-feed-server-master/url.txt"
    def download_file(self, url):
        """
        Download the feeds specified
        :param url: The location of the source to download
        :return The content of the request
        """

        r = requests.get(url)
        return r.content

    def ipgrabber(self, results):
        """
        :param reults: The results that should be filtered
        :return: Only the IP addresses from the object it filtered out
        """

        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', results)
        return ip
print(ip)


       
