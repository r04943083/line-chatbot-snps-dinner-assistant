from flask import Flask, request, abort
from line_bot import LineBot

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot = LineBot()
# Channel Access Token
line_bot_api = line_bot.line_bot_api

# Channel Secret
handler = line_bot.handler

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.TextSendMessage(event, event.message.text)
    
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    pass

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
