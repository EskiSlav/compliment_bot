from __future__ import annotations

import json

import aws
from tg.bot import Bot
from tg.models import Update
# from aws.ssm import get_ssm_parameter_value
# from aws.translate import Translator


def main(event, context):
    api_token = aws.get_ssm_parameter_value('/config/bot/api_token')
    print(event)

    update = Update(json.loads(event['body']))

    bot = Bot(api_token)
    bot.send_message(update.message.chat.id, 'Wooooow!!!')

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
