from lxml import html
import requests
from math import trunc
import csv

#page = requests.get('http://www.bikewagon.com/part/brakes-levers')

#page = requests.get('http://www.bikewagon.com/part/brakes-levers/cables-housing')

#page = requests.get('http://www.bikewagon.com/part/brakes-levers/other-brakes')


def csv_get_site(file_obj, output_path):
    data = [("Category","last_page")]
    reader = csv.DictReader(file_obj, delimiter = ',')
    for line in reader:
        page = requests.get(line['Category'])
        tree = html.fromstring(page.content)
        xpath_result = tree.xpath('//div[@class="toolbar-bottom"]/div[@class="toolbar"]/div[@class="sorter"]/div[contains(@class, "content-pagination")]/ul/li/a/text()')
        page_count = [int(item) for item in xpath_result if item.isdigit()]
        max_page_number = 1 if len(page_count) == 0 else max(page_count)
        for page_number in range(1, max_page_number+1):
            data.append((line['Category'],trunc(page_number)))
            print(",".join((line["Category"], str(trunc(page_number)))))

    with open(output_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for data_line in data:
            writer.writerow(data_line)

if __name__=="__main__":
    old_csv_path = 'C:\\Users\\alan\\Documents\\_Tax returns\\Amazon\\Tactical Arbitrage\\bulk_lists_for_product_search\\bikewagon_category1.csv'
    new_csv_path = old_csv_path.replace(".csv", "_updated.csv")
    with open(old_csv_path) as f_obj:
        csv_get_site(f_obj, new_csv_path)
