import nextcord
import os
import config
from nextcord.ext import commands
from datetime import datetime, timezone
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

# initial declarations
intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='? ', intents=intents)

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command for a better ping with latency measure.
    @commands.command(description="Shows the current latency of the bot.")
    async def tping(self, ctx):
        latency = self.bot.latency * 1000

        embed = nextcord.Embed(
            title="Time Ping",
            description=f'Current ping is of {latency:.2f}ms',
            color=nextcord.Color.blue()
        )
        embed.set_thumbnail(url=ctx.author.avatar.url)

        await ctx.send(embed=embed)
        print(f'tping - used by {ctx.author.mention} in #{ctx.channel.name}')

    # serverinfo command
    @commands.command(name='serverinfo', description="Shows information about the server.")
    async def serverinfo(self, ctx):
        server = ctx.guild
        total_members = len(server.members)
        server_owner = server.owner.display_name
        server_region = str(server.region).capitalize()
        server_creation_date = server.created_at.strftime("%B %d, %Y")

        server_info = f"Server Name: {server.name}\n" \
                      f"Server Owner: {server_owner}\n" \
                      f"Region: {server_region}\n" \
                      f"Total Members: {total_members}\n" \
                      f"Creation Date: {server_creation_date}"

        await ctx.send(server_info)
        print(f'serverinfo - used by {ctx.author.mention} in #{ctx.channel.name}')
        logging.info(f'serverinfo - used by {ctx.author.mention} in #{ctx.channel.name}')

    # userinfo command
    @commands.command(name='userinfo', description="Shows information about the user.")
    async def userinfo(self, ctx, member: nextcord.Member = None):
        member = member or ctx.author
        join_date = member.joined_at.strftime("%Y-%m-%d %H:%M:%S")
        current_time = datetime.now(timezone.utc)
        time_on_server = current_time - member.joined_at
        time_on_server_minutes = divmod(time_on_server.total_seconds(), 60)
        hours, minutes = divmod(time_on_server_minutes[0], 60)

        # Define the embed inside the command function
        embed = nextcord.Embed(title="User Information", color=nextcord.Color.blue())
        embed.set_thumbnail(url=member.avatar.url)

        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined Server", value=join_date, inline=True)
        embed.add_field(name="Time on server", value=f"{int(hours)} hours, {int(minutes)} minutes", inline=False)

        await ctx.send(embed=embed)
        print(f'userinfo - used by {ctx.author.mention} in #{ctx.channel.name}')
        logging.info(f'userinfo - used by {ctx.author.mention} in #{ctx.channel.name}')


# FOOTER (for all cog files)
def setup(bot):
    bot.add_cog(Utility(bot))
