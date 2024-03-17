import json
import random
import os

def opener(func):
    def wrapper():
        if not os.path.exists(".\database"):
            os.mkdir("database")
        os.chdir("database")
        return func()
    return wrapper

@opener
def choose():

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
    reply_lst = []
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)

    reply_lst.append('👌 Запрос принят! Ожидайте...\n\n')
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️ Время приготовления: {choose_z['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_z['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_z['story']}")
    reply_lst.append(f"🔥 Калории: {choose_z['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_z['porcies']} порций:")
    for i in choose_z['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_z['url']}")
    
    
    reply_lst.append(f"|🥪 Перекус 1: {choose_l1['title']}\n⏱️ Время приготовления: {choose_l1['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_l1['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_l1['story']}")
    reply_lst.append(f"🔥 Калории: {choose_l1['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_l1['porcies']} порций:")
    for i in choose_l1['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_l1['url']}")

    

    reply_lst.append(f"|    Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️ Время приготовления: {choose_o[0]['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_o[0]['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_o[0]['story']}")
    reply_lst.append(f"🔥 Калории: {choose_o[0]['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_o[0]['porcies']} порций:")
    for i in choose_o[0]['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_o[0]['url']}")
    
    reply_lst.append(f"|🥩 2 блюдо: {choose_o[1]['title']}\n⏱️ Время приготовления: {choose_o[1]['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_o[1]['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_o[1]['story']}")
    reply_lst.append(f"🔥 Калории: {choose_o[1]['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_o[1]['porcies']} порций:")
    for i in choose_o[1]['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_o[1]['url']}")
    
    reply_lst.append(f"|🥪 Перекус 2: {choose_l2['title']}\n⏱️ Время приготовления: {choose_l2['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_l2['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_l2['story']}")
    reply_lst.append(f"🔥 Калории: {choose_l2['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_l2['porcies']} порций:")
    for i in choose_l2['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_l2['url']}")
    
    reply_lst.append(f"|🍕 Ужин: {choose_u['title']}\n⏱️ Время приготовления: {choose_u['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_u['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_u['story']}")
    reply_lst.append(f"🔥 Калории: {choose_u['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_u['porcies']} порций:")
    for i in choose_u['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_u['url']}")
    
    reply_lst.append(f"|🍹 Напиток: {choose_n['title']}\n⏱️ Время приготовления: {choose_n['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_n['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_n['story']}")
    reply_lst.append(f"🔥 Калории: {choose_n['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_n['porcies']} порций:")
    for i in choose_n['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_n['url']}")
    os.chdir("..")
    return reply_lst


def choose_decs():

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
    reply_lst = []
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)

    reply_lst.append('👌 Запрос принят! Ожидайте...\n\n')
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️ Время приготовления: {choose_z['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_z['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_z['story']}")
    reply_lst.append(f"🔥 Калории: {choose_z['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_z['porcies']} порций:")
    for i in choose_z['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_z['url']}")
    
    
    reply_lst.append(f"|🥪 Перекус 1: {choose_l1['title']}\n⏱️ Время приготовления: {choose_l1['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_l1['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_l1['story']}")
    reply_lst.append(f"🔥 Калории: {choose_l1['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_l1['porcies']} порций:")
    for i in choose_l1['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_l1['url']}")

    

    reply_lst.append(f"|    Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️ Время приготовления: {choose_o[0]['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_o[0]['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_o[0]['story']}")
    reply_lst.append(f"🔥 Калории: {choose_o[0]['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_o[0]['porcies']} порций:")
    for i in choose_o[0]['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_o[0]['url']}")
    
    reply_lst.append(f"|🥩 2 блюдо: {choose_o[1]['title']}\n⏱️ Время приготовления: {choose_o[1]['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_o[1]['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_o[1]['story']}")
    reply_lst.append(f"🔥 Калории: {choose_o[1]['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_o[1]['porcies']} порций:")
    for i in choose_o[1]['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_o[1]['url']}")
    
    reply_lst.append(f"|🥪 Перекус 2: {choose_l2['title']}\n⏱️ Время приготовления: {choose_l2['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_l2['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_l2['story']}")
    reply_lst.append(f"🔥 Калории: {choose_l2['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_l2['porcies']} порций:")
    for i in choose_l2['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_l2['url']}")
    
    reply_lst.append(f"|🍕 Ужин: {choose_u['title']}\n⏱️ Время приготовления: {choose_u['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_u['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_u['story']}")
    reply_lst.append(f"🔥 Калории: {choose_u['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_u['porcies']} порций:")
    for i in choose_u['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_u['url']}")
    
    reply_lst.append(f"|🍹 Напиток: {choose_n['title']}\n⏱️ Время приготовления: {choose_n['time']}")
    reply_lst.append(f"👀 Просмотрено: {choose_n['views']}")
    reply_lst.append(f"📝 Краткое описание: {choose_n['story']}")
    reply_lst.append(f"🔥 Калории: {choose_n['kkal']}\n")
    reply_lst.append(f"📋 Ингредиенты для {choose_n['porcies']} порций:")
    for i in choose_n['ings']:
        reply_lst.append("---- "+i)
    reply_lst.append(f"\n🔗 Ссылка на рецепт: {choose_n['url']}")
    return reply_lst

def choose_week():
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
    reply_lst = []
    reply_lst.append("👌 Запрос принят! Ожидайте...\n\n")
    reply_lst.append("\n\nПонедельник: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\n🔥 Калории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}|")
    
    reply_lst.append("\n\nВторник: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\nКалории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}|")
    
    reply_lst.append("\n\nСреда: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\nКалории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}|")
    
    reply_lst.append("\n\nЧетверг: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\n🔥 Калории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}|")
    
    reply_lst.append("\n\nПятница: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\n🔥 Калории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}\n\n|")
    
    reply_lst.append("\n\nСуббота: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\n🔥 Калории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}|")
    
    reply_lst.append("\n\nВоскресенье: \n\n")
    
    choose_z = random.choice(zavtrak)
    choose_u = random.choice(uzhin)
    choose_o = random.choices(obed, k=2)
    choose_l1 = random.choice(zakuski)
    choose_l2 = random.choice(zakuski)
    choose_n = random.choice(napitki)
    
    reply_lst.append(f"🍳 Завтрак: {choose_z['title']}\n⏱️  {choose_z['time']}\n🔥 Калории: {choose_z['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_z['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 1: {choose_l1['title']}\n⏱️  {choose_l1['time']}\n🔥 Калории: {choose_l1['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l1['url']}\n\n")
    reply_lst.append(f"Обед:\n🥗 1 блюдо: {choose_o[0]['title']}\n⏱️  {choose_o[0]['time']}\n🔥 Калории: {choose_o[0]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[0]['url']}\n\n")
    reply_lst.append(f"🥩 2 блюдо: {choose_o[1]['title']}\n⏱️  {choose_o[1]['time']}\n🔥 Калории: {choose_o[1]['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_o[1]['url']}\n\n")
    reply_lst.append(f"🥪 Перекус 2: {choose_l2['title']}\n⏱️  {choose_l2['time']}\n🔥 Калории: {choose_l2['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_l2['url']}\n\n")
    reply_lst.append(f"🍕 Ужин: {choose_u['title']}\n⏱️  {choose_u['time']}\n🔥 Калории: {choose_u['kkal']}")
    reply_lst.append(f"\nСсылка - {choose_u['url']}")
    return reply_lst