#######################################################
#                   ~Bot Loader~                      #
# Shield v0.1                                         #
# https://slurp.space                                 #
# By @A Burnt Bagel#0001                              #
# Licensed under CC0                                  #
#######################################################

import discord
from discord.ext import commands
from configparser import ConfigParser
import os

config = ConfigParser()
config.read(os.getcwd() + '/shield_priv.ini')

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

@bot.event
async def on_ready():
  print('Ready!')

bot.run(config.get('shield', 'token'))
