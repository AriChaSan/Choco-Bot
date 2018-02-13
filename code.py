# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio

from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
bot = Bot(description="ChocoBot", command_prefix="", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@bot.event
async def on_ready():
	print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(bot.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(bot.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Habchy#1665')
	return await bot.change_presence(game=discord.Game(name='PLAYING AND EATING PYTHON')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@bot.command()
async def ping(*args):
	await bot.say(":ping_pong: Pong!")
	await asyncio.sleep(3)

@bot.command(pass_context=True)
async def say(ctx, *, something=None):
    if something is None:
        await bot.say("What would you like me to say?")
    else:
        await bot.say(something)

@bot.command(pass_context=True)
async def say1(ctx, *, something):
    await bot.say("**{} said:** {}".format(str(ctx.message.author), something))
    await bot.delete_message(ctx.message)

bot.run('NDExMDUzOTQ1MDc5OTg4MjI1.DV51Og.LKAkCy_ChsGdVGQtZiCwvwZTTq8')



# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
