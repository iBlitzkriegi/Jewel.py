from discord.ext import commands
from Util import get_size


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='server',
        description='Get information about the current server',
        aliases=['guild', 'guild_info', 'server_info']
    )
    async def server_info(self, ctx):
        """Get information about the current server"""
        server_info = []
        server_info.append("-=Server Information=-")
        server_info.append("```")
        server_info.append("Name: " + ctx.guild.name)
        server_info.append("ID: " + str(ctx.guild.id))
        server_info.append("Owner: " + ctx.guild.owner.name + "#" + ctx.guild.owner.discriminator)
        server_info.append("Members: " + get_size(ctx.guild.members))
        server_info.append("Channels: " + get_size(ctx.guild.channels))
        server_info.append("Region: " + str(ctx.guild.region))
        server_info.append("```")
        await ctx.send("\n".join(server_info))

    @commands.command(
        name='invite'
    )
    async def invite_bot(self, ctx):
        """Get the bot's invite URL."""
        await ctx.send(
            'Here is my invite URL' + ctx.author.mention + '! <https://discordapp.com/oauth2/authorize?client_id=' + str(
                self.bot.user.id) + '&scope=bot&permissions=0>')
