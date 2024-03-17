def test_for_good_eat(dct_el):
    awful_lst = "Колбас колбас коф Коф кофе Кофе Чипс чипс самогон Самогон пив Пив Конья конья ликер Ликер алкогол Алкогол Текил текил Водк водк настойк Настойк анисова Анисова Медовух медовух бренд Бренд хмел Хмел копчен копчён Копчен Копчён бекон Бекон майонез Майонез кетчуп Кетчуп консерв Консерв хот-дог Хот-дог попкорн Попкорн маргарин Маргарин конфет Конфет йогурт Йогурт сосиск Сосиск соя Соя бургер Бургер".split()
    awful_titles = "Чипс чипс самогон Самогон пив Пив Конь конь ликер Ликер алкогол Алкогол Текил текил Водк водк настойк Настойк анисова Анисова Медовух медовух бренд Бренд Джин джин пунш Пунш глинтвейн Глинтвейн сидр Сидр лимончелл Лимончелл абсент Абсент Наливк наливк виск Виск Бурбон бурбон Коф коф Бекон бекон майонез Майонез консерв Консерв попкорн Попкорн конфет Конфет Йогурт йогурт сосиск Сосиск".split()
    awful_text_patterns = "золотист Золотист".split()
    awful_lst += ["Вино ", "вино "]
    awful_lst += ["пиво ", "Пиво "]
    ftc = 1
    for i in awful_lst:
        if i in " ".join(dct_el['ings']):
            ftc = 0
            break
    for k in awful_titles:
        if k in dct_el['title']:
            ftc = 0
            break
    for j in awful_text_patterns:
        if j in dct_el['recept']:
            ftc = 0
            break
    return ftc

def test_for_sport_eat(dct_el):
    ftc = 1
    if int(dct_el["kkal"].split(" ккал.")[0])<=95:
        ftc = 0
    return ftc

def diabetic_test(dct_el):
    ftc = 0
    good_ings_list = "земляника клубника арбуз черника крыжовник ежевика любая смородина вишня черешня яблоки киви апельсин огурц капуст горошек салат кабачк баклажан помидор творог соя фасол чечевица гречнева овсяна перлова индейка куриц кролик лосос горбуш кета форел тунец сазан карп треск камбал хек щук судак окунь минтай сорбит рожь яйц гриб помидор огурц капуст кабачк вишн клюкв брусник груш яблок ячменн овсян телятина".split()
    awful_ings_lst = "сахар шоколад рис картофель молок йогурт банан груш виноград колбас фарш пельмен свинин говядин гусяятин сало сардельк бекон колбас котлеты бифштексы зразы шницел наггетсы котлеты сметан сливк сыр консерв сливочн растительн фрукт алкогол орех семечк сахар мед арбуз малин дын".split()
    awful_title_list = "пирожн торт шоколад варень джем лимонад фрукт выпечк конфет бульон".split()
            
    good_ings_list += [i.title() for i in good_ings_list]
    awful_ings_lst += [k.title() for k in awful_ings_lst]
    awful_title_list += [j.title() for j in awful_title_list]
    
    for g in good_ings_list:
        if g in dct_el["ings"]:
            ftc = 1
            break
        
    for f in awful_ings_lst:
        if f in dct_el["ings"]:
            ftc = 0
            break
        
    for k in awful_title_list:
        if k in dct_el["title"]:
            ftc = 0
            break
    
    return ftc
        
def sport_scan(dct: list):
    return [i for i in dct if test_for_sport_eat(i)]

def scan(dct: list):
    return [i for i in dct if test_for_good_eat(i)]

def diabetic_scan(dct: list):
    return [i for i in dct if diabetic_test(i)]

