#HEAD------------------------------------------------------------------
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

#initial declarations
intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='? ',intents=intents)
#/head

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: nextcord.Member, *, reason=None):
        await user.kick(reason=reason)
        await ctx.send(f"{user.mention} has been kicked for: {reason}")
        print(f'kick - used by {ctx.author.mention} in #{ctx.channel.name}')
        logging.info(f'kick - used by {ctx.author.mention} in #{ctx.channel.name}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        print(f'clear - used by {ctx.author.mention} in #{ctx.channel.name}')
        logging.info(f'serverinfo - used by {ctx.author.mention} in #{ctx.channel.name}')

#FOOTER (for all cog files)
def setup(bot):
    bot.add_cog(Admin(bot))
