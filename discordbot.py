import discord
import re

TOKEN = "OTc4MDgzNzIyNDc1NzQ5Mzg2.GTPmgi.a0CrGadvFKAaAM3lRLgykADYrnf3tBYlInKoN4";
client = discord.Client()

def vtuber(msg):
    is_vtuber = False
    false_positive = None
    check_message = re.sub(r"[^a-zA-Z0-9]+", ' ', msg.lower())

    for vtuber in vtubers:
        if vtuber in check_message:
            if is_vtuber:
                check_message = false_positive
            

















vtubers = set()


@client.event

client.run(TOKEN)