from bs4 import BeautifulSoup
import requests

cars_com_url = input('cars.com url (absolute): ')
cars_com = 'https://cars.com'

r = requests.get(cars_com_url)

soup = BeautifulSoup(r.text,'html.parser')

list_of_items = soup.find_all('div',class_='shop-srp-listings__listing-container')

idx = 1
for x in list_of_items:
    print('#',idx)

    new_or_used = None
    if x.a.div.find('div',class_='listing-row__stocktype') is not None:
        new_or_used = x.a.div.find('div',class_='listing-row__stocktype').get_text()

    mileage = None
    if x.a.div.find('span',class_='listing-row__mileage') is not None:
        mileage = x.a.div.find('span',class_='listing-row__mileage').get_text()

    title = None
    if x.a.div.find('h2',class_='listing-row__title') is not None:
        title =  x.a.div.find('h2',class_='listing-row__title').get_text()

    msrp = None
    if x.a.div.div.find('span',class_='listing-row__msrp') is not None:
        msrp =  x.a.div.div.find('h2',class_='listing-row__msrp').get_text()

    price = None
    if x.a.div.find('span',class_='listing-row__price') is not None:
        price = x.a.div.find('span',class_='listing-row__price').get_text()

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

    if new_or_used is not None:
        print(new_or_used.strip())

    if mileage is not None:
        print(mileage.strip())

    if title is not None:
        print(title.strip())

    if msrp is not None:
        print(msrp.strip())

    if price is not None:
        print(price.strip())

    if dealer is not None:
        print(dealer.strip())

    if meta_dictionary is not None:
        for item in meta_dictionary:
            print(item,meta_dictionary.get(item))

    if x.a['href'] is not None:
        print(cars_com+x.a['href'])

    print()