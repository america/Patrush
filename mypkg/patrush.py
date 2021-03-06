#!/usr/bin/env python
# -*- coding: utf-8 -*-
import discord
import os
import traceback
import logging
import random

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# 接続に必要なオブジェクトを生成
client = discord.Client()
# 環境変数からトークンを読み込む
token = os.environ['DISCORD_BOT_TOKEN']


# 起動時に動作する処理
@client.event
async def on_ready():
    logger.debug("on_ready")
    print("on_ready")
    logger.debug(discord.__version__)
    print(discord.__version__)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return None

    if message.content == 'パトラッシュ':
        list = [" 呼んだ？",
                " なんでしょうか？"
                ]

        msg = message.author.mention + random.choice(list)
        await message.channel.send(msg)

    # 辞書
    cmd_dict = {
        '/neko': 'にゃーん',
        '/inu': 'わんっ',
        'お名前は？': client.user.name,
    }

    if message.content in cmd_dict:
        try:
            await message.channel.send(cmd_dict[message.content])
        except Exception:
            traceback.print_exc()

client.run(token)
