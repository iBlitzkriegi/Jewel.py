from discord.ext import commands


class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='stop',
        aliases=['shutdown'],
        description='This is a command for staff only to stop the bot'
    )
    async def stop_bot(self, ctx):
        """Shutdown the bot"""
        if ctx.author.id == 98208218022428672:
            await ctx.send('Oh, alright... I\'ll just shutup I guess.. :wave:')
            await self.bot.close()
