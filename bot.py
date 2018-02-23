import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$$', description='A bot that greets the user back.')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
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
