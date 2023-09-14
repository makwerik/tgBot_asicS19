import requests
import json
import telebot
from telebot import types
import yaml


class S19(telebot.TeleBot):
    """Получение инормации из json для авторизации на сайте"""
    def __init__(self, token, url):
        super().__init__(token)

        try:
            with open('auth.json', encoding='utf8') as file:
                self.headers = json.load(file)
        except:
            print("Account information is missing")

    def full_stats(self):
        """Используется для получения json файла со списком интересующих нас данных"""
        return requests.get(f'http://{url}/cgi-bin/stats.cgi', headers=self.headers).json()

    def start(self, message):
        """Приветствие и вывод доступных методов"""
        name = message.from_user.first_name, message.from_user.last_name

        if name[1] is None:
            name = message.from_user.first_name

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        funs = types.KeyboardButton('Состояние кулеров')
        chip = types.KeyboardButton('Температура чипов')
        plats = types.KeyboardButton('Температура плат')
        markup.add(funs, chip, plats)
        self.send_message(message.from_user.id, f"👋 Привет, {name} ! Я твой бот-помощник по асику!",
                          reply_markup=markup)

    def stats_chp_pcb(self, message):
        """Через метод full_stats вытаскиваем нужные данные для каждого условия"""
        if message.text == 'Состояние кулеров':
            self.send_message(message.from_user.id,
                              f'Обороты куллеров/мин : {self.full_stats().get("STATS")[0].get("fan")}')

        if message.text == 'Температура чипов':
            for i in range(0, 3):
                self.send_message(message.from_user.id,
                                  f'Температура чипов на {i + 1}-й плате : {self.full_stats().get("STATS")[0].get("chain")[i].get("temp_chip")}')

        if message.text == 'Температура плат':
            for i in range(0, 3):
                self.send_message(message.from_user.id,
                                  f'Температура {i + 1}-й платы : {self.full_stats().get("STATS")[0].get("chain")[i].get("temp_pcb")}')


with open('config.yaml', 'r', encoding='utf8') as config:
    cfg = yaml.load(config, Loader=yaml.FullLoader)

token = cfg.get('token')
url = cfg.get('url')

s = S19(token, url)


@s.message_handler(commands=['start'])  # Декоратор обработки сообщения
def start(message):
    s.start(message)


@s.message_handler(content_types=['text']) # Декоратор обработки сообщения
def stats_chp_pcb(message):
    s.stats_chp_pcb(message)


s.polling(none_stop=True, interval=0)
