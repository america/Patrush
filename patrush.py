import discord
import os
import traceback

# 接続に必要なオブジェクトを生成
client = discord.Client()
# 環境変数からトークンを読み込む
token = os.environ['DISCORD_BOT_TOKEN']

# 起動時に動作する処理
@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    # マップ
    cmd_map = {
        '/neko': 'にゃーん',
        '/inu': 'わんっ',
        'お名前は？': client.user.name
    }

    try:
        await message.channel.send(cmd_map[message.content])
    except KeyError as ke:
        traceback.print_exc()
    
client.run(token)
