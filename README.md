Discord Weather Bot
  A simple Discord bot that provides weather information for a given city using the WeatherAPI.

**Prerequisites**
Before running the bot, make sure you have the following installed:

Python 3.x
  python-dotenv package
  requests package
  discord.py package
  Setup

**Setup**

Clone the repository:
  git clone https://github.com/your-username/discord-weather-bot.git
  
Install the required packages:
  pip install python-dotenv discord requests

Create a new Discord bot and obtain its token. You can follow the official Discord documentation on how to create a bot and get its token.

Create a .env file in the root directory of the project and add the following variables:
  TOKEN=<your_discord_bot_token>
  OPEN_WEATHER_KEY=<your_open_weather_map_api_key>

Customize the command prefix in the Python code ($ by default) if desired.

Run the bot:
  python bot.py

**Usage**
The bot listens for commands in Discord channels. Here's an example of how to use it:
  $weather <city>

Replace <city> with the name of the city you want to get the weather information for.

**Contributing**
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
