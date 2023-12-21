import telebot
from telebot import types

from App.services.serviceLaptop import LaptopService

bot = telebot.TeleBot('6400581372:AAGIND0W14iVR6Wkap79y6rQPXCA1mIe_wQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btnHeadPhones = types.KeyboardButton('Наушники')
    btnPhones = types.KeyboardButton('Смартфоны')
    btnLaptops = types.KeyboardButton('Ноутбуки')
    btnKeyboards = types.KeyboardButton('Клавиатуры')
    btnMouses = types.KeyboardButton('Мышки')
    btnAnother = types.KeyboardButton('Прочее электроника')
    markup.add(btnHeadPhones, btnPhones, btnLaptops, btnKeyboards, btnMouses, btnAnother)
    bot.send_message(message.chat.id, '1', reply_markup=markup)
    bot.register_next_step_handler(message, on_choose)


def on_choose(message):
    if message.text == 'Наушники':
        get(message)
    elif message.text == 'Смартфоны':
        bot.send_message(message.chat.id, 'Смартфоны')
    elif message.text == 'Ноутбуки':
        get(message)
    elif message.text == 'Клавиатуры':
        bot.send_message(message.chat.id, 'Клавиатуры')
    elif message.text == 'Мышки':
        bot.send_message(message.chat.id, 'Мышки')
    elif message.text == 'Прочее электроника':
        bot.send_message(message.chat.id, 'Прочее электроника')


@bot.message_handler(commands=['get'])
def get(message):
    if message.text == 'Наушники':
        from App.services.serviceHeadphones import HeadPhonesService
        head_service = HeadPhonesService()
        heads = head_service.get_all_heads()

        bd(message, heads)
    elif message.text == 'Ноутбуки':
        from App.services.serviceLaptop import LaptopService
        laptop_service = LaptopService()
        heads = laptop_service.get_all_laptops()

        # for i in heads:
        #     name, price, description, showcase, discount, image = i['name'], i['price'], i['description'], i[
        #         'showcase'], i[
        #         'discount'], i['image']
        #     bot.send_photo(message.chat.id, image,
        #                    caption=f'Название: {name}\n\nЦена: {price}\n\nОписание: {description}\n\nВ наличии: {showcase}\n\nСкидка: -{discount}%',)

        bd(message, heads)


def bd(message, obj):
    result = []
    for product in obj:
        result.append(
            {"id": product['id'], "name": product['name'], "price": product['price'], "description": product['description'],
             "showcase": product['showcase'], "discount": product['discount'], "image": product['image']})

    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('По убыванию цены')
    btn2 = types.KeyboardButton('По возрастанию цены')
    btn3 = types.KeyboardButton('Указать точный бренд')
    btn4 = types.KeyboardButton('Назад')
    markup.row(btn4)
    markup.row(btn1, btn2, btn3)
    for i in result:
        name, price, description, showcase, discount, image = i['name'], i['price'], i['description'], i['showcase'], i['discount'], i['image']
        bot.send_photo(message.chat.id, image,
                       caption=f'Название: {name}\n\nЦена: {price}\n\nОписание: {description}\n\nВ наличии: {showcase}\n\nСкидка: -{discount}%',
                       reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'По убыванию цены':
        laptop_service = LaptopService()
        laptops = laptop_service.priceDesc()
        for i in laptops:
            name, price, description, showcase, discount, image = i['name'], i['price'], i['description'], i[
                'showcase'], i['discount'], i['image']
            bot.send_photo(message.chat.id, image,
                           caption=f'Название: {name}\n\nЦена: {price}\n\nОписание: {description}\n\nВ наличии: {showcase}\n\nСкидка: -{discount}%')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'По возрастанию цены':
        laptop_service = LaptopService()
        laptops = laptop_service.priceAsc()
        for i in laptops:
            name, price, description, showcase, discount, image = i['name'], i['price'], i['description'], i[
                'showcase'], i['discount'], i['image']
            bot.send_photo(message.chat.id, image,
                           caption=f'Название: {name}\n\nЦена: {price}\n\nОписание: {description}\n\nВ наличии: {showcase}\n\nСкидка: -{discount}%')
        bot.register_next_step_handler(message, on_click)
    elif message.text == 'Указать точный бренд':
        bot.send_message(message.chat.id, 'Введите назавние бренда:')
        bot.register_next_step_handler(message, choose_brand)
    elif message.text == 'Назад':
        bot.register_next_step_handler(message, start)


def choose_brand(message):
    brand = message.text.strip()
    laptop_service = LaptopService()
    print(brand)
    laptops = laptop_service.get_by_name(brand)
    print(laptops)
    for i in laptops:
        name, price, description, showcase, discount, image = i['name'], i['price'], i['description'], i['showcase'], i[
            'discount'], i['image']
        bot.send_photo(message.chat.id, image,
                       caption=f'Название: {name}\n\nЦена: {price}\n\nОписание: {description}\n\nВ наличии: {showcase}\n\nСкидка: -{discount}%')
    bot.register_next_step_handler(message, choose_brand)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Go to site')
#     btn2 = types.KeyboardButton('Remove photo')
#     btn3 = types.KeyboardButton('Edit text')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
#     print(message.text)
#     bot.register_next_step_handler(message, on_click)
#
#
# def on_click(message):
#     print(message.text)
#     if message.text == 'Go to site':
#         bot.send_message(message.chat.id, 'site is open')
#     elif message.text.lower() == 'Remove photo':
#         bot.send_message(message.chat.id, 'remove is working')
#     elif message.text.lower() == 'Edit':
#         bot.send_message(message.chat.id, 'edited')
#
#
# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://www.sulpak.kz/f/noutbuki')
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
#
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, 'Help information!')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Go to site', url='https://onlyfans.com/')
#     btn2 = types.InlineKeyboardButton('Remove photo', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     markup.add()
#     bot.reply_to(message, 'Какое крисивое фото!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('edit text', callback.message.chat.id, callback.message.message_id)
#
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}')
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
#
bot.polling(non_stop=True)
bot.polling(none_stop=True)
