#HEAD------------------------------------------------------------------
import nextcord
import os
import config
import requests
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

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="urban dictionary")
    async def urban(self, ctx, term: str):
        api_url = f'https://api.urbandictionary.com/v0/define?term={term}'
        response = requests.get(api_url)
        data = response.json()

        if data.get('list'):
            definition = data['list'][0]['definition']
            await ctx.send(f"**{term.capitalize()}:** {definition}")
        else:
            await ctx.send(f"No definition found for {term}.")
        print(f'urban - used by {ctx.author.mention} in #{ctx.channel.name}')
        logging.info(f'urban - used by {ctx.author.mention} in #{ctx.channel.name}')



#FOOTER (for all cog files)
def setup(bot):
    bot.add_cog(nsfw(bot))
