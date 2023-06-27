import discord
import os
from dotenv import load_dotenv
import weather

# load .env variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$getweather'):
        response = weather.fetch_weather('San Jose')
        embed = discord.Embed(title='Weather', description='The current, realtime weather data for San Jose')
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/1123321796129734676/e39042077a496ed27c93d35780abb28d.webp?size=80')
        embed.add_field(name='Temperature in Fahrenheit', value=response["temp_f"], inline=True)
        embed.add_field(name='UV Index', value=response["uv_index"], inline=True)
        await message.channel.send(embed=embed)


client.run(os.getenv('TOKEN'))

