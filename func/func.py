from __future__ import annotations

from aws.dynamodb import DynamoDB
from tg.models import User
# from aws.models import Compliment
# from aws.models import NewCompliment
# from tg.models import Update

db = DynamoDB()


def put_user_to_the_table(user: User):
    if db.put_user(user):
        return True
