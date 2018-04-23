from lxml import html
import requests
from math import trunc
import csv

#page = requests.get('https://www.budgetgolf.com/golf-iron-clubs.html')
#tree = html.fromstring(page.content)

#page_count = tree.xpath('count(//div[@class="navigation_block_bottom"]/div[@class="nav-pages"]/a)')


#print('Number of pages: {}'.format(trunc(page_count)))


def csv_get_site(file_obj, output_path):
    
    #data = ["Category,last_page".split(",")]
    data = [("Category","last_page")]

    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        #print(line["category"])
        page = requests.get(line["category"])
        tree = html.fromstring(page.content)
        page_count = tree.xpath('count(//div[@class="navigation_block_bottom"]/div[@class="nav-pages"]/a)')
        page_count_final = 1 if page_count == 0 else page_count
        #data.append(",".join((line["category"], str(trunc(page_count_final)))))
        data.append((line["category"], trunc(page_count_final)))
        print(",".join((line["category"], str(trunc(page_count_final)))))
       
    with open(output_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for data_line in data:
            writer.writerow(data_line)



if __name__=="__main__":
    old_csv_path = 'C:\\Users\\alan\\Documents\\_Tax returns\\Amazon\\Tactical Arbitrage\\bulk_lists_for_product_search\\budgetgolf.csv'
    new_csv_path = old_csv_path.replace(".csv", "_updated.csv")
    with open(old_csv_path) as f_obj:
        csv_get_site(f_obj, new_csv_path)
