from __future__ import annotations

import json

from aws.ssm import get_ssm_parameter_value
from func.func import put_user_to_the_table
from tg.bot import Bot
from tg.models import Update

default_message = 'Your message is accepted! Wait 9:00 Kyiv '
default_message += 'time for your compliment! Have a great day'


def main(event, context):
    api_token = get_ssm_parameter_value('/config/bot/api_token')
    print(event)

    update = Update(json.loads(event['body']))
    put_user_to_the_table(update.message.from_user)

    bot = Bot(api_token)
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
