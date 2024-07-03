
from discord.ext import commands

class reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="reload")
    async def reload_cogs(self, ctx):
        for extension in self.bot.extensions:
            self.bot.reload_extension(f"{extension}")
            await ctx.respond(f'Przeładowano {extension}', ephemeral=True)

def setup(bot):
    bot.add_cog(reload(bot))
