from commands.general import GeneralCommands
from commands.staff import StaffCommands
import Util
from discord.ext import commands

description = 'Jewel, the magical bot!'
token = None

bot = commands.Bot(command_prefix='!', description='Jewel the magical Discord bot')
bot.add_cog(StaffCommands.Staff(bot))
bot.add_cog(GeneralCommands.General(bot))

config = open('./ignore/config.yml')
for s in config:
    token = s


@bot.event
async def on_ready():
    print('------------------------------------------------')
    print(bot.user.name + ' is up and ready to serve ' + Util.get_size(bot.guilds) + ' guilds!')
    print('------------------------------------------------')


if token is not None:
    bot.run(token)
    token = None
else:
    Util.print_error('Could not parse config file! Could be missing or corrupt.')
