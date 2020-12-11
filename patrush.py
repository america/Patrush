import discord
import traceback

# 接続に必要なオブジェクトを生成
client = discord.Client()

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
#        raise ValueError('Invalid content: {}'.format(message.content))
#        raise ke
        traceback.print_exc()
    
# アクセストークンが書かれたファイルを読み込み専用で開く
f = open('AT.txt', 'r', encoding='UTF-8')
# ファイルを読み込む
token = f.read()
# ファイルを閉じる
f.close()

client.run(token)
