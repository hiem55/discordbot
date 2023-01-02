from discord.ext import commands
from discord import utils
import discord


class emotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def getemote(self, arg):
        emotes = utils.get(self.bot.emotes, name=arg.strip(":"))

        if emotes is not None:
            if emotes.animated:
                animate = "a"
            else:
                animate = ""
            return f"<{animate}:{emotes.name}:{emotes.id}>"
        else:
            return None

    async def getinstruction(self, content):
        ret = []

        spc = content.split(" ")
        cnt = content.split(":")

        if len(cnt) > 1:
            for item in spc:
                if item.count(":") > 1:
                    wr = ""
                    if item.startswith("<") and item.endswith(">"):
                        ret.append(item)
                    else:
                        cnt = 0
                        for i in item:
                            if cnt == 2:
                                aaa = wr.replace(" ", "")
                                ret.append(aaa)
                                wr = ""
                                cnt = 0

                            if i != ":":
                                wr += i
                            else:
                                if wr == "" or cnt == 1:
                                    wr += " : "
                                    cnt += 1
                                else:
                                    aaa = wr.replace(" ", "")
                                    ret.append(aaa)
                                    wr = ":"
                                    cnt = 1
                        aaa = wr.replace(" ", "")
                        ret.append(aaa)
                else:
                    ret.append(item)
        else:
            return content

        return ret

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if ":" in message.content:
            msg = await self.getinstruction(message.content)
            ret = ""
            em = False
            smth = message.content.split(":")
            if len(smth) > 1:
                for word in msg:
                    if word.startswith(":") and word.endswith(":") and len(word) > 1:
                        emotes = await self.getemote(word)
                        if emotes is not None:
                            em = True
                            ret += f" {emotes}"
                        else:
                            ret += f" {word}"
                    else:
                        ret += f" {word}"
            else:
                ret += msg

            if em:
                webhooks = await message.channel.webhooks()
                webhook = utils.get(webhooks, name="NQN LOOKALIKE")
                if webhook is None:
                    webhook = await message.channel.create_webhook(name="NQN LOOKALIKE")

                await webhook.send(ret, username=message.author.name, avatar_url=message.author.avatar_url)
                await message.delete()


async def setup(bot):
    await bot.add_cog(emotes(bot))
