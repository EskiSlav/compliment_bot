from __future__ import annotations

import requests


class Bot:
    def __init__(self, token) -> None:
        self.token = token
        self.session = requests.Session()
        self.request_string = f'https://api.telegram.org/bot{self.token}/'

    def send_message(self, chat_id: int, text: str):
        url = self.request_string + 'sendMessage'
        json_data = {
            'chat_id': chat_id,
            'text': text,
        }
        response = self.session.post(url=url, json=json_data)

        return response.status_code
