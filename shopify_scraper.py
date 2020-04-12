import csv
import json
import sys
import requests
import pdb

store_url = sys.argv[1]

def scrape_store(base_url):
    filename = "products.csv"
    print (filename)
    create_file(filename)
    incomplete_url = base_url + '/products.json?page='
    n = 1 
    while True:
        page_url = incomplete_url + str(n)
        try:
            write_values_from_url(page_url, filename,base_url)
            n += 1
        except:
            print ("Done")
            break


def create_file(filename):
    f = open( filename, "w")
    f.write ("vendor *&^ title *&^ link *&^ Description *&^ Price*&^ images")
    f.close
    return filename
    
def write_values_from_url(url,file,base_url):
    # takes a url and returns a list of products from that page
    resp = requests.get(url)
    json = resp.json()
    products =json['products']
    if len(products) ==0:
        raise

    f = open("products.csv", "a")
    for product in products:
        line = ''
        line= line +  (product['vendor'] )
        line= line + ("*&^")
        line= line +  (product['title'] )
        line= line + ("*&^")
        line= line +  base_url+ '/products/' + (product['handle'])
        line= line + ("*&^")
        line= line +  (product['body_html']).replace('\n','')
        # test = product['body_html']
        # test = test.replace('\n','')

        # pdb.set_trace()

        line= line + ("*&^")
        line= line +  (product['variants'][0]['price'])
        line= line + ("*&^")
        for image in product['images']:
            line= line +  (image['src'])
            line= line + ("*&^")
        f.write('\n')
        f.write(line)
        line = ''
    f.close()

    # break

scrape_store(store_url)
