import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Intent declaration
intents = discord.Intents.default()  # All but the THREE privileged ones
intents.message_content = True  # Subscribe to the Message Content intent

bot = commands.Bot(command_prefix='.', intents=intents, case_insensitive=True)
cogs = ["events.on_message"]

#send message in console if bot is ready and logged in successfully

@bot.event
async def on_ready():
    print("We are logged in as {0.user}!".format(bot))
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"{cog} was loaded successfully.")
        except Exception as e:
            print(e)


@bot.event
async def on_member_join(member):
    print(f'(member) has joined a server.')


@bot.event
async def on_member_remove(member):
    print(f'(member) has left a server.')


@bot.command(name='test1', aliases=['t1'], pass_context=True)
async def test1(ctx):
    await ctx.send('test command works!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith("hi"):
        await message.channel.send('Hello!')

    await bot.process_commands(message)


# Send a message to the user if the required arguments are missing
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            f'''Correct command: {ctx.prefix}{ctx.command.name} {ctx.command.signature}
    For more help, type `.help {ctx.command.name}` or `.statcommands`'''
        )

#help commands for stat commands

@bot.command(name='statcommands', aliases=['commands'], brief='Show list of command', pass_context=True)
async def statcommands(ctx):
    await ctx.send(
        """```  Game                  Command                                   Example
League of Legends      .lolstat <username>                     .lolstat hiem5
Teamfight Tactics      .tftstat <username>                     .tftstat hiem5
```"""
    )

#possible regions supported by Riot

regions = ['na', 'euw', 'eune', 'oce', 'kr',
           'jp', 'br', 'las', 'lan', 'ru', 'tr', 'sg']


@bot.command(brief='Teamfight Tactics')
async def tftstat(ctx, region, *, username):
    if region.lower() in regions:
        region = region
    if region.lower() not in regions:
        await ctx.send('wrong region, check .help')
        return

    username = username.replace(' ', '')
    await ctx.send(f'https://lolchess.gg/profile/{region}/{username}')

# League of Legends Stat


@bot.command(aliases=['leaguestat'], brief='League of Legends')
async def lolstat(ctx, region, *, username):
    if region.lower() in regions:
        region = region
    if region.lower() not in regions:
        await ctx.send('wrong region, check .help')
        return
    username = username.replace(' ', '%20')
    await ctx.send(f'https://www.op.gg/summoners/{region}/{username}')


bot.run(TOKEN)
