from __future__ import annotations


class User:
    def __init__(self, user: dict) -> None:
        self.id: int = user['id']
        self.is_bot: bool = user.get('is_bot')
        self.first_name: str = user.get('first_name')
        self.last_name: str = user.get('last_name')
        self.username: str = user.get('username')
        self.language_code: str = user.get('language_code')

    def __repr__(self) -> str:
        return str(self.__dict__)


class Chat:
    def __init__(self, chat: dict) -> None:
        self.id: int = chat.get('id')
        self.first_name: str = chat.get('first_name')
        self.last_name: str = chat.get('last_name')
        self.username: str = chat.get('username')
        self.type: str = chat.get('type')

    def __repr__(self) -> str:
        return str(self.__dict__)


class Message:
    def __init__(self, message: dict) -> None:
        self.from_user = User(message.get('from'))
        self.chat = Chat(message.get('chat'))
        self.date: int = message.get('date')
        self.text: int = message.get('text')

    def __repr__(self) -> str:
        return str(self.__dict__)


class Update:
    def __init__(self, update: dict) -> None:
        self.update_id = update['update_id']
        self.message = Message(update.get('message'))

    def __repr__(self) -> str:
        return str(self.__dict__)
