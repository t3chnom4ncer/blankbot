#HEAD------------------------------------------------------------------
import time
import nextcord
import os
import config
from nextcord.ext import commands
import logging
from datetime import datetime
import sys
sys.path.append('')#SET TO the bot's root dir!!!

#---logging---
log_directory = 'logs'
log_filename = os.path.join(log_directory, datetime.now().strftime('%m%d%y.log'))

logging.basicConfig(filename=log_filename,
                    level=logging.INFO,
                    format='%(asctime)s | %(levelname)s | %(message)s\n')

logging.info("BlankBot- initialised")

#initial declarations
intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='? ',intents=intents)
#/HEAD

@bot.event
async def  on_ready():
    print(f'logged in as {bot.user.name} ({bot.user.id})')
    print('_____________________________________________________')

# Command: Ping (basic one with no latency measure)
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
    print(f'ping - used by {ctx.author.mention} in #{ctx.channel.name}')
    logging.info(f'ping - used by {ctx.author.mention} in #{ctx.channel.name}')


#Welcome message !!!does not work with new nextcord!!!
@commands.Cog.listener()
async def on_member_join(self, member):
    guild = member.guild
    channel_id = #SET THIS!
    channel = guild.get_channel(channel_id)

    if channel:
        embed = nextcord.Embed(
            title="Welcome!",
            description=f"Welcome to {guild.name}, {member.mention} Enjoy your stay!",
            color=nextcord.color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Information", value="Please read latest info", inline=False)

        await channel.send(embed=embed)

#leave message !!!does not work with new nextcord!!!
@commands.Cog.listener()
async def on_member_remove(self, member):
    guild = member.guild
    channel_id = #SET THIS!
    channel = guild.get_channel(channel_id)

    if channel:
        embed = nextcord.Embed(
            title="Goodbye",
            description=f"{member.mention} has left {guild.name}, peace out!",
            color=nextcord.color.blue()
        )
        embed.set_thumbnail(url=member.avatar.url)

        await channel.send(embed=embed)


#Cog load handler
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(config.TOKEN)
