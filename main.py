# -*- coding:utf-8 -*-
import discord
from randgame import *
from discord.ext import commands as com

game = game()
from colorama import Fore, init

token = open("token.txt", "r").read()
from discord.ext import commands as com

intents = discord.Intents.all()
bot = com.Bot(command_prefix="-", intents=intents)


@bot.event
async def on_ready():
    print(
        Fore.YELLOW,
        "\n\n\t      Security " + Fore.RED + "Puppet " + Fore.GREEN +
        "korumaya " + Fore.CYAN + "hazır" + Fore.LIGHTMAGENTA_EX + "..!\n")


@bot.command()
async def randnum(ctx):
    try:
        await ctx.send(game.randnum())
        print('Randint fonksiyonu gönderildi..\n')
    except:
        ctx.send("Error..!")

@bot.command()
@com.has_role('Puppet')
async def erase(ctx, amount=5):
    try:
        await ctx.channel.purge(limit=amount + 1)
    except:
        await ctx.channel.send("Error..!")

@bot.command()
@com.has_role('Puppet')
async def clone(ctx, amount=1):
    try:
        for i in range(amount):
            await ctx.channel.clone()
    except:
        await ctx.channel.send("Error..!")
@bot.command()
@com.has_role('Puppet')
async def delete(ctx,amount=1):
  try:
    for i in range(amount):
      await ctx.channel.delete()
  except Exception as e:
    await ctx.channel.send("Error..!")
    await ctx.channel.send(e)

bot.run(token)
