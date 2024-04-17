#-- coding: utf-8 --
import discord
from discord.ext import commands
import asyncio
import requests
from cogs import bili_api # type: ignore
import datetime
import os,json

class BilibiliLiveNotifier(commands.Cog):
    def __init__(self, bot, uid, room_id,channel_id):
        self.bot = bot
        self.uid = uid
        self.room_id = room_id
        self.channel_id = channel_id
        self.live_status = None
        self.loop = asyncio.get_event_loop()

    async def notify_live_start(self):
        info1 = bili_api.get_info(self.uid)
        channel = self.bot.get_channel(self.channel_id)
        name = info1[self.uid]['name']  
        embed = discord.Embed(title=self.live_info[self.uid]['title'], description=f'{name} is streaming.', color=0x03b2f8,url=f'https://live.bilibili.com/{self.room_id}')
        embed.set_author(name=info1[self.uid]['name'], url=f'https://space.bilibili.com/{self.uid}', icon_url=info1[self.uid]['icon'])
        embed.set_image(url=self.live_info[self.uid]['face'])
        embed.timestamp = datetime.datetime.now()
        await channel.send(embed=embed)

    async def check_live_status(self):
        live_status = bili_api.get_info_live(self.uid,self.room_id)
        self.live_info = live_status
        if live_status[self.uid]['live_status'] == 1 and self.live_status != 1:
            self.live_status = 1
            await self.notify_live_start()
        else:
            self.live_status = int( live_status[self.uid]['live_status'] )

    @commands.Cog.listener()
    async def on_ready(self):
        # print(f"{self.bot.user} is ready and online!")
        print("Traking...")
        while True:
            await self.check_live_status()
            await asyncio.sleep(20)

def setup(bot):
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    parent_dir = os.path.join(parent_dir,"config.json")

    with open(parent_dir,"r") as file:
        json_data = json.load(file)
        
    uid = json_data['uid']
    room_id = json_data['room_id']
    channel_id = json_data['channel_ID']
    bot.add_cog(BilibiliLiveNotifier(bot, uid, room_id, channel_id))