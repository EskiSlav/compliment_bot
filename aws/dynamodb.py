from __future__ import annotations

from hashlib import sha1

import boto3

from .models import Compliment
from tg.models import User


class DynamoDB:
    USERS_TABLE = 'users'
    COMPLIMENTS_TABLE = 'compliments'

    def __init__(self) -> None:
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

    def put_compliment(self, compliment: Compliment) -> bool:
        table = self.dynamodb.Table(DynamoDB.COMPLIMENTS_TABLE)
        response = table.put_item(
            Item={
                'id': sha1(compliment.compliment).hexdigest(),
                'compliment': compliment.compliment,
                'translated_compliment': compliment.compliment_ua,
            },
        )
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        return bool(status_code)

    def put_user(self, user: User) -> bool:
        table = self.dynamodb.Table(DynamoDB.USERS_TABLE)
        response = table.put_item(
            Item={
                'id': user.id,
                'is_bot': user.is_bot,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'language_code': user.language_code,
            },
        )
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        return bool(status_code)
