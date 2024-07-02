import discord
from discord.ext import commands
from discord.commands import Option

import json
import requests


class lupy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="lupy", description="Wysyła łupy danego gracza", guild_ids=[1257688368767176785])

    async def lupy(self, ctx: discord.ApplicationContext, gracz: Option(str, "Wpisz nazwę gracza")): # type: ignore

        link = (f'https://empire-api.fly.dev/EmpireEx_5/hgh/"LT":2,"SV":"{gracz}"')
        print(link)
        json_download = requests.get(link)
        todos = json.loads(json_download.text)
        rank = todos['content']['FR']   
        gracz1 = todos['content']['SV']
        if todos['return_code']=="0":
            for i in range(0,10):
                if rank==todos['content']['L'][i][0]:
                    lupy = todos['content']['L'][i][1]
                    formattedlupy = f"{lupy:,d}".replace(',', ' ')
            await ctx.respond(f'Gracz {gracz1} w tym tygodniu pozyskał {formattedlupy} puntków rabunku')
        else:
            await ctx.respond('ERROR')
def setup(bot):
    bot.add_cog(lupy(bot))
