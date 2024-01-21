import os
import requests
import discord
from discord.ext import commands
from aiohttp import web

# Discord bot token
BOT_TOKEN = os.getenv('NDIzMDIzMjA4MTgzMTAzNDg5.GEbC-y.6oSj8TY13WzbcwAHmXUwk_kTBFUkSGAz-2U4HU')

# Webhook URL
WEBHOOK_URL = os.getenv('https://hook.eu2.make.com/pyn955jukt45ptx39k2diiuxf8vyzdyq')

# Set up the bot
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Avoid the bot responding to itself
    if message.author == bot.user:
        return

    # Call the webhook when a message is received
    try:
        requests.post(WEBHOOK_URL)
        print("Webhook triggered successfully.")
    except Exception as e:
        print(f"Error triggering webhook: {e}")

    # Process commands
    await bot.process_commands(message)

async def start_bot():
    bot.loop.create_task(bot.start(BOT_TOKEN))
    app = web.Application()
    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Default to 8080 if PORT not set
    web.run_app(start_bot(), port=port)