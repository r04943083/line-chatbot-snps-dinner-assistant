import os
from singleton_decorator import singleton
from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import (
    TextSendMessage, ImageSendMessage
)

@singleton
class LineBotMgr:
    def __init__(self):
        self._channel_secret = str(os.getenv('CHANNEL_SECRET'))
        self._channel_access_token = str(os.getenv('CHANNEL_ACCESS_TOKEN'))
        self._line_bot_api = LineBotApi(self._channel_access_token)
        self._handler = WebhookHandler(self._channel_secret)
    
    @property
    def line_bot_api(self):
        return self._line_bot_api
    
    @property
    def handler(self):
        return self._handler
    
    def TextSendMessage(self, event, text):
        message = TextSendMessage(text)
        self._line_bot_api.reply_message(event.reply_token, message)