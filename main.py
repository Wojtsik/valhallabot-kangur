import discord
import os
TOKEN = 'tuidzietoken'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(intents=intents, activity = discord.Game(name="Test1234"))


@bot.event #ładowanie komend w folderze /cogs
async def on_ready(): 
    print(f'Zalogowano jako {bot.user.name}')

for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'): 
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Załadowano: {filename[:-3]}")
    else:
        print("Nie znaleziono więcej plików .py")

@bot.slash_command() #teoretcznie powinno przeładować cogi bez wyłączania bota
async def reload(ctx):
    if filename.endswith('.py'): 
        bot.unload_extension(f'cogs.{filename[:-3]}')
    if filename.endswith('.py'): 
        bot.load_extension(f'cogs.{filename[:-3]}')
    await ctx.respond('przeładowano')

bot.run(TOKEN)
