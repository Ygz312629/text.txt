import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben bir botum!')


@bot.command()
async def goodbye(ctx):
    await ctx.send(f'Görüşürüz!')

bot.run("token")
