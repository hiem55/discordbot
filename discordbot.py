import re
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print("We are logged in as {0.user}!".format(bot))






















bot.run(TOKEN)