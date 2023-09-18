import telebot
from telebot.types import Message
from gdrive_processors import GSheet

from model import UserAnswers
from constants import (
    QUESTIONNAIRE_CITY, QUESTIONNAIRE_LIVE_PLACE, QUESTIONNAIRE_DOG_PLACE,
    QUESTIONNAIRE_CHILDREN, QUESTIONNAIRE_OTHER_ANIMALS,
    QUESTIONNAIRE_DOG_EXPERIENCE, QUESTIONNAIRE_DOG_CHOICE,
    QUESTIONNAIRE_CONTACT_NUMBER, QUESTIONNAIRE_THANKS,
    POLL_SHEET_NAME,
)
from button_data_1_lvl import RETURN_BUTTON_VALUE
from utils import build_reply_markup, send_start_menu_message


gsheet = GSheet()
USER_QUESTIONNAIRE_DATA: dict[str, UserAnswers] = {}


def start_form(message: Message,
               bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    user = message.from_user
    name = f'{user.first_name} {user.last_name}'
    answer = UserAnswers(name, user.username)
    USER_QUESTIONNAIRE_DATA[message.chat.id] = answer
    msg = bot.send_message(
        message.chat.id,
        QUESTIONNAIRE_CITY,
        reply_markup=markup,
    )
    bot.register_next_step_handler(msg, process_city, bot)
    return msg


def process_city(message: telebot.types.Message,
                 bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    city = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.city = city
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_LIVE_PLACE,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_live_place, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_live_place(message: Message,
                       bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    place = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.place = place
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_DOG_PLACE,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_dog_place, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_dog_place(message: Message,
                      bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    dog_place = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.dog_place = dog_place
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_CHILDREN,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_children, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_children(message: Message,
                     bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    children = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.children = children
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_OTHER_ANIMALS,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_other_animals, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_other_animals(message: Message,
                          bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    other_animals = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.other_animals = other_animals
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_DOG_EXPERIENCE,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_dog_experience, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_dog_experience(message: Message,
                           bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    dog_experience = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.dog_experience = dog_experience
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_DOG_CHOICE,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_dog_choice, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_dog_choice(message: Message,
                       bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    dog_choice = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.dog_choice = dog_choice
    if message.text != RETURN_BUTTON_VALUE:
        msg = bot.reply_to(message,
                           QUESTIONNAIRE_CONTACT_NUMBER,
                           reply_markup=markup)
        bot.register_next_step_handler(msg, process_contact_number, bot)
        return msg
    else:
        process_start_menu(message, bot)


def process_contact_number(message: Message,
                           bot: telebot.TeleBot) -> Message:
    markup = build_reply_markup((RETURN_BUTTON_VALUE,))
    chat_id = message.chat.id
    contact_number = message.text
    answer = USER_QUESTIONNAIRE_DATA[chat_id]
    answer.contact_number = contact_number
    msg = bot.send_message(chat_id, QUESTIONNAIRE_THANKS, reply_markup=markup)
    save_answer(answer, chat_id)
    bot.register_next_step_handler(msg, process_start_menu, bot)
    return msg


def process_start_menu(message: Message,
                       bot: telebot.TeleBot) -> Message:
    if message.text == RETURN_BUTTON_VALUE:
        msg = send_start_menu_message(bot, message)
    return msg


def save_answer(answer: UserAnswers, chat_id: str) -> None:
    available_row_number = gsheet.next_available_row(POLL_SHEET_NAME)
    gsheet.update_row(POLL_SHEET_NAME, f'A{available_row_number}',
                      [answer.to_list()])
    del USER_QUESTIONNAIRE_DATA[chat_id]
