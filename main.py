import logging
import telebot
from telebot.types import Message
from button_data_3_lvl import (
    AMMUNITION_BUTTONS,
    CARE_BUTTONS,
    CLOTHES_BUTTONS,
    DOG_COLLAR_BUTTON_VALUE,
    FOOD_BUTTONS,
    TOYS_BUTTONS
)
from button_data_2_lvl import (
    ABOUT_PUPPIES_BUTTONS,
    EDUCATION_AND_LEISURE_BUTTONS,
    HEALT_BUTTONS,
    PLACE_BUTTON_VALUE
)
from button_data_1_lvl import (
    CATALOG_BUTTON_VALUE,
    FORM_BUTTON_VALUE,
    MAIN_SCREEN_BUTTONS,
    MAKE_DONATION_BUTTON_VALUE,
    NEWS_BUTTON_VALUE,
    OTHER_BUTTON_VALUE,
    RETURN_BUTTON_VALUE,
    TELL_STORY_BUTTON_VALUE
)
from constants import TOKEN
from useful_information import filter_info
from questionnaire import start_form
from utils import (
    send_start_menu_message,
    send_1_lvl_menu_message,
    send_2_lvl_menu_message,
    send_3_lvl_menu_message,
    send_4_lvl_menu_message,
)


bot = telebot.TeleBot(TOKEN)

user_path_dict = {}


class Path:
    def __init__(self, button_1_level):
        self.button_1_level = button_1_level
        self.button_2_level = None
        self.button_3_level = None
        self.button_4_level = None


@bot.message_handler(func=lambda message: message.text in MAIN_SCREEN_BUTTONS
                     or message.text.startswith('/start'))
def start_handler(message: Message):
    message_sent = send_start_menu_message(bot, message)
    bot.register_next_step_handler(message_sent, process_1_lvl_buttons)


def process_1_lvl_buttons(message: Message):
    chat_id = message.chat.id

    if (message.text != RETURN_BUTTON_VALUE and
       message.text != TELL_STORY_BUTTON_VALUE):
        button_1_level = message.text
        path = Path(button_1_level)
        user_path_dict[chat_id] = path
        message_sent = send_1_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
            message_sent,
            process_2_lvl_buttons,
            )
    elif message.text == TELL_STORY_BUTTON_VALUE:
        message_sent = send_1_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
            message_sent,
            process_1_lvl_buttons,
        )


def process_2_lvl_buttons(message: Message):
    chat_id = message.chat.id

    if message.text == RETURN_BUTTON_VALUE:
        message_sent = send_start_menu_message(bot, message)
        bot.register_next_step_handler(message_sent, process_1_lvl_buttons)

    elif message.text in (NEWS_BUTTON_VALUE, OTHER_BUTTON_VALUE):
        button_2_level = message.text
        path = user_path_dict[chat_id]
        path.button_2_level = button_2_level
        message_sent = filter_info(bot, message)
        bot.register_next_step_handler(
            message_sent,
            process_3_lvl_buttons)

    elif message.text == FORM_BUTTON_VALUE:
        message_sent = start_form(message, bot)

    elif message.text in (MAKE_DONATION_BUTTON_VALUE, CATALOG_BUTTON_VALUE):
        message_sent = send_2_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(message_sent,
                                       process_2_lvl_buttons)

    else:
        button_2_level = message.text
        path = user_path_dict[chat_id]
        path.button_2_level = button_2_level
        message_sent = send_2_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
                message_sent,
                process_3_lvl_buttons,
            )


def process_3_lvl_buttons(message: Message):
    chat_id = message.chat.id

    if message.text == RETURN_BUTTON_VALUE:
        path = user_path_dict[chat_id]
        message.text = path.button_1_level
        message_sent = send_1_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
                message_sent,
                process_2_lvl_buttons,
            )

    elif ((message.text in HEALT_BUTTONS or
           message.text in ABOUT_PUPPIES_BUTTONS or
           message.text in EDUCATION_AND_LEISURE_BUTTONS or
           message.text in PLACE_BUTTON_VALUE) and
          message.text != RETURN_BUTTON_VALUE):
        message_sent = filter_info(bot, message)
        bot.register_next_step_handler(
            message_sent,
            process_4_lvl_buttons)

    else:
        button_3_level = message.text
        path = user_path_dict[chat_id]
        path.button_3_level = button_3_level
        message_sent = send_3_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
                message_sent,
                process_4_lvl_buttons,
            )


def process_4_lvl_buttons(message: Message):
    chat_id = message.chat.id

    if message.text == RETURN_BUTTON_VALUE:
        path = user_path_dict[chat_id]
        message.text = path.button_2_level
        message_sent = send_2_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
            message_sent,
            process_3_lvl_buttons,
        )

    elif ((message.text in CLOTHES_BUTTONS or
           message.text in CARE_BUTTONS or
           message.text in AMMUNITION_BUTTONS or
           message.text in FOOD_BUTTONS or
           message.text in TOYS_BUTTONS) and
          message.text != RETURN_BUTTON_VALUE and
          message.text != DOG_COLLAR_BUTTON_VALUE):
        message_sent = filter_info(bot, message)
        bot.register_next_step_handler(
            message_sent,
            process_5_lvl_buttons)

    else:
        button_4_level = message.text
        path = user_path_dict[chat_id]
        path.button_4_level = button_4_level
        message_sent = send_4_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(message_sent, process_5_lvl_buttons)


def process_5_lvl_buttons(message: Message):
    if message.text == RETURN_BUTTON_VALUE:
        chat_id = message.chat.id
        path = user_path_dict[chat_id]
        message.text = path.button_3_level
        message_sent = send_3_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(
            message_sent,
            process_4_lvl_buttons,
        )

    else:
        message_sent = filter_info(bot, message)
        bot.register_next_step_handler(message_sent, process_6_lvl_buttons)


def process_6_lvl_buttons(message: Message):
    if message.text == RETURN_BUTTON_VALUE:
        chat_id = message.chat.id
        path = user_path_dict[chat_id]
        message.text = path.button_4_level
        message_sent = send_4_lvl_menu_message(bot, chat_id, message)
        bot.register_next_step_handler(message_sent,
                                       process_5_lvl_buttons)


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers
# (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file
# (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()


# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()
def main():
    # try:
    telebot.logger.setLevel(logging.DEBUG)
    bot.infinity_polling(logger_level=logging.DEBUG, timeout=10,
                         long_polling_timeout=5)
    # except Exception as e:
    #     print(f'Exception: {str(e)}')


if __name__ == "__main__":
    main()
