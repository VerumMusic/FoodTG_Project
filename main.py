import requests
import json
import os
from bs4 import BeautifulSoup as bs
import random
import fake_useragent
import time
import datetime
from food_test import scan, sport_scan, diabetic_scan

url = 'https://1000.menu/catalog/'

def opener(func, path="database"):
    def wrapper():
        if not os.path.exists(f".\{path}"):
            os.mkdir(path)
        os.chdir(path)
        func()
        os.chdir("..")
    return wrapper

def parse_url(url, name_dir = None):
    print("Страница - ", url)
    headers = {'UserAgent': fake_useragent.UserAgent().random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
            }
    resp = requests.get(url=url, headers = headers)
    if resp.status_code == 200:
        soup = bs(resp.text, 'lxml')
        info = soup.find_all(class_='cn-item', recursive=True)
        res = []
        
        for n, row in enumerate(info):
            a_tag = row.find("a")
            if a_tag:
                link = a_tag['href']
                res.append(link)
            print("Собрано ссылок - ", n)
            
        return res
    else:
        print('Возникла ошибка - ', resp.status_code)
        
def parser_one(url):
    try:
        print('Обработка страницы - ', url)
        time.sleep(0.5)
        headers = {'UserAgent': fake_useragent.UserAgent().random,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                }
        resp = requests.get(url = url, headers = headers)
        soup = bs(resp.text, "lxml")
        try:
            finded_ings = soup.find(id = 'ingredients').find_all("meta")
            finded_ings = [i['content'] for i in finded_ings]
        except Exception:
            finded_ings = soup.find(id = 'recept-list').find_all("meta")
            finded_ings = [i['content'] for i in finded_ings]
        title = soup.find("h1").text
        timer = soup.find_all(class_="label-with-icon")[-1].text.split("\n")[2]
        views = soup.find("span", class_='label ml-2').text
        recept = "".join(map(lambda n: n.text, soup.find_all(class_ = "instruction")))
        short_story = ". ".join(soup.find(class_="description is-citation").text[::-1].split(".")[1:][::-1])[::-1]
        try:
            kkal = soup.find(id="nutr_kcal").text+" ккал. / 100 г."
        except Exception:
            kkal = soup.find(class_="nutr_kcal").text+" ккал. / 100 г."
        dct = {
                'url': url,
                "porcies": finded_ings[0],
                'ings': finded_ings[1:],
                'title': title,
                "recept": recept,
                'time': timer,
                "views": views,
                "kkal": kkal,
                'story': short_story,
            }
        return dct
    except Exception as x:
        print(f"на {url} все сломалось, ошибка - {x}")
        
def zavtrak_db(): #работает
    url_list_zavtrak = []
    data = []
    
    for i in random.choices(range(1, 10), k=2):
        url_list_zavtrak.extend(parse_url(url + 'na-zavtrak'+f'/{i}'))
    if os.path.exists("zavtrak.json"): 
        os.remove("zavtrak.json")
    
    for ur in url_list_zavtrak:
        data.append(parser_one("https://1000.menu"+ur))
        
    with open("zavtrak.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
def obed_db(): #работает
    url_list_obed = []
    data = []
    
    url_list_obed.extend(parse_url(url + 'vtoroe-bludo'))
    url_list_obed.extend(parse_url(url + 'supj'))
    if os.path.exists("obed.json"):
        os.remove("obed.json")
    
    for ur in url_list_obed:
        data.append(parser_one("https://1000.menu"+ur))
        
    with open("obed.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
def uzhin_db(): #работает
    url_list_uzhin = []
    data = []
    for i in random.choices(range(1, 10), k=2):
        url_list_uzhin.extend(parse_url(url + 'zvanji-uzhin'+f'/{i}'))
    if os.path.exists("uzhin.json"):
        os.remove("uzhin.json")
    
    for ur in url_list_uzhin:
        data.append(parser_one("https://1000.menu"+ur))
        
    with open("uzhin.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def perekus(): #работает
    url_list_zakuski = []
    data = []
    for i in random.choices(range(1, 10), k=2):
        url_list_zakuski.extend(parse_url(url + 'zakuski'+f'/{i}'))
    if os.path.exists("zakuski.json"):
        os.remove("zakuski.json")
    
    for ur in url_list_zakuski:
        data.append(parser_one("https://1000.menu"+ur))
        
    with open("zakuski.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        
def napitki(): #работает
    url_list_zakuski = []
    data = []
    for i in random.choices(range(1, 4), k=2):
        url_list_zakuski.extend(parse_url(url + 'napitki?ms=1&str=&cat_es_inp%5B%5D=16&es_tf=0&es_tt=14&es_cf=0&es_ct=2000'+f'/{i}'))
    if os.path.exists("napitki.json"):
        os.remove("napitki.json")
    
    for ur in url_list_zakuski:
        data.append(parser_one("https://1000.menu"+ur))
        
    with open("napitki.json", "w", encoding = "utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def healthy_food():
    with open('zavtrak.json', encoding="utf-8") as f:
        zavtrak = json.load(f)
        with open('uzhin.json', encoding="utf-8") as f:
            uzhin = json.load(f)
            with open('zakuski.json', encoding="utf-8") as f:
                zakuski = json.load(f)
                with open('obed.json', encoding="utf-8") as f:
                    obed = json.load(f)
                    with open('napitki.json', encoding="utf-8") as f:
                        napitki = json.load(f)
                        
    if not os.path.exists("healthy_food"):
        os.mkdir('healthy_food')
    os.chdir("healthy_food")
    
    with open('zavtrak.json', "w", encoding="utf-8") as f:
        json.dump(scan(zavtrak), f, ensure_ascii=False, indent=4)
        
    with open('uzhin.json', "w", encoding="utf-8") as f:
        json.dump(scan(uzhin), f, ensure_ascii=False, indent=4)
        
    with open('zakuski.json', "w", encoding="utf-8") as f:
        json.dump(scan(zakuski), f, ensure_ascii=False, indent=4)
    
    with open('obed.json', "w", encoding="utf-8") as f:
        json.dump(scan(obed), f, ensure_ascii=False, indent=4)
        
    with open('napitki.json', "w", encoding="utf-8") as f:
        json.dump(scan(napitki), f, ensure_ascii=False, indent=4)
    os.chdir("..")
        
def sport():
    if os.path.exists("database/healthy_food"):
        os.chdir("database/healthy_food")
    if os.path.exists("healthy_food"):
        os.chdir("healthy_food")
    with open('zavtrak.json', encoding="utf-8") as f:
        zavtrak = json.load(f)
        with open('uzhin.json', encoding="utf-8") as f:
            uzhin = json.load(f)
            with open('zakuski.json', encoding="utf-8") as f:
                zakuski = json.load(f)
                with open('obed.json', encoding="utf-8") as f:
                    obed = json.load(f)
                    with open('napitki.json', encoding="utf-8") as f:
                        napitki = json.load(f)
                
    os.chdir("..")
    if not os.path.exists("sport_food"):
        os.mkdir("sport_food")
    os.chdir("sport_food")
    with open('zavtrak.json', "w", encoding="utf-8") as f:
        json.dump(sport_scan(zavtrak), f, ensure_ascii=False, indent=4)
        
    with open('uzhin.json', "w", encoding="utf-8") as f:
        json.dump(sport_scan(uzhin), f, ensure_ascii=False, indent=4)
        
    with open('zakuski.json', "w", encoding="utf-8") as f:
        json.dump(sport_scan(zakuski), f, ensure_ascii=False, indent=4)
    
    with open('obed.json', "w", encoding="utf-8") as f:
        json.dump(sport_scan(obed), f, ensure_ascii=False, indent=4)
        
    with open('napitki.json', "w", encoding="utf-8") as f:
        json.dump(sport_scan(napitki), f, ensure_ascii=False, indent=4)
    os.chdir("..")
    
def diabetic():
    with open('zavtrak.json', encoding="utf-8") as f:
        zavtrak = json.load(f)
        with open('uzhin.json', encoding="utf-8") as f:
            uzhin = json.load(f)
            with open('zakuski.json', encoding="utf-8") as f:
                zakuski = json.load(f)
                with open('obed.json', encoding="utf-8") as f:
                    obed = json.load(f)
                    with open('napitki.json', encoding="utf-8") as f:
                        napitki = json.load(f)
                        
    if not os.path.exists("diabetic"):
        os.mkdir("diabetic")
    os.chdir("diabetic")
    
    with open('zavtrak.json', "w", encoding="utf-8") as f:
        json.dump(diabetic_scan(zavtrak), f, ensure_ascii=False, indent=4)
        
    with open('uzhin.json', "w", encoding="utf-8") as f:
        json.dump(diabetic_scan(uzhin), f, ensure_ascii=False, indent=4)
        
    with open('zakuski.json', "w", encoding="utf-8") as f:
        json.dump(diabetic_scan(zakuski), f, ensure_ascii=False, indent=4)
    
    with open('obed.json', "w", encoding="utf-8") as f:
        json.dump(diabetic_scan(obed), f, ensure_ascii=False, indent=4)
        
    with open('napitki.json', "w", encoding="utf-8") as f:
        json.dump(diabetic_scan(napitki), f, ensure_ascii=False, indent=4)
    os.chdir("..")
    
def modification_date_day(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t).day

@opener
def main():
    try:
        if modification_date_day("zavtrak.json")!=datetime.date.today().day:
            napitki()
            obed_db()
            zavtrak_db()
            perekus()
            uzhin_db()
            healthy_food()
            sport()
            diabetic()
    except Exception:
        napitki()
        obed_db()
        zavtrak_db()
        perekus()
        uzhin_db()
        healthy_food()
        sport()
        diabetic()
    print("База данных обновлена!")
        
        
    

    
    
    


if __name__ == '__main__':
    main()