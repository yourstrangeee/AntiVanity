import os
import discord
from discord.ext import commands
import logging
os.system("pip install git+https://github.com/dolfies/discord.py-self")
token = "your_discord_token"
bot = commands.Bot(command_prefix='-', self_bot=True)

guild_id = "add your guildid"


async def strange(before, after):
    if before.vanity_url_code != after.vanity_url_code:
        try:
            await after.edit(vanity_code=before.vanity_url_code)
        except Exception as e:
            logging.error(f"Failed to restore vanity URL: {e}")

@bot.event
async def on_guild_update(before, after):
    if after.id != guild_id:
        return
    
    async for entry in after.audit_logs(limit=1):
        
        if entry.user.id in [after.owner_id, bot.user.id]:
            return
        
        await strange(before, after)
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

bot.run(token)
