from discord.ext import commands


def is_owner():
    async def predicate(ctx):
        return ctx.author.id == 98208218022428672

    return commands.check(predicate)


class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='stop',
        aliases=['shutdown'],
        description='This is a command for staff only to stop the bot'
    )
    @is_owner()
    async def stop_bot(self, ctx):
        """Shutdown the bot"""
        await ctx.send('Oh, alright... I\'ll just shutup I guess.. :wave:')
        await self.bot.close()
