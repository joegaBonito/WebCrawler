from bs4 import BeautifulSoup
import requests

cars_com_url = input('cars.com url (absolute): ')
cars_com = 'https://cars.com'

r = requests.get(cars_com_url)

soup = BeautifulSoup(r.text,'html.parser')

list_of_items = soup.find_all('div',class_='shop-srp-listings__listing-container')

file1 = open(r"C:\Users\joejung5678\PycharmProjects\WebScraper\exporteddata.csv","w+") 
column_header = ["Title,","New or Used,","Mileage,","MSRP,","Price,","Dealer,","Link\n"]  
file1.writelines(column_header)

idx = 1
for x in list_of_items:
    print('#',idx)

    title = None
    if x.a.div.find('h2',class_='listing-row__title') is not None:
        title =  x.a.div.find('h2',class_='listing-row__title').get_text()

    new_or_used = None
    if x.a.div.find('div',class_='listing-row__stocktype') is not None:
        new_or_used = x.a.div.find('div',class_='listing-row__stocktype').get_text()

    mileage = None
    if x.a.div.find('span',class_='listing-row__mileage') is not None:
        mileage = x.a.div.find('span',class_='listing-row__mileage').get_text()

    msrp = None
    if x.a.div.find('div',class_='listing-row__details').find('span',class_='listing-row__msrp') is not None:
        msrp =  x.a.div.find('div',class_='listing-row__details').find('span',class_='listing-row__msrp').get_text().replace('MSRP','').replace(',','')

    price = None
    if x.a.div.find('span',class_='listing-row__price') is not None:
        price = x.a.div.find('span',class_='listing-row__price').get_text().replace(',', '')

    dealer = None
    if x.a.div.find('div',class_='listing-row__dealer').div.find('div',class_='dealer-name').span is not None:
        dealer = x.a.div.find('div',class_='listing-row__dealer').div.find('div',class_='dealer-name').span.get_text()

    meta = None
    if x.a.div.find('div',class_='listing-row__details').find('ul',class_='listing-row__meta') is not None:
        meta =  x.a.div.find('div',class_='listing-row__details').find_all('ul',class_='listing-row__meta')

    meta_dictionary = {}
    for li in meta:
        li_strong = li.find_all('strong')
        for each_li_strong in li_strong:
            # print(each_li_strong.get_text().strip())
            # print(each_li_strong.next_sibling.strip())
            meta_dictionary[each_li_strong.get_text().strip()] = each_li_strong.next_sibling.strip()

    idx += 1

    if title is not None:
        print(title.strip())
        file1.write(title.strip()+',')
    else:
        file1.write(' ,')

    if new_or_used is not None:
        print(new_or_used.strip())
        file1.write(new_or_used.strip()+',')
    else:
        file1.write(' ,')

    if mileage is not None:
        print(mileage.strip())
        file1.write(mileage.strip()+',')
    else:
        file1.write(' ,')

    if msrp is not None:
        print(msrp.strip())
        file1.write(msrp.strip()+',')
    else:
        file1.write(' ,')

    if price is not None:
        print(price.strip())
        file1.write(price.strip()+',')
    else:
        file1.write(' ,')

    if dealer is not None:
        print(dealer.strip())
        file1.write(dealer.strip()+',')
    else:
        file1.write(' ,')

    if x.a['href'] is not None:
        print(cars_com+x.a['href'])    
        file1.write(cars_com+x.a['href']+',')
    else:
        file1.write(' ,')

    if meta_dictionary is not None:
        for item in meta_dictionary:
            print(item,meta_dictionary.get(item))

    file1.write('\n')
    print()

file1.close()