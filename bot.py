import os
from dotenv import load_dotenv
import requests
import discord
from discord.ext import commands

# load .env variables
load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# weather command
@bot.command()
async def weather(ctx: commands.Context, *, city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": os.getenv('OPEN_WEATHER_KEY'),
        "q": city
    }

    response = requests.get(url, params=params)
    data = response.json()
    location = data['location']['name']
    temp_c = data['current']['temp_c']
    temp_f = data['current']['temp_f']
    uv = data['current']['uv']
    image_url = "http:" + data['current']['condition']['icon']
    condition = data['current']['condition']['text']

    # build embed response
    embed = discord.Embed(title='Weather', description=f'The current weather condition in `{location}` is `{condition}`.')
    embed.set_thumbnail(url=image_url)
    embed.add_field(name='Temperature', value=f"C: {temp_c} | F: {temp_f}", inline=True)
    embed.add_field(name='UV Index', value=uv, inline=True)
    await ctx.channel.send(embed=embed)


bot.run(os.getenv('TOKEN'))

