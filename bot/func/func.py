from __future__ import annotations

import logging

from aws.dynamodb import DynamoDB
from tg.bot import Bot
from tg.models import Update
from tg.models import User
# from aws.models import Compliment
# from aws.models import NewCompliment

logger = logging.getLogger(__name__)

db = DynamoDB()
bot = Bot()

default_message = r'Your message is accepted\! Wait 9:00 Kyiv '
default_message += r'time for your compliment\! Have a great day'


def update_handler(update: Update):
    put_user_to_the_table(update.message.from_user)
    logger.info(
        f'{update.message.text} == "Саша то кохання?" | {update.message.text == "Саша то кохання?"}',
    )

    if update.message.text == 'Саша то кохання?' or 'саша' in update.message.text.lower():
        bot.send_message(
            update.message.chat.id,
            r'Саша то *шалене* кохання\!❤️❤️❤️',
        )
    else:
        bot.send_message(update.message.chat.id, default_message)


def put_user_to_the_table(user: User):
    if db.put_user(user):
        return True
