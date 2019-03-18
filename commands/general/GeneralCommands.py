from discord.ext import commands
from Util import get_size
import discord
import datetime


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

    @commands.command(
        name='embed',
        aliases=['example_embed'],
        description='Get an example embed to see what each part of an embed does'
    )
    async def example_embed(self, ctx):
        """Get an example embed"""
        embed = discord.Embed(
            title='Title',
            description='Description\nThe title leads to the URL, if given.',
            url='https://www.google.com/',
            color=discord.Color.dark_blue(),
            timestamp=datetime.datetime.today()
        )
        embed.set_author(
            name='Author name (Can point to URL)',
            icon_url='https://discordapp.com/assets/28174a34e77bb5e5310ced9f95cb480b.png'
        )
        embed.set_image(
            url='https://media.discordapp.net/attachments/237757030708936714/390520880242884608/8xAac.png?width=508&height=522'
        )
        embed.set_thumbnail(
            url='https://i.imgur.com/sm9JTa9.png')
        embed.add_field(
            name='Field Name',
            value='Color sets\n< that ',
            inline=True
        )
        embed.add_field(
            name='Field Name',
            value='Another split field',
            inline=True
        )
        embed.add_field(
            name='Field Name',
            value='Split is also called inline',
            inline=True
        )
        embed.add_field(
            name='Non-Inline Field Name',
            value='The number of fields that can be shown on the same row is limited to 3, but is limited to 2 when a '
                  'image is included',
            inline=False
        )
        embed.set_footer(
            text='Footer-text',
            icon_url='https://i.imgur.com/sm9JTa9.png'
        )

        await ctx.send(embed=embed)
