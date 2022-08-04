import scrapy
import os
from os.path import dirname
import json


current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, "source-EXPLOIT-DB.html")

class CveSpider(scrapy.Spider):
    name = 'cve_json'
    allowed_domains = ['cve.mitre.org']
    start_urls = ['https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html']
    # start_urls = [f"{url}"]
    print("PRINTING URL: \n", str(start_urls))

    def parse(self, response):
        for child in response.xpath("//table"):
            if len(child.xpath("tr")) > 100:
                table = child
                break
        count = 0
        data = {}
        json_file = open("vulnerabilities.json", "w")

        for row in table.xpath("//tr"):
            if count > 100:
                break
            try:
                exploit_id = row.xpath("td//text()")[0].extract()
                cve_id = row.xpath("td//text()")[2].extract()
                data[exploit_id] = cve_id
                count += 1
            except IndexError:
                pass
        json.dump(data, json_file)
        json_file.close()