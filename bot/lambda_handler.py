from __future__ import annotations

import json
import logging
from logging.config import dictConfig

from config.config import logging_config
from func.func import update_handler
from tg.models import Update


dictConfig(logging_config)
logger = logging.getLogger(__name__)


def main(event, context):
    logger.debug(event)

    update = Update(json.loads(event['body']))

    update_handler(update)

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
