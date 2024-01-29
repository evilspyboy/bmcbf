  GNU nano 5.4                                                                                        bot.py                                                                                                 
import discord
from discord.ext import commands
import requests

# Discord bot token
BOT_TOKEN = ''  # Replace with your bot token

# Webhook URL
WEBHOOK_URL = ''  # Replace with your webhook URL

# Define Intents
intents = discord.Intents.default()
intents.messages = True  # Assuming you want the bot to read messages

# Set up the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    # Avoid the bot responding to itself
    if message.author.bot:
        return

    # Check if the bot is mentioned in the message
    if bot.user.mentioned_in(message):
        # Bot logic when it is mentioned
        try:
            requests.post(WEBHOOK_URL)
            print("Webhook triggered successfully.")
        except Exception as e:
            print(f"Error triggering webhook: {e}")

    # Process commands
    await bot.process_commands(message)

bot.run(BOT_TOKEN)