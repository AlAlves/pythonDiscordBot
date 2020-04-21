from auth import TOKEN
import codeNames as cn
import dice as d
import discord
from discord.ext import commands
from googletrans import Translator
import os
import random

# INIT
translator = Translator()
prefix = "!!"
bot = commands.Bot(command_prefix=prefix)

# ON READY
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# COMMANDS

#CODENAMES
@bot.command(name='codenames', help='Set up a CodeNames')
async def codeNames(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    msg = 'Go pour un codenames {0.author.mention}'.format(message)
    await message.channel.send(msg)

    # cn.imageGridNeutral(cn.createWordGrid())
    # cn.imageGridColored(cn.createWordGrid())
    pathNeutral = cn.imageGridNeutral(cn.createWordGrid())
    pathColored = cn.imageGridColored(cn.createWordGrid())

    await message.channel.send("La grille neutre : ", file=discord.File(pathNeutral))
    await message.channel.send("La grille de team : ")
    await message.channel.send(file=discord.File(pathColored))

# ROLLING DICE
@bot.command(name='rd', help='Roll <N> dice with <M> faces (cmd : '+prefix+'rd <N>d<M>)')
async def roll(message, arg):
    l = arg.split("d")

    if(len(l) != 2):
        await message.channel.send('cmd : '+prefix+'rd <N>d<M>')
        return
    try:
        int(l[0])
        int(l[1])
    except ValueError:
        await message.channel.send('cmd : '+prefix+'rd <N>d<M>')
        return

    number_of_dice = int(l[0])
    number_of_sides = int(l[1])

    await message.channel.send(d.presentRollingDice(number_of_dice, number_of_sides))

# @bot.command(name='', help='')
# async def

bot.run(TOKEN)
