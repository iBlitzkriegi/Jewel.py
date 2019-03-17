from commands.general import GeneralCommands
from commands.staff import StaffCommands
from Util import get_size
from discord.ext import commands

description = 'Jewel, the magical bot!'

bot = commands.Bot(command_prefix='!', description='Jewel the magical Discord bot')
bot.add_cog(StaffCommands.Staff(bot))
bot.add_cog(GeneralCommands.General(bot))


@bot.event
async def on_ready():
    print('----')
    print(bot.user.name + ' is up and ready to serve ' + get_size(bot.guilds) + ' guilds!')
    print('----')


bot.run('')
