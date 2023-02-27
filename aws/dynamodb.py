from __future__ import annotations

from hashlib import sha1

import boto3


class DynamoDB:
    def __init__(self) -> None:
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

    def put_compliment(self, compliment, translated_compliment) -> None:
        table = self.dynamodb.Table('compliments')
        response = table.put_item(
            Item={
                'id': sha1(compliment).hexdigest(),
                'compliment': compliment,
                'translated_compliment': translated_compliment,
            },
        )
        status_code = response['ResponseMetadata']['HTTPStatusCode']
        return status_code
