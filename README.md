# Discord Weather Bot
  A simple Discord bot that provides weather information for a given city using the WeatherAPI.
## Add it to your server [here](https://discord.com/api/oauth2/authorize?client_id=1123321796129734676&permissions=84992&scope=bot)

# Requirements

Python 3.x

## Local Installation & Usage

Clone the repository:

```sh
git clone https://github.com/andresaclan/discordbot.git
```
pip install python-dotenv discord requests

### Getting Started
Create a new Discord bot and obtain its token. You can follow the official Discord [documentation](https://discordpy.readthedocs.io/en/stable/discord.html) on how to create a bot and get its token.

### Authentication    
Create a .env file in the root directory of the project and add the following variables:\
\
TOKEN=<your_discord_bot_token>\
OPEN_WEATHER_KEY=<your_open_weather_map_api_key>

### Setup
Customize the command prefix in the Python code ($ by default) if desired.

### Usage
Run the bot:
```sh
python bot.py
```
The bot listens for commands in Discord channels. Here's an example of how to use it:
```sh
$weather <city>
```
Replace <city> with the name of the city you want to get the weather information for.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
