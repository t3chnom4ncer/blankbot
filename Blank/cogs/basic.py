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

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#welcome DM daemon
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_message = "Welcome to our server! We hope you enjoy your stay."
        try:
            await member.send(welcome_message)
        except nextcord.Forbidden:  # DMs are disabled
            pass


#FOOTER (for all cog files)
def setup(bot):
    bot.add_cog(basic(bot))
