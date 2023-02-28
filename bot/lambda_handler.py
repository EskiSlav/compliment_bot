from __future__ import annotations

import json
import logging
from logging.config import dictConfig

from aws.ssm import get_ssm_parameter_value
from config.config import logging_config
from func.func import put_user_to_the_table
from tg.bot import Bot
from tg.models import Update

dictConfig(logging_config)
logger = logging.getLogger(__name__)

default_message = 'Your message is accepted! Wait 9:00 Kyiv '
default_message += 'time for your compliment! Have a great day'


def main(event, context):
    logger.debug(event)

    api_token = get_ssm_parameter_value('/config/bot/api_token')
    update = Update(json.loads(event['body']))
    bot = Bot(api_token)

    put_user_to_the_table(update.message.from_user)
    bot.send_message(update.message.chat.id, default_message)

    body = json.dumps({
        'status': 200,
    })
    ret = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {},
        'body': body,
    }
    return ret


def lambda_handler(event, context):
    return main(event, context)
