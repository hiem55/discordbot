import re
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='$')
TOKEN = os.getenv('DISCORD_TOKEN')


@bot.event
async def on_ready():
    print("We are logged in as {0.user}!".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await bot.process_commands(message)


bot.run(TOKEN)
