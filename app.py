 #!/usr/bin/python3
 
from flask import Flask, request, abort
from line_bot_mgr import LineBotMgr
from cmd_mgr import CmdMgr

from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, StickerMessage
)

app = Flask(__name__)

line_bot = LineBotMgr()
cmd_mgr = CmdMgr()
# Channel Access Token
#line = line_bot.line_bot_api

# Channel Secret
handler = line_bot.handler

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #line_bot.TextSendMessage(event, event.message.text)
    cmd_mgr.decode(event, event.message.text)
    #cmd_mgr.execute(event)
    
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    pass

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
