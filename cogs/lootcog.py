import discord
from discord.ext import commands
from discord.commands import Option

import json
import requests


class lupy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="lupy", description="Wysyła łupy danego gracza")

    async def lupy(self, ctx: discord.ApplicationContext, gracz: Option(str, "Wpisz nazwę gracza"), serwer: Option(str, "pl, cn", choices=["cn", "pl"])): # type: ignore
        if serwer.lower() == "cn":
            link = (f'https://empire-api.fly.dev/EmpireEx_27/hgh/"LT":2,"SV":"{gracz}"')
        elif serwer.lower() == "pl":
            link = (f'https://empire-api.fly.dev/EmpireEx_5/hgh/"LT":2,"SV":"{gracz}"')
        else:
            await ctx.respond("Dostępne opcje to pl (Polska 1) lub cn (Chiński)")
        json_download = requests.get(link)
        todos = json.loads(json_download.text)
        # Checking if player is in DB.
        if todos['return_code']=="0":
            rank = todos['content']['FR']   
            gracz1 = todos['content']['SV']
            for i in range(0,10):
                if rank==todos['content']['L'][i][0]:
                    lupy = todos['content']['L'][i][1]
                    formattedlupy = f"{lupy:,d}".replace(',', ' ')
            await ctx.respond(f'Gracz **{gracz1}** w tym tygodniu pozyskał **{formattedlupy}** punktów rabunku', ephemeral=False)
        else:
            await ctx.respond("Nie znaleziono w bazie :<")
def setup(bot):
    bot.add_cog(lupy(bot))
