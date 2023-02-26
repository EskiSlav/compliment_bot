from __future__ import annotations

import json

import boto3

from bot import Bot
from models import Update


def get_ssm_parameter_value(parameter_string, ssm_client=None):
    if ssm_client is None:
        ssm_client = boto3.client('ssm')

    parameter = ssm_client.get_parameter(
        Name=parameter_string, WithDecryption=True,
    )

    return parameter['Parameter']['Value']


def main(event, context):
    api_token = get_ssm_parameter_value('/config/bot/api_token')
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
