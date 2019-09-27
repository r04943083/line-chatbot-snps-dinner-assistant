from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('jgex4RHeYTbbBBwCOvMNB8X4mrM/ZHWShjsrqmjDra43C5knZBPW7O8rMBDU8O24RTAFm+V78G504OO6J/i+XQ78lgwYVDDO6o1lmf+P544hW/i33/Zkqq0aLdrhKcOwKatp7oCm8aw0bYExRcMGtgdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('d57f5ce688eaf2c98c0d54468bbfbfbc')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
