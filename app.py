from flask import Flask, request
import requests

app = Flask(__name__)

# ======================
# 1. 请在这里填入你的 Bot Token 和 Chat ID（仅修改这两行！）
# ======================
TELEGRAM_BOT_TOKEN = '8264663558:AAGRDUL6iq565BNv7nyOJwb_8lleKotF5dI'  # 🔒 你的 Bot Token（来自 @BotFather）
YOUR_CHAT_ID = '7589258201'          # 🔒 你的 Chat ID（来自 @userinfobot，必须是数字，如 123456789）
# ======================

@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def receive_message():
    print("🔔 收到 Telegram 请求！")  # ✅ 打印日志：确认请求到达
    update = request.get_json()
    print("📥 请求内容：", update)    # ✅ 打印原始 JSON 数据，调试用

    if 'message' in update:
        chat_id = update['message']['chat']['id']
        user_text = update['message']['text']

        # 只处理你自己的 Chat ID（安全，可选，避免其他人触发）
        if str(chat_id) != YOUR_CHAT_ID:
            return {'ok': True}

        # 模拟 AI 回复内容
        ai_reply = f"🤖 AI 模拟回复（本地 Python 3.12.4）：你刚才说：「{user_text}」，我已收到！"

        # 调用 Telegram Bot API，发送回复消息给你
        requests.post(
            f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage',
            json={'chat_id': chat_id, 'text': ai_reply}
        )
    return {'ok': True}

if __name__ == '__main__':
    print("🚀 本地服务启动！运行在 http://127.0.0.1:5000")
    print("📡 请使用 ngrok 暴露此服务，以便 Telegram 能访问（公网 URL 如：https://xxxx.ngrok-free.dev/你的_Bot_Token）")
    app.run(port=5000)