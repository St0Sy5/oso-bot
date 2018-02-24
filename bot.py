import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='$$', description='A bear-y good bot!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    """adds two user given numbers"""
    await ctx.send(a+b)

@bot.command()
async def subtract(ctx, a: int, b: int):
    """subtracts two user given numbers"""
    await ctx.send(a-b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    """multiplies two user given numbers"""
    await ctx.send(a*b)

@bot.command()
async def divide(ctx, a: int, b: int):
    """divides two user given numbers"""
    await ctx.send(a/b)

@bot.command()
async def greet(ctx):
    """sends a friendly greeting"""
    await ctx.send(":smiley: :wave: Hello, there!  Hope you're having a bear-y good day!")

@bot.command()
async def cat(ctx):
    """sends a funny cat gif"""
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def bareoso(ctx):
    """sends a link to cool new music"""
    await ctx.send("Check this out: https://bareoso.bandcamp.com/")

@bot.command()
async def info(ctx):
    """returns information about this bot"""
    embed = discord.Embed(title="OSO-bot", description='A bear-y good bot!')
    embed.add_field(name="Author", value="PythonSlut#0477")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=416349280597573632&permissions=2048&scope=bot")
    await ctx.send(embed=embed)

#bot.remove_command('help')

#@bot.command()
#async def help(ctx):
#    embed = discord.Embed(title="OSO-bot", description="A bear-y good bot!")
#    embed.add_field(name="$$add X Y", value="Adds **X** and **Y** together", inline=False)
#    embed.add_field(name="$$multiply X Y", value="Multiplies **X** and **Y** together", inline=False)
#    embed.add_field(name="$$greet", value="Sends a nice message of greeting", inline=False)
#    embed.add_field(name="$$cat", value="Provides a cat gif for eyebleach", inline=False)
#    embed.add_field(name="$$info", value="Prints some info about oso-bot", inline=False)
#    embed.add_field(name="$$help", value="Prints this message", inline=False)
#    await ctx.send(embed=embed)

bot.run('NDE2MzQ5MjgwNTk3NTczNjMy.DXDTZA.d66DpwRthcczhn0yM1epdrH4UsM')
