from typing import Optional, Tuple
import telebot
from telebot import types
from telebot.util import quick_markup
from constants import (
    CATALOG_URL,
    START_SCREEN_TEMPLATE,
    MONOBANK_URL,
    PRIVAT_BANK_URL,
    GOOGLE_FORM_HAPPY_STORY_URL
)
from button_data_1_lvl import (
    CATALOG_BUTTON_VALUE,
    MAIN_SCREEN_BUTTONS,
    BUTTON_BY_TEXT_1_LVL,
    BUTTON_CLICK_MESSAGE_1_LVL,
    MESSAGE_USEFUL_INFO_BUTTON_VALUE,
    MAKE_DONATION_BUTTON_VALUE,
    TELL_STORY_BUTTON_VALUE
)
from button_data_2_lvl import (
    BUTTON_BY_TEXT_2_LVL,
    BUTTON_CLICK_MESSAGE_2_LVL,
)
from button_data_3_lvl import BUTTON_BY_TEXT_3_LVL
from button_data_4_lvl import BUTTON_BY_TEXT_4_LVL


def build_reply_markup(
    button_list: Optional[Tuple[str, ...]],
    one_time_keyboard: bool = True,
    row_width: int = 2,
    resize_keyboard: bool = True
) -> types.ReplyKeyboardMarkup:
    """_summary_
    This function builds a reply markup for the bot.
    Here is an example of how to use it:

    YES_NO = ("Yes", "No")

    markup = build_reply_markup(constants.YES_NO)

    msg = bot.reply_to(
        initialMessage,
        "Do you want to continue?",
        reply_markup=markup
    )

    It will return a markup (table) with two buttons: "Yes" and "No".
    You can use it to quickly create a reply buttons for the bot.

    Args:
        button_list (tuple[str]):
            It is a tuple of strings. Each string is a button.
        one_time_keyboard (bool, optional):
            Defaults to True.
        row_width (int, optional):
            It is a number of buttons in a row. Defaults to 2.
        resize_keyboard (bool, optional):
            It is a flag to resize the keyboard. Defaults to True.

    Returns:
        types.ReplyKeyboardMarkup: _description_
    """
    if button_list is None:
        button_list = MAIN_SCREEN_BUTTONS
    markup = types.ReplyKeyboardMarkup(
        one_time_keyboard=one_time_keyboard,
        resize_keyboard=resize_keyboard,
        row_width=row_width,
    )

    buttons = [types.KeyboardButton(i) for i in button_list]
    markup.add(*buttons)

    return markup


def build_inline_markup(
    button_list: dict[str, str],
    row_width: int = 2,
) -> types.InlineKeyboardButton:
    """_summary_
    Usage:
    This function builds a markup inside messages.

    Args:
        button_list (dict[str, str]): _description_
        row_width (int, optional): _description_. Defaults to 2.

    Returns:
        types.InlineKeyboardButton: _description_
    """
    markup = types.InlineKeyboardMarkup(row_width=row_width)

    for button, url in button_list.items():
        markup.add(
            types.InlineKeyboardButton(button, url=url)
        )

    return markup


def send_start_menu_message(bot: telebot.TeleBot,
                            message: telebot.types.Message
                            ) -> telebot.types.Message:
    markup = build_reply_markup(MAIN_SCREEN_BUTTONS)
    return bot.send_message(
        message.chat.id,
        START_SCREEN_TEMPLATE.format(first_name=message.from_user.first_name),
        reply_markup=markup,
    )


def send_1_lvl_menu_message(bot: telebot.TeleBot,
                            chat_id,
                            message: telebot.types.Message
                            ) -> telebot.types.Message:
    if message.text == TELL_STORY_BUTTON_VALUE:
        markup = quick_markup({
            'Поділитися історією': {'url': GOOGLE_FORM_HAPPY_STORY_URL}
        }, row_width=1)
    else:
        markup = build_reply_markup(BUTTON_BY_TEXT_1_LVL.get(message.text))
    return bot.send_message(
        chat_id,
        BUTTON_CLICK_MESSAGE_1_LVL.get(message.text),
        reply_markup=markup,
    )


def send_2_lvl_menu_message(bot: telebot.TeleBot,
                            chat_id,
                            message: telebot.types.Message
                            ) -> telebot.types.Message:
    if message.text == MAKE_DONATION_BUTTON_VALUE:
        markup = quick_markup({
            'Monobank': {'url': MONOBANK_URL},
            'Privat Bank': {'url': PRIVAT_BANK_URL},
        }, row_width=2)
    elif message.text == CATALOG_BUTTON_VALUE:
        markup = quick_markup({
            'Посилання на каталог': {'url': CATALOG_URL},
        }, row_width=2)
    else:
        markup = build_reply_markup(BUTTON_BY_TEXT_2_LVL.get(message.text))
    return bot.send_message(
        chat_id,
        BUTTON_CLICK_MESSAGE_2_LVL.get(message.text),
        reply_markup=markup,
    )


def send_3_lvl_menu_message(bot: telebot.TeleBot,
                            chat_id,
                            message: telebot.types.Message
                            ) -> telebot.types.Message:
    markup = build_reply_markup(BUTTON_BY_TEXT_3_LVL.get(message.text))
    return bot.send_message(
        chat_id,
        MESSAGE_USEFUL_INFO_BUTTON_VALUE,
        reply_markup=markup,
    )


def send_4_lvl_menu_message(bot: telebot.TeleBot,
                            chat_id,
                            message: telebot.types.Message
                            ) -> telebot.types.Message:
    markup = build_reply_markup(BUTTON_BY_TEXT_4_LVL.get(message.text))
    return bot.send_message(
        chat_id,
        MESSAGE_USEFUL_INFO_BUTTON_VALUE,
        reply_markup=markup,
    )
