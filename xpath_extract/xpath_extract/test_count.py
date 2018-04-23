from lxml import html
import requests
from math import trunc

page = requests.get('http://www.bikewagon.com/part/brakes-levers')

#page = requests.get('http://www.bikewagon.com/part/brakes-levers/cables-housing')

#page = requests.get('http://www.bikewagon.com/part/brakes-levers/other-brakes')

tree = html.fromstring(page.content)
xpath_result = tree.xpath('//div[@class="toolbar-bottom"]/div[@class="toolbar"]/div[@class="sorter"]/div[contains(@class, "content-pagination")]/ul/li/a/text()')
page_count = [int(item) for item in xpath_result if item.isdigit()]
max_page_number = 1 if len(page_count) == 0 else max(page_count)

print(max_page_number)
