
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Pokazuje ping bota", guild_ids=[1257688368767176785])
    async def ping(self, ctx):
        await ctx.respond(f'Ping wynosi {(self.bot.latency) * 1000:.2f}ms')

def setup(bot):
    bot.add_cog(ping(bot))
