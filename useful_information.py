import re
import typing as t

import telebot
from telebot.types import Message
from gdrive_processors import GSheet

from utils import build_reply_markup
from button_data_1_lvl import RETURN_BUTTON_VALUE


gsheet = GSheet()
USEFUL_INFO_SHEET = 'useful_info'


def filter_info(
    bot: telebot.TeleBot,
    message: Message,
) -> Message:
    useful_info = gsheet.get_all_data(USEFUL_INFO_SHEET)
    sent_message = None
    for item in useful_info:
        if message.text in [item['Category 1'], item['Category 2'],
                            item['Category 3'], item['Category 4']]:
            sent_message = send_category_data(bot, item, message.chat.id)
    return sent_message or message


def send_category_data(bot: telebot.TeleBot,
                       item: dict[str, t.Any],
                       chat_id: int) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    sent_message = None
    if item['Text']:
        sent_message = bot.send_message(
            chat_id,
            item['Text'],
            reply_markup=markup
        )
    if item['Pictures']:
        pictures_list = re.split(r'\s', item['Pictures'])
        for picture in pictures_list:
            try:
                sent_message = bot.send_photo(
                    chat_id,
                    picture,
                    reply_markup=markup
                )
            except telebot.apihelper.ApiTelegramException:
                print(f'Error sending photo: {picture}')
    return sent_message
