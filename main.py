import discord
import os
TOKEN = 'TOKEN'

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = discord.Bot(intents=intents, activity = discord.Game(name="Sasaki Alpha"))


@bot.event #ładowanie komend w folderze /cogs
async def on_ready(): 
    print(f'Zalogowano jako {bot.user.name}')

for filename in os.listdir('./cogs'): 
    if filename.endswith('.py'): 
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"Załadowano: {filename[:-3]}")


bot.run(TOKEN)
